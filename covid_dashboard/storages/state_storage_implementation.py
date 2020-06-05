import datetime
from abc import ABC
import datetime
from abc import ABC
from typing import List
from abc import abstractmethod
from collections import defaultdict
from django.db.models import Sum, F, Prefetch
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.models import State, District, Mandal, Stats
from covid_dashboard.exceptions.exceptions import *
from covid_dashboard.interactors.storages.state_storage_interface\
    import StateStorageInterface
state_id, state_name = 1, 'Andhrapradesh'

class StateStorageImplementation(StateStorageInterface):

    def _get_next_stat(self, stats, next):
        if next < len(stats):
            stat = stats[next]
        else:
            stat = {'district_id':None}
        next += 1
        return stat, next

    def _next_day(self, date):
        import datetime
        timedelata = datetime.timedelta(days=1)
        return date + timedelata

    def is_state_id_valid(self, state_id: int):
        try:
            State.objects.get(id=state_id)
        except State.DoesNotExist:
            raise InvalidStateId

    def check_is_date_valid(self, date):
        import datetime
        today = datetime.date.today()
        if date > today:
            raise InvalidDate

    def get_state_wise_daily_report(self, state_id: int) -> StateDto:
        pass

    def get_state_wise_cumulative_report(self, till_date) -> StateDto:
        state_id, state_name = 1, 'Andhrapradesh'
        districts= list(
            District.objects.values_list('id', flat=True)\
                    .filter(state_id=state_id)
            )
    
        districts_cumulative_report = \
            Mandal.objects.values('district_id')\
                          .filter(stats__date__lte=till_date)\
                          .annotate(
                              total_cases=Sum('stats__total_confirmed'),
                              total_deaths=Sum('stats__total_deaths'),
                              total_recovered=Sum('stats__total_recovered'),
                              district_name=F('district__name')
                           )\
                          .filter(district_id__in=districts).order_by('district_id')
        
        districts_cumulative_report_list = list(districts_cumulative_report)

        state_cumulative_report_dto = \
            self._convert_to_state_cumulative_report_dto(
                districts_cumulative_report_list, till_date,
                state_id, state_name)
        return state_cumulative_report_dto

    def _convert_to_state_cumulative_report_dto(self,
            report_list, till_date, state_id, state_name):
        districts = District.objects.values('id','name').order_by('id')
        list_district_dtos = []
        
        next = 0
        report, next = self._get_next_district_report(report_list, next)
        for district in districts:
            if district['id'] == report['district_id']:
                district_dto = self._convert_to_district_cumulative_report_dto(
                    report, till_date
                )
                report, next = self._get_next_district_report(report_list, next)
            else:
                district_dto = self._get_dto_with_zeroes(district, till_date)
            list_district_dtos.append(district_dto)

        state_cumulative_report_dto = StateDto(
                state_id=state_id,
                state_name=state_name,
                stats=list_district_dtos
            )
        return state_cumulative_report_dto

    def _get_next_district_report(self, report_list, next):
        if report_list and next < len(report_list):
            report = report_list[next]
        else:
            report = {
                'district_id':None
            }
        next += 1
        return report, next

    def _get_dto_with_zeroes(self, district, till_date):
        district_dto = DistrictStatDto(
                district_id=district['id'],
                district_name=district['name'],
                date=till_date,
                total_cases=0,
	            total_deaths=0,
	            total_recovered_cases=0,
	            active_cases=0
            )
        return district_dto

    def _convert_to_district_cumulative_report_dto(self,
            district_report, till_date):
        district_dto = DistrictStatDto(
            date=till_date,
            district_id=district_report['district_id'],
            district_name=district_report['district_name'],
            total_cases=district_report['total_cases'],
	        total_deaths=district_report['total_deaths'],
	        total_recovered_cases=district_report['total_recovered'],
	        active_cases=district_report['total_cases'] - \
	           (
	               district_report['total_deaths'] + 
	               district_report['total_recovered']
	           )
	   )
        return district_dto


    def get_daily_cumulative_report(self) -> DailyCumulativeReport:
        stats = Stats.objects.values('date', 'mandal__district__state_id')\
                     .annotate(
                         total_deaths=Sum('total_deaths'),
                         total_confirmed=Sum('total_confirmed'),
                         total_recovered=Sum('total_recovered'))\
                     .filter(mandal__district__state_id=state_id)\
                     .order_by('date')
    
        daily_cumulative_report_dto = \
            self._convert_to_daily_cumulative_report_dto(stats)
        return daily_cumulative_report_dto

    def _convert_to_daily_cumulative_report_dto(self, stats):
        specific_day_report = []
        first, next = 0, 0
        date = stats[first]['date']
        get_next = True
        total_cases, total_deaths, total_recovered, active_cases = \
            0,0,0,0
        while next < len(stats):
            if get_next:
                stat, next = self._get_next_stat(stats, next)
                get_next = False
            if date == stat['date']:
                get_next = True
                total_cases += stat['total_confirmed']
                total_deaths += stat['total_deaths']
                total_recovered += stat['total_recovered']
                today_active_cases = stat['total_confirmed'] - (
                    stat['total_deaths'] + stat['total_recovered']
                )
                active_cases += today_active_cases
            report = self._convert_specific_day_cumulative_report_dto(
                date, total_cases, total_deaths,
                total_recovered, active_cases
            )
            date = self._next_day(date)
            specific_day_report.append(report)
        daily_cumulative_report_dto = \
            DailyCumulativeReport(report=specific_day_report)
        return daily_cumulative_report_dto

    def _convert_specific_day_cumulative_report_dto(self, date, total_cases,
            total_deaths, total_recovered_cases, active_cases):
        report = CumulativeReportOnSpecificDay(
            date=date,
            total_cases=total_cases,
            total_deaths=total_deaths,
            total_recovered_cases=total_recovered_cases,
            active_cases=active_cases
        )
        return report

    def get_district_daily_cumulative_report(self) -> List[DistrictStatDto]:
        stats = Stats.objects.values('mandal__district_id', 'date')\
                     .annotate(
                        district_id=F('mandal__district__id'),
                        name=F('mandal__district__name'),
                        total_cases=Sum('total_confirmed'),
                        total_deaths=Sum('total_deaths'),
                        total_recovered_cases=Sum('total_recovered'),
                        ).order_by('date')
        districts = list(District.objects.filter(state_id=state_id))
        districts_details = self._convert_to_district_details(districts)

        reports =  self._convert_to_district_daily_cumulative_report(stats)
        district_daily_cumulative_report_dict = {
            "state_name":state_name,
            "districts":districts_details,
            "reports":reports
        }
        return district_daily_cumulative_report_dict
    
    def _convert_to_district_details(self, districts):
        district_details = {}
        for district in districts:
            district_details[district.id]={
                "district_id":district.id,
                "district_name":district.name
            }
        return district_details

    def _convert_to_district_daily_cumulative_report(self, stats):
        districts = defaultdict(list)
        for stat in stats:
            statistics = defaultdict(int)
            if districts[stat['district_id']]:
                statistics = self._add_district_enties(stat, districts)
            else:
                statistics = self._initialize_entry(stat)
            districts[stat['district_id']].append(statistics)
        return districts

    def _add_district_enties(self, stat, districts):
        previous_report = self._get_previous_report(districts, stat['district_id'])
        return self._add_entries(stat, districts, previous_report)
    
    def _get_previous_report(self, reports, district_id):
        end = -1
        previous_cumulative_data = reports[district_id][end]
        return previous_cumulative_data

    def _initialize_entry(self, stat):
        statistics = defaultdict(int)
        total_cases, total_deaths, total_recovered = \
            self._get_stat_details(stat)
        statistics['date'] = stat['date']
        statistics['total_cases'] = total_cases
        statistics['total_deaths'] = total_deaths
        statistics['total_recovered_cases'] = total_recovered
        return statistics

    def _add_entries(self, stat, mandals, previous_report):
        total_cases, total_deaths, total_recovered = \
            self._get_stat_details(previous_report)

        statistics = defaultdict(int)
        statistics['date'] = stat['date']
        statistics['total_cases'] = \
            stat['total_cases'] + total_cases
        statistics['total_deaths'] = \
            stat['total_deaths'] + total_deaths
        statistics['total_recovered_cases'] = \
            stat['total_recovered_cases'] + total_recovered

        return statistics

    def get_report_of_state_for_date(self, date):
        state_id = 1
        stats = Mandal.objects.values('district_id').annotate(
            total_cases=Sum('stats__total_confirmed'),
            total_recovered_cases=Sum('stats__total_recovered'),
            total_deaths=Sum('stats__total_deaths'),
            district_name = F('district__name'),
            state_naem = F('district__state__name')
        ).filter(stats__date=date).order_by('district_id')
        districts = District.objects.filter(state_id=state_id)\
                            .order_by('id')
        return self._convert_to_state_report_of_a_date(stats, districts)

    def _convert_to_state_report_of_a_date(self, stats, districts):
        state_name="Andrapradesh"
        next = 0
        stat, next = self._get_next_stat(stats, next)
        reports = []
        total_cases, total_deaths, total_recovered_cases = 0, 0, 0
        for district in districts:
            today_cases, today_deaths, today_recovered_cases = 0, 0, 0
            if district.id == stat['district_id']:
                today_cases, today_deaths, today_recovered_cases = \
                    self._get_stat_details(stat)
                next += 1
                stat, next = self._get_next_stat(stats, next)
            total_cases += today_cases
            total_deaths += today_deaths
            total_recovered_cases += today_recovered_cases
            reports.append(
                self._convert_to_report_of_district_for_state(
                    today_cases, today_deaths,
                    today_recovered_cases, district)
            )
            # print(reports)
        return StateReportForADate(
            state_name=state_name,
            districts=reports,
            total_cases=total_cases,
            total_deaths=total_deaths,
            total_recovered_cases=total_recovered_cases
        )

    def _get_stat_details(self, stat):
        today_cases = stat['total_cases']
        today_deaths= stat['total_deaths']
        today_recovered_cases = stat['total_recovered_cases']
        return today_cases, today_deaths, today_recovered_cases

    def _convert_to_report_of_district_for_state(self,
            today_cases, today_deaths, today_recovered_cases, district):
        district_report = DistrictReportForADate(
            district_id=district.id,
            district_name=district.name,
            total_cases=today_cases,
            total_deaths=today_deaths,
            total_recovered_cases=today_recovered_cases
        )
        return district_report


    def get_state_wise_daily_cases_report(self) -> StateDailyReport:
        stats = Mandal.objects.values('district__state_id', 'stats__date').annotate(
            total_cases=Sum('stats__total_confirmed'),
            total_recovered_cases=Sum('stats__total_recovered'),
            total_deaths=Sum('stats__total_deaths'),
            date=F('stats__date')
            ).order_by('date').exclude(date=None)
        state_report = self._convert_to_daily_cases_report(stats)
        return state_report

    def _convert_to_daily_cases_report(self, stats):
        index = 0
        date = stats[index]['date']
        stat, index = self._get_next_stat(stats, index)
        reports = []
        while stat:
            total_cases, total_deaths, total_recovered_cases = 0, 0, 0
            if date == stat['date']:
                total_cases, total_deaths, total_recovered_cases = \
                    self._get_stat_details(stat)
                if index >= len(stats):
                    break
                stat, index = self._get_next_stat(stats, index)

            reports.append(
                Report(
                    date=date,
                    total_cases=total_cases,
                    total_recovered_cases=total_recovered_cases,
                    total_deaths=total_deaths,
                    active_cases=total_cases - \
                        (total_deaths + total_recovered_cases)
                )
            )
            date = self._next_day(date)
        return reports
