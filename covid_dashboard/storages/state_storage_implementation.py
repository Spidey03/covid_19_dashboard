import datetime
from abc import ABC
from typing import List
from abc import abstractmethod
from django.db.models import Sum, F, Prefetch, Max, Min
from covid_dashboard.models import State, District, Mandal, Stats
from covid_dashboard.interactors.storages.state_storage_interface \
    import StateStorageInterface
from covid_dashboard.exceptions.exceptions import InvalidStateId
from covid_dashboard.interactors.storages.dtos \
    import StateDto, DistrictDto, DistrictReportDto, DayReportDto, \
        DistrictDayReportDto

class StateStorageImplementation(StateStorageInterface):

    def _extract_report(self, report) -> tuple:

        total_confirmed = report['total_confirmed']
        total_deaths = report['total_deaths']
        total_recovered = report['total_recovered']
        return total_confirmed, total_recovered, total_deaths

    def _get_next_report(self, report_query_set, index: int):
        if index < len(report_query_set):
            return report_query_set[index], index+1
        return {'district_id':None}, index+1

    def check_state_id_is_valid(self, state_id):
        is_state_id_valid = State.objects.filter(id=state_id).exists()
        is_not_state_id_valid = not is_state_id_valid
        if is_not_state_id_valid:
            raise InvalidStateId

    def get_initial_and_final_dates(self):
        dates = Stats.objects.aggregate(initial_date=Min('date'),
            final_date=Max('date'))
        return dates['initial_date'], dates['final_date']


    def get_state_details(self, state_id: int) -> StateDto:
        try:
            state = State.objects.get(id=state_id)
        except State.DoesNotExist:
            raise InvalidStateId

        state_dto = StateDto(
                state_id=state.id,
                state_name=state.name
            )
        return state_dto

    def get_districts_for_state(self, state_id: int) -> List[DistrictDto]:
        districts = District.objects.filter(state_id=state_id)
        district_dtos = []
        for district in districts:
            district_dtos.append(
                DistrictDto(
                    district_id=district.id,
                    district_name=district.name
                )
            )
        return district_dtos

    def get_cumulative_report_for_districts(self, district_ids: List[int],
            till_date: datetime.date) -> List[DistrictReportDto]:

        report_query_set = \
            Mandal.objects.values('district_id')\
                  .filter(district_id__in=district_ids,
                      stats__date__lte=till_date)\
                  .annotate(
                        total_confirmed=Sum('stats__total_confirmed'),
                        total_recovered=Sum('stats__total_recovered'),
                        total_deaths=Sum('stats__total_deaths')
                    ).order_by('district_id')
        print(report_query_set)
        return self._convert_to_district_report_dto(
            report_query_set=report_query_set, district_ids=district_ids)

    def _convert_to_district_report_dto(self, report_query_set,
            district_ids: List[int]):
        district_report_dto_list = []
        index = 0
        report, index = self._get_next_report(report_query_set, index)
        for district_id in district_ids:
            total_confirmed, total_recovered, total_deaths = 0, 0, 0
            if district_id == report['district_id']:
                total_confirmed, total_recovered, total_deaths = \
                    self._extract_report(report)
                report, index = self._get_next_report(report_query_set, index)
            district_report_dto = DistrictReportDto(
                district_id=district_id,
                total_confirmed=total_confirmed,
                total_recovered=total_recovered,
                total_deaths=total_deaths
            )
            district_report_dto_list.append(district_report_dto)
        return district_report_dto_list

    def state_get_day_wise_report(self, state_id: int) -> List[DayReportDto]:

        report_query_set = Stats.objects.values(
                'mandal__district__state_id', 'date'
            ).annotate(
                total_confirmed=Sum('total_confirmed'),
                total_recovered=Sum('total_recovered'),
                total_deaths=Sum('total_deaths')
            ).order_by('date')

        return self._convert_to_daily_report_dto_list(report_query_set)

    def _convert_to_daily_report_dto_list(self, report_query_set):

        daily_report_dto_list = []
        for report in report_query_set:
            total_confirmed, total_recovered, total_deaths = \
                    self._extract_report(report)
            daily_report_dto_list.append(
                DayReportDto(
                    date=report['date'],
                    total_confirmed=total_confirmed,
                    total_recovered=total_recovered,
                    total_deaths=total_deaths
                )
            )
        return daily_report_dto_list

    def get_day_wise_report_for_distrcts(self,
            district_ids: List[int]) -> DistrictDayReportDto:

        print(district_ids)
        report_query_set = Stats.objects.values(
                'mandal__district_id', 'date'
            ).annotate(
                district_id = F('mandal__district_id'),
                total_confirmed=Sum('total_confirmed'),
                total_recovered=Sum('total_recovered'),
                total_deaths=Sum('total_deaths')
            ).filter(mandal__district_id__in=district_ids)\
             .order_by('district_id', 'date')
        # print(report_query_set)

        return self._convert_to_district_day_report_dtos(report_query_set)

    def _convert_to_district_day_report_dtos(self, report_query_set):

        district_day_report_dtos = []
        print(len(report_query_set))
        for report in report_query_set:
            print('-='*30)
            print(report)
            print('-='*30)
            district_day_report_dtos.append(
                DistrictDayReportDto(
                    date=report['date'],
                    district_id=report['district_id'],
                    total_confirmed=report['total_confirmed'],
                    total_recovered=report['total_recovered'],
                    total_deaths=report['total_deaths']
                )
            )
        return district_day_report_dtos

    def get_day_report_districts(self,
            district_ids: List[int], date) -> List[DistrictDayReportDto]:
        report_query_set = Stats.objects.values('mandal__district_id') \
                                .annotate(
                                    date = F('date'),
                                    district_id = F('mandal__district_id'),
                                    total_confirmed=Sum('total_confirmed'),
                                    total_recovered=Sum('total_recovered'),
                                    total_deaths=Sum('total_deaths')
                                ).filter(
                                    mandal__district_id__in=district_ids,
                                    date=date
                                ).order_by('mandal__district_id')
        print(report_query_set)
        return self._convert_to_district_day_report_dtos(report_query_set)
