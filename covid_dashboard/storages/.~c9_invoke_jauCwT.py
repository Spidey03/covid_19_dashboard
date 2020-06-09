import datetime
from abc import ABC
from typing import List
from abc import abstractmethod
from collections import defaultdict
from django.db.models import Sum, F, Prefetch
from covid_dashboard.exceptions.exceptions import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.models import State, District, Mandal, Stats
from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface

class DistrictStorageImplementation(DistrictStorageInterface):

    def is_district_id_valid(self, district_id: int):
        try:
            District.objects.get(id=district_id)
        except District.DoesNotExist:
            raise InvalidDistrictId

    def check_is_date_valid(self, date):
        import datetime
        today = datetime.date.today()
        if date > today:
            raise InvalidDate

    def _next_day(self, date):
        import datetime
        timedelata = datetime.timedelta(days=1)
        return date + timedelata

    def _get_initial_and_final_dates(self, stats):
        initial, final = 0, len(stats)-1
        initial_date = stats[initial]['date']
        final_date = stats[final]['date']
        return initial_date, final_date

    # return stat with None if stat doesnotexist
    def _get_next_stat(self, stats, index):
        if index < len(stats):
            stat = stats[index]
        else:
            stat = {'district_id':None, 'mandal_id':None}
        index += 1
        return stat, index

    def _get_previous_report(self, districts, stat):
        end = -1
        previous_cumulative_data = districts[stat['district_id']][end]
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

    def _get_stat_details(self, stat):
        today_cases = stat['total_cases']
        today_deaths= stat['total_deaths']
        today_recovered_cases = stat['total_recovered_cases']
        return today_cases, today_deaths, today_recovered_cases

    def get_district_cumulative_report(self, till_date, district_id):
        district = District.objects.get(id=district_id)
        stats = Stats.objects.values('mandal_id').annotate(
                    mandal_name=F('mandal__name'),
                    total_deaths=Sum('total_deaths'),
                    total_cases=Sum('total_confirmed'),
                    total_recovered_cases=Sum('total_recovered')
                ).filter(mandal__district_id=district_id, date__lte=till_date)\
                 .order_by('mandal_id')
    
        return self._get_cumulative_report_for_district(stats, district)

    def _get_cumulative_report_for_district(self, stats, district):
        mandals = Mandal.objects.filter(district_id=district.id).order_by('id')
        mandal_reports, total_cases, total_recovered_cases, total_deaths,\
            total_active_cases = \
                self._get_mandal_cumulative_report_for_district(stats, mandals)
        district_report = DistrictReportDto(
            district_name=district.name,
            mandals=mandal_reports,
            total_cases=total_cases,
            total_deaths=total_deaths,
            total_recovered_cases=total_recovered_cases,
            active_cases=total_active_cases
        )
        return district_report

    def _get_mandal_cumulative_report_for_district(self, stats, mandals):
        index = 0
        reports = []
        stat, index = self._get_next_stat(stats, index)
        total_cases, total_deaths, total_recovered_cases, total_active_cases =\
            0, 0, 0, 0
        for mandal in mandals:
            today_cases, today_deaths, today_recovered_cases = 0, 0, 0
            if mandal.id == stat['mandal_id']:
                today_cases, today_deaths, today_recovered_cases = \
                    self._get_stat_details(stat)
                stat, index = self._get_next_stat(stats, index)
        
            active_cases = today_cases - (today_deaths + today_recovered_cases)
            total_cases += today_cases
            total_recovered_cases += today_recovered_cases
            total_deaths += today_deaths
            total_active_cases += active_cases
            
            reports.append(self._convert_to_mandal_report_dto(
                mandal.id, mandal.name,
                today_cases, today_deaths,
                today_recovered_cases, active_cases)
            )
        return reports, total_cases, total_recovered_cases,\
            total_deaths, total_active_cases

    def _convert_to_mandal_report_dto(
            self, mandal_id, name, today_cases, today_deaths,
            today_recovered_cases, active_cases):
        return MandalReportDto(
                mandal_id=mandal_id,
                mandal_name=name,
                total_cases=today_cases,
                total_deaths=today_deaths,
                total_recovered_cases=today_recovered_cases,
                active_cases=active_cases
            )


    def get_daily_cumulative_report_for_district(self, district_id):
        stats = Stats.objects.values('date')\
                     .filter(mandal__district_id=district_id)\
                     .annotate(
                            total_cases=Sum('total_confirmed'),
                            total_deaths=Sum('total_deaths'),
                            total_recovered_cases=Sum('total_recovered')
                            )
        report = self._convert_to_daily_cumulative_report_dto_for_district(stats)
        return DailyCumulativeReport(
            report = report
        )

    def _convert_to_daily_cumulative_report_dto_for_district(self, stats):
        index = 0
        stat, index = self._get_next_stat(stats, index)
        date, final_date = self._get_initial_and_final_dates(stats)
        get_next = False
        cumulative_reports = []
        total_cases, total_deaths, total_recovered_cases, active_cases = \
            0, 0, 0, 0
        while date <= final_date:
            print(date)
            today_cases, today_deaths, today_recovered_cases = 0, 0, 0
            if date == stat['date']:
                today_cases, today_deaths, today_recovered_cases = \
                    self._get_stat_details(stat)
                get_next = True

            today_active_cases = today_cases - \
                (today_deaths + today_recovered_cases)
            total_cases += today_cases
            total_deaths += today_deaths
            total_recovered_cases += today_recovered_cases
            active_cases += today_active_cases 
            cumulative_reports.append(
                CumulativeReportOnSpecificDay(
                    date=date,
                    total_cases=total_cases,
                    total_deaths=total_deaths,
                    total_recovered_cases=total_recovered_cases,
                    active_cases=active_cases
                )
            )
            if get_next:
                if index < len(stats):
                    stat, next = self._get_next_stat(stats, index)
                else:
                    break
                get_next = False
            date = self._next_day(date)
        return cumulative_reports


    def get_daily_cumulative_report_of_mandals_for_district(self,
            district_id: int):
        district = District.objects.get(id=district_id)
        stats = Stats.objects.values('mandal_id', 'date')\
                    .annotate(
                        total_cases=Sum('total_confirmed'),
                        total_recovered_cases=Sum('total_recovered'),
                        total_deaths=Sum('total_deaths')
                    ).filter(mandal__district_id=district_id)\
                     .order_by('mandal_id', 'date')


        mandals = list(Mandal.objects.filter(district_id=district_id))
        mandal_details = self._convert_to_mandal_details(mandals)

        mandal_reports =  self._convert_to_list_mandal_daily_cumulative_report(
            stats)
        mandal_wise_daily_cumulative_report_dict= {
            "district_name":district.name,
            "mandals":mandal_details,
            "reports":mandal_reports
        }
        return mandal_wise_daily_cumulative_report_dict

    def _convert_to_list_mandal_daily_cumulative_report(self, stats):
        mandals_dict = defaultdict(list)
        for stat in stats:
            mandal_statistics = defaultdict(int)
            if not mandals_dict[stat['mandal_id']]:
                mandal_statistics = self._initialize_entry(stat)
            else:
                mandal_statistics = self._add_mandal_entries(
                    stat, mandals_dict)
            mandals_dict[stat['mandal_id']].append(mandal_statistics)
            
        return mandals_dict

    def _get_previous_report(self, reports, mandal_id):
        end = -1
        previous_cumulative_data = reports[mandal_id][end]
        return previous_cumulative_data

    def _add_mandal_entries(self, stat, mandals_dict):
        previous_report = \
            self._get_previous_report(mandals_dict, stat['mandal_id'])
        return self._add_entries(stat, mandals_dict, previous_report)

    def _convert_to_mandal_details(self, mandals):
        mandal_details = {}
        for mandal in mandals:
            
            mandal_details[mandal.id]={
                "mandal_id":mandal.id,
                "mandal_name":mandal.name
            }
        return mandal_details

    def get_district_report_of_specific_day(
            self, date, district_id):
        stats = Stats.objects.values('mandal_id')\
                      .annotate(
                          name=F('mandal__name'),
                          total_cases=F('total_confirmed'),
                          total_recovered_cases=F('total_recovered'),
                          total_deaths=F('total_deaths')
                       )\
                      .filter(mandal__district_id=district_id,
                        date=date).order_by('mandal_id')
        district = self._get_district_with_mandals(district_id=district_id)
        return self._convert_to_district_report_of_day(stats, district)

    def _get_district_with_mandals(self, district_id):
        district = District.objects.prefetch_related('mandal_set').get(id=district_id)
        return district

    def _convert_to_district_report_of_day(self, stats, district):
        mandals = district.mandal_set.all().order_by('id')
        reports, total_cases, total_deaths, total_recovered_cases = \
            self._get_mandal_reports_of_day(stats, mandals)
        district_report = DistrictReportOfDay(
            district_name=district.name,
            mandals=reports,
            total_cases=total_cases,
            total_deaths=total_deaths,
            total_recovered_cases=total_recovered_cases
        )
        return district_report

    def _get_mandal_reports_of_day(self, stats, mandals):
        index = 0
        reports = []
        total_cases, total_deaths, total_recovered_cases = 0, 0, 0
        if not stats:
            return reports, total_cases, total_deaths,\
                total_recovered_cases
        stat, index = self._get_next_stat_for_mandal(stats, index)
        print(mandals)
        for mandal in mandals:
            today_cases, today_deaths, today_recovered = 0, 0, 0
            if mandal.id == stat['mandal_id']:
                today_cases, today_deaths, today_recovered = \
                    self._get_stat_details(stat)
                stat, index = self._get_next_stat_for_mandal(stats, index)
        
            total_cases += today_cases
            total_recovered_cases += today_recovered
            total_deaths += today_deaths
            reports.append(
                MandalReportOfDay(
                    mandal_id=mandal.id,
                    mandal_name=mandal.name,
                    total_cases=today_cases,
                    total_deaths=today_deaths,
                    total_recovered_cases=today_recovered
                )
            )
        return reports, total_cases, total_deaths,\
            total_recovered_cases

    def _get_next_stat_for_mandal(self, stats, next):
        if next < len(stats) and stats:
            return stats[next], next+1
        return {'mandal_id':None}, next+1

    def get_day_wise_district_details(self, district_id):
        stats = Stats.objects.values('mandal__district_id', 'date', 'mandal__district__name')\
                     .annotate(
                        total_cases=Sum('total_confirmed'),
                        total_recovered_cases=Sum('total_recovered'),
                        total_deaths=Sum('total_deaths')
                    ).filter(mandal__district_id=district_id)\
                     .order_by('date')
        return self._conver_to_day_wise_district_details(stats)

    def _conver_to_day_wise_district_details(self, stats):
        index = 0
        district_reports_list = []
        if not stats:
            return district_reports_list
        date = stats[index]['date']
        stat, index = self._get_next_stat(stats, index)
        while index<len(stats):
            total_cases, total_deaths, total_recovered = 0, 0, 0
            if date == stat['date']:
                total_cases, total_deaths, total_recovered = \
                    self._get_stat_details(stat)
                stat, index = self._get_next_stat(stats, index)
            district_reports_list.append(
                Report(
                    date=date,
                    total_cases=total_cases,
                    total_recovered_cases=total_recovered,
                    total_deaths=total_deaths,
                    active_cases=total_cases - (total_deaths + total_recovered)
                )
            )
            date = self._next_day(date)
        return district_reports_list

    def get_day_wise_mandal_details(self, district_id):
        stats = Stats.objects.values('mandal_id', 'date')\
                      .annotate(
                          name=F('mandal__name'),
                          total_cases=F('total_confirmed'),
                          total_recovered_cases=F('total_recovered'),
                          total_deaths=F('total_deaths')
                       )\
                      .filter(mandal__district_id=district_id)\
                      .order_by('mandal_id', 'date')
        district = self._get_district_with_mandals(district_id=district_id)
        mandals = district.mandal_set.all()
        mandal_details = self._convert_to_mandal_details(mandals)
        mandal_reports =  self._convert_to_list_mandal_day_wise_report(
            stats)
        mandal_wise_daily_cumulative_report_dict= {
            "district_name":district.name,
            "mandals":mandal_details,
            "reports":mandal_reports
        }
        return mandal_wise_daily_cumulative_report_dict


    def _convert_to_list_mandal_day_wise_report(self, stats):
        mandals_dict = defaultdict(list)
        for stat in stats:
            mandal_statistics = defaultdict(int)
            if not mandals_dict[stat['mandal_id']]:
                mandal_statistics = self._initialize_entry(stat)
            else:
                mandal_statistics = self._add_day_wise_entries(stat)
            mandals_dict[stat['mandal_id']].append(mandal_statistics)
            
        return mandals_dict

    def _add_day_wise_entries(self, stat):
        total_cases, total_deaths, total_recovered = \
            self._get_stat_details(stat)

        statistics = defaultdict(int)
        statistics['date'] = stat['date']
        statistics['total_cases'] = total_cases
        statistics['total_deaths'] = total_deaths
        statistics['total_recovered_cases'] = total_recovered

        return statistics
