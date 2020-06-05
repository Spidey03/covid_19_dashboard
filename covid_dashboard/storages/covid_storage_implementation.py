# import datetime
# from abc import ABC
# from abc import abstractmethod
# from typing import List
# from collections import defaultdict
# from django.db.models import Sum, F, Prefetch
# from covid_dashboard.models\
#     import State, District, Mandal, Stats
# from covid_dashboard.interactors.storages.covid_storage_interface\
#     import CovidStorageInterface
# from covid_dashboard.interactors.storages.dtos\
#     import (DailyCumulativeReport, CumulativeReportOnSpecificDay,
#             StateDto, DistrictStatDto, DistrictDto,
#             DailyCumulativeDistrictWise, DistrictDetails,
#             DistrictReportForADate, StateReportForADate, Report,
#             StateDailyReport, DistrictReportDto, MandalReportDto,
#             DailyCumulativeMandalWiseReportDto, DistrictReportOfDay,
#             MandalReportOfDay, Statistics, MandalStatistics)
# from covid_dashboard.exceptions.exceptions\
#     import (InvalidStateId, InvalidDistrictId,
#             InvalidDetailsForTotalConfirmed,
#             InvalidDetailsForTotalDeaths,
#             InvalidDetailsForTotalRecovered,
#             InvalidMandalId, InvalidStatsDetails, StatNotFound,
#             DetailsAlreadyExist, InvalidDate)

# class CovidStorageImplementation(CovidStorageInterface):

#     # # State
#     # def is_state_id_valid(self, state_id: int):
#     #     try:
#     #         State.objects.get(id=state_id)
#     #     except State.DoesNotExist:
#     #         raise InvalidStateId


#     def is_district_id_valid(self, district_id: int):
#         try:
#             District.objects.get(id=district_id)
#         except District.DoesNotExist:
#             raise InvalidDistrictId


#     # # State
#     # def get_state_wise_daily_report(self, state_id: int) -> StateDto:
#     #     pass


#     # # State
#     # def get_state_wise_cumulative_report(
#     #         self, till_date) -> StateDto:
                
#     #     state_id, state_name = 1, 'Andhrapradesh'
#     #     queryset2 = F('stats__total_cases')-\
#     #         (F('stats__total_deaths')+F('stats__total_recovered'))
#     #     districts= list(District.objects.values_list('id', flat=True)\
#     #                             .filter(state_id=state_id)
#     #                   )
    
#     #     districts_cumulative_report = \
#     #         Mandal.objects.values('district_id')\
#     #                       .filter(stats__date__lte=till_date)\
#     #                       .annotate(
#     #                           total_cases=Sum('stats__total_confirmed'),
#     #                           total_deaths=Sum('stats__total_deaths'),
#     #                           total_recovered=Sum('stats__total_recovered'),
#     #                           district_name=F('district__name')
#     #                       )\
#     #                       .filter(district_id__in=districts).order_by('district_id')
        
#     #     districts_cumulative_report_list = list(districts_cumulative_report)

#     #                         #   date=F('stats__date')
#     #     state_cumulative_report_dto = \
#     #         self._convert_to_state_cumulative_report_dto(
#     #             districts_cumulative_report_list, till_date,
#     #             state_id, state_name)
#     #     return state_cumulative_report_dto

    
#     def _convert_to_state_cumulative_report_dto(self,
#             districts_cumulative_report_list, till_date,
#             state_id, state_name):
#         districts = District.objects.values('id','name').order_by('id')
#         list_district_dtos = []
        
#         next = 0
#         district_report = self._get_next_district_report(
#             districts_cumulative_report_list, next)
#         next += 1
#         for district in districts:
#             if district['id'] == district_report['district_id']:
#                 district_dto = self._convert_to_district_cumulative_report_dto(
#                     district_report, till_date
#                 )
#                 district_report = self._get_next_district_report(
#                     districts_cumulative_report_list, next)
#                 next += 1
#             else:
#                 district_dto = self._convert_to_district_dto_with_zeroes(district, till_date)
#             list_district_dtos.append(district_dto)

#         state_cumulative_report_dto = StateDto(
#                 state_id=state_id,
#                 state_name=state_name,
#                 stats=list_district_dtos
#             )
#         return state_cumulative_report_dto

#     def _get_next_district_report(self, district_reports, next):
#         if district_reports and next < len(district_reports):
#             district_report = district_reports[next]
#         else:
#             district_report = {
#                 'district_id':None
#             }
#         return district_report

#     def _convert_to_district_dto_with_zeroes(self, district, till_date):
#         district_dto = DistrictStatDto(
#                 district_id=district['id'],
#                 district_name=district['name'],
#                 date=till_date,
#                 total_cases=0,
# 	            total_deaths=0,
# 	            total_recovered_cases=0,
# 	            active_cases=0
#             )
#         return district_dto

#     def _convert_to_district_cumulative_report_dto(self,
#             district_report, till_date):
#         district_dto = DistrictStatDto(
#                 district_id=district_report['district_id'],
#                 district_name=district_report['district_name'],
#                 date=till_date,
#                 total_cases=district_report['total_cases'],
# 	            total_deaths=district_report['total_deaths'],
# 	            total_recovered_cases=district_report['total_recovered'],
# 	            active_cases=district_report['total_cases'] - \
# 	                (district_report['total_deaths'] + district_report['total_recovered'])
#             )
#         return district_dto



#     # def get_daily_cumulative_report(self) -> DailyCumulativeReport:

#     #     specific_day_report = []
#     #     state_id, state_name = 1, 'Andhrapradesh'
#     #     stats = Stats.objects.values('date', 'mandal__district__state_id').annotate(
            
#     #         total_confirmed=Sum('total_confirmed'),
#     #         total_deaths=Sum('total_deaths'),
#     #         total_recovered=Sum('total_recovered')
#     #     ).filter(mandal__district__state_id=state_id).order_by('date')
    
#     #     daily_cumulative_report_dto = \
#     #         self._convert_to_daily_cumulative_report_dto(stats)
#     #     return daily_cumulative_report_dto

#     def _convert_to_daily_cumulative_report_dto(self, stats):
#         import datetime
#         specific_day_report = []
#         first, next = 0, 0
#         date = stats[first]['date']
#         get_next = True
#         timedelata = datetime.timedelta(days=1)
#         total_cases, total_deaths, total_recovered, active_cases = \
#             0,0,0,0
#         while next < len(stats):
#             if get_next and next < len(stats):
#                 stat = stats[next]
#                 next += 1
#                 get_next = False
        
#             if date == stat['date']:
#                 get_next = True
#                 total_cases += stat['total_confirmed']
#                 total_deaths += stat['total_deaths']
#                 total_recovered += stat['total_recovered']
#                 today_active_cases = stat['total_confirmed'] - (
#                     stat['total_deaths'] + stat['total_recovered']
#                 )
#                 active_cases += today_active_cases
    
#             report = self._covert_specific_day_cumulative_report_dto(
#                 date, total_cases, total_deaths, total_recovered, active_cases)
#             date = date + timedelata
#             specific_day_report.append(report)
        
#         daily_cumulative_report_dto = \
#             DailyCumulativeReport(report=specific_day_report)
#         return daily_cumulative_report_dto

#     def _covert_specific_day_cumulative_report_dto(self, date, total_cases,
#             total_deaths, total_recovered_cases, active_cases):
#         report = CumulativeReportOnSpecificDay(
#             date=date,
#             total_cases=total_cases,
#             total_deaths=total_deaths,
#             total_recovered_cases=total_recovered_cases,
#             active_cases=active_cases
#         )
#         return report


#     # def get_district_daily_cumulative_report(self) -> List[DistrictStatDto]:
#     #     state_id, state_name = 1, 'Andhrapradesh'
#     #     stats = Stats.objects.values('mandal__district_id', 'date')\
#     #                  .annotate(
#     #                     district_id=F('mandal__district__id'),
#     #                     name=F('mandal__district__name'),
#     #                     total_confirmed=Sum('total_confirmed'),
#     #                     total_deaths=Sum('total_deaths'),
#     #                     total_recovered=Sum('total_recovered'),
#     #                     ).order_by('date')
#     #     districts = list(District.objects.filter(state_id=state_id))
#     #     districts_details = self._convert_to_district_details(districts)

#     #     reports =  self._convert_to_list_district_daily_cumulative_report(
#     #         stats)
#     #     district_wise_daily_cumulative_report_dict = {
#     #         "state_name":state_name,
#     #         "districts":districts_details,
#     #         "reports":reports
#     #     }
#     #     return district_wise_daily_cumulative_report_dict

#     def _convert_to_list_district_daily_cumulative_report(self, stats):
#         districts = defaultdict(list)
#         for stat in stats:
#             district_statistics = defaultdict(int)
#             if not districts[stat['district_id']]:
#                 district_statistics = self._initialize_entry(stat)
#             else:
#                 district_statistics = self._add_district_enties(
#                     stat, districts)
#             districts[stat['district_id']].append(district_statistics)
            
#         return districts

#     def _get_previous_report_for_district(self, districts, stat):
#         end = -1
#         previous_cumulative_data = districts[stat['district_id']][end]
#         return previous_cumulative_data
    
#     def _add_district_enties(self, stat, districts):
#         previous_report = \
#             self._get_previous_report_for_district(districts, stat)
#         return self._add_entries(stat, districts, previous_report)

#     def _convert_to_district_details(self, districts):
#         district_details = {}
#         for district in districts:
            
#             district_details[district.id]={
#                 "district_id":district.id,
#                 "district_name":district.name
#             }
#         return district_details


#     # def get_report_of_state_for_date(self, date):
#     #     state_id = 1
#     #     stats = Mandal.objects.values('district_id').annotate(
#     #         total_cases=Sum('stats__total_confirmed'),
#     #         total_recovered_cases=Sum('stats__total_recovered'),
#     #         total_deaths=Sum('stats__total_deaths'),
#     #         district_name = F('district__name'),
#     #         state_naem = F('district__state__name')
#     #     ).filter(stats__date=date).order_by('district_id')
#     #     districts = District.objects.filter(state_id=state_id)\
#     #                         .order_by('id')
#     #     return self._convert_to_state_report_of_a_date(stats, districts)

#     def _convert_to_state_report_of_a_date(self, stats, districts):
#         state_name="Andrapradesh"
#         next = 0
#         stat = self._get_next_stat(stats, next)
#         reports = []
#         total_cases, total_deaths, total_recovered_cases = 0, 0, 0
#         for district in districts:
#             today_cases, today_deaths, today_recovered_cases = 0, 0, 0
#             if district.id == stat['district_id']:
#                 today_cases, today_deaths, today_recovered_cases = \
#                     self._get_stat_details(stat)
#                 next += 1
#                 stat = self._get_next_stat(stats, next)
#             total_cases += today_cases
#             total_deaths += today_deaths
#             total_recovered_cases += today_recovered_cases
#             reports.append(
#                 self._convert_to_report_of_district_for_state(
#                     today_cases, today_deaths,
#                     today_recovered_cases, district)
#             )
#             # print(reports)
#         return StateReportForADate(
#             state_name=state_name,
#             districts=reports,
#             total_cases=total_cases,
#             total_deaths=total_deaths,
#             total_recovered_cases=total_recovered_cases
#         )

#     def _get_next_stat(self, stats, next):
#         if next < len(stats):
#             return stats[next]
#         stat = {'district_id':None}
#         return stat

#     def _get_stat_details(self, stat):
#         today_cases = stat['total_cases']
#         today_deaths= stat['total_deaths']
#         today_recovered_cases = stat['total_recovered_cases']
#         return today_cases, today_deaths, today_recovered_cases

#     def _convert_to_report_of_district_for_state(self,
#             today_cases, today_deaths, today_recovered_cases, district):
#         district_report = DistrictReportForADate(
#             district_id=district.id,
#             district_name=district.name,
#             total_cases=today_cases,
#             total_deaths=today_deaths,
#             total_recovered_cases=today_recovered_cases
#         )
#         return district_report


#     def check_is_date_valid(self, date):
#         import datetime
#         today = datetime.date.today()
#         if date > today:
#             raise InvalidDate

#     # def get_state_wise_daily_cases_report(self) -> StateDailyReport:
#     #     stats = Mandal.objects.values('district__state_id', 'stats__date').annotate(
#     #         total_cases=Sum('stats__total_confirmed'),
#     #         total_recovered_cases=Sum('stats__total_recovered'),
#     #         total_deaths=Sum('stats__total_deaths'),
#     #         date=F('stats__date')
#     #         ).order_by('date').exclude(date=None)
#     #     state_report = self._convert_to_daily_cases_report(stats)
#     #     return state_report

#     def _convert_to_daily_cases_report(self, stats):
#         first, next = 0, 0
#         date = stats[first]['date']
#         timedelta = datetime.timedelta(days=1)
#         stat = stats[next]
#         next += 1
#         reports = []
#         while stat:
#             total_cases, total_deaths, total_recovered_cases = 0, 0, 0
#             if date == stat['date']:
#                 total_cases, total_deaths, total_recovered_cases = \
#                     stat['total_cases'], stat['total_deaths'],\
#                         stat['total_recovered_cases']
#                 if next >= len(stats):
#                     break
#                 stat = stats[next]
#                 next += 1

#             reports.append(
#                 Report(
#                     date=date,
#                     total_cases=total_cases,
#                     total_recovered_cases=total_recovered_cases,
#                     total_deaths=total_deaths,
#                     active_cases=total_cases - \
#                         (total_deaths + total_recovered_cases)
#                 )
#             )
#             date = date + timedelta
#         return reports


#     def get_district_cumulative_report(self, till_date, district_id):
#         district = District.objects.get(id=district_id)
#         stats = Stats.objects.values('mandal_id').annotate(
#                     mandal_name=F('mandal__name'),
#                     total_deaths=Sum('total_deaths'),
#                     total_cases=Sum('total_confirmed'),
#                     total_recovered_cases=Sum('total_recovered')
#                 ).filter(mandal__district_id=district_id)\
#                  .order_by('mandal_id')
    
#         return self._get_cumulative_report_for_district(stats, district)

#     def _get_cumulative_report_for_district(self, stats, district):
#         mandals = Mandal.objects.filter(district_id=district.id).order_by('id')
#         mandal_reports, total_cases, total_recovered_cases, total_deaths,\
#             total_active_cases = \
#                 self._get_mandal_cumulative_report_for_district(stats, mandals)
#         district_report = DistrictReportDto(
#             district_name=district.name,
#             mandals=mandal_reports,
#             total_cases=total_cases,
#             total_deaths=total_deaths,
#             total_recovered_cases=total_recovered_cases,
#             active_cases=total_active_cases
#         )
#         return district_report

#     def _get_mandal_cumulative_report_for_district(self, stats, mandals):
#         next = 0
#         stat = stats[next]
#         next += 1
#         reports = []
#         total_cases, total_deaths, total_recovered_cases, total_active_cases =\
#             0, 0, 0, 0
#         for mandal in mandals:
#             today_cases, today_deaths, today_recovered_cases = 0, 0, 0
#             if mandal.id == stat['mandal_id']:
#                 today_cases, today_deaths, today_recovered_cases = \
#                     self._get_stat_details(stat)
#                 if next < len(stats):
#                     stat = stats[next]
#                     next += 1
        
#             active_cases = today_cases - (today_deaths + today_recovered_cases)
#             total_cases += today_cases
#             total_recovered_cases += today_recovered_cases
#             total_deaths += today_deaths
#             total_active_cases += active_cases
            
#             reports.append(self._convert_to_mandal_report_dto(
#                 mandal.id, mandal.name,
#                 today_cases, today_deaths,
#                 today_recovered_cases, active_cases)
#             )
#         return reports, total_cases, total_recovered_cases,\
#             total_deaths, total_active_cases

#     def _convert_to_mandal_report_dto(
#             self, mandal_id, name, today_cases, today_deaths,
#             today_recovered_cases, active_cases):
#         return MandalReportDto(
#                 mandal_id=mandal_id,
#                 mandal_name=name,
#                 total_cases=today_cases,
#                 total_deaths=today_deaths,
#                 total_recovered_cases=today_recovered_cases,
#                 active_cases=active_cases
#             )


#     def get_daily_cumulative_report_for_district(self, district_id):
#         stats = Stats.objects.values('date')\
#                      .filter(mandal__district_id=district_id)\
#                      .annotate(
#                             total_cases=Sum('total_confirmed'),
#                             total_deaths=Sum('total_deaths'),
#                             total_recovered_cases=Sum('total_recovered')
#                             )
#         report = self._convert_to_daily_cumulative_report_dto_for_district(stats)
#         return DailyCumulativeReport(
#             report = report
#         )

#     def _convert_to_daily_cumulative_report_dto_for_district(self, stats):
#         next = 0
#         stat = stats[next]
#         next += 1
#         date = stat['date']
#         get_next = False
#         timedelta = datetime.timedelta(days=1)
#         cumulative_reports = []
#         total_cases, total_deaths, total_recovered_cases, active_cases = \
#             0, 0, 0, 0
#         while stat:
#             today_cases, today_deaths, today_recovered_cases = 0, 0, 0
#             if date == stat['date']:
#                 today_cases, today_deaths, today_recovered_cases = \
#                     stat['total_cases'], stat['total_deaths'],\
#                         stat['total_recovered_cases']
#                 get_next = True

#             today_active_cases = today_cases - \
#                 (today_deaths + today_recovered_cases)
#             total_cases += today_cases
#             total_deaths += today_deaths
#             total_recovered_cases += today_recovered_cases
#             active_cases += today_active_cases 
#             cumulative_reports.append(
#                 CumulativeReportOnSpecificDay(
#                     date=date,
#                     total_cases=total_cases,
#                     total_deaths=total_deaths,
#                     total_recovered_cases=total_recovered_cases,
#                     active_cases=active_cases
#                 )
#             )
#             if get_next:
#                 if next < len(stats):
#                     stat = stats[next]
#                     next += 1
#                 else:
#                     break
#                 get_next = False
#             date = date + timedelta
#         return cumulative_reports


#     def get_daily_cumulative_report_of_mandals_for_district(self,
#             district_id: int):
#         district = District.objects.get(id=district_id)
#         stats = Stats.objects.values('mandal_id', 'date')\
#                     .annotate(
#                         total_confirmed=Sum('total_confirmed'),
#                         total_recovered=Sum('total_recovered'),
#                         total_deaths=Sum('total_deaths')
#                     ).filter(mandal__district_id=district_id)\
#                      .order_by('mandal_id', 'date')


#         mandals = list(Mandal.objects.filter(district_id=district_id))
#         mandal_details = self._convert_to_mandal_details(mandals)

#         reports =  self._convert_to_list_mandal_daily_cumulative_report(
#             stats)
#         mandal_wise_daily_cumulative_report_dict= {
#             "district_name":district.name,
#             "mandals":mandal_details,
#             "reports":reports
#         }
#         return mandal_wise_daily_cumulative_report_dict

#     def _convert_to_list_mandal_daily_cumulative_report(self, stats):
#         mandals = defaultdict(list)
#         for stat in stats:
#             mandal_statistics = defaultdict(int)
#             if not mandals[stat['mandal_id']]:
#                 mandal_statistics = self._initialize_entry(stat)
#             else:
#                 mandal_statistics = self._add_mandal_entries(
#                     stat, mandals)
#             mandals[stat['mandal_id']].append(mandal_statistics)
            
#         return mandals

#     def _get_previous_report_for_mandal(self, mandals, stat):
#         end = -1
#         previous_cumulative_data = mandals[stat['mandal_id']][end]
#         return previous_cumulative_data
        
#     def _initialize_entry(self, stat):
#         statistics = defaultdict(int)
#         total_cases = stat['total_confirmed']
#         total_deaths = stat['total_deaths']
#         total_recovered = stat['total_recovered']
#         statistics['date'] = stat['date']
#         statistics['total_cases'] = total_cases
#         statistics['total_deaths'] = total_deaths
#         statistics['total_recovered_cases'] = total_recovered
#         # statistics['active_cases'] = \
#         # total_cases - (total_deaths + total_recovered)
#         return statistics

#     def _add_mandal_entries(self, stat, mandals):
#         previous_report = \
#             self._get_previous_report_for_mandal(mandals, stat)
#         return self._add_entries(stat, mandals, previous_report)

#     def _add_entries(self, stat, mandals, previous_report):
#         total_cases = previous_report['total_cases']
#         total_deaths = previous_report['total_deaths']
#         total_recovered = \
#             previous_report['total_recovered_cases']
#         # active_cases = previous_report['active_cases']

#         statistics = defaultdict(int)
#         statistics['date'] = stat['date']
#         statistics['total_cases'] = \
#             stat['total_confirmed'] + total_cases
#         statistics['total_deaths'] = \
#             stat['total_deaths'] + total_deaths
#         statistics['total_recovered_cases'] = \
#             stat['total_recovered'] + total_recovered
#         return statistics

#     def _convert_to_mandal_details(self, mandals):
#         mandal_details = {}
#         for mandal in mandals:
            
#             mandal_details[mandal.id]={
#                 "mandal_id":mandal.id,
#                 "mandal_name":mandal.name
#             }
#         return mandal_details


#     def get_district_report_of_specific_day(
#             self, date, district_id):
#         stats = Stats.objects.values('mandal_id')\
#                       .annotate(
#                           name=F('mandal__name'),
#                           total_cases=F('total_confirmed'),
#                           total_recovered_cases=F('total_recovered'),
#                           total_deaths=F('total_deaths')
#                       )\
#                       .filter(mandal__district_id=district_id,
#                         date=date).order_by('mandal_id')
#         district = District.objects.prefetch_related('mandal_set').get(id=district_id)
#         return self._convert_to_district_report_of_day(stats, district)


#     def _convert_to_district_report_of_day(self, stats, district):
#         mandals = district.mandal_set.all().order_by('id')
#         reports, total_cases, total_deaths, total_recovered_cases = \
#             self._get_mandal_reports_of_day(stats, mandals)
#         district_report = DistrictReportOfDay(
#             district_name=district.name,
#             mandals=reports,
#             total_cases=total_cases,
#             total_deaths=total_deaths,
#             total_recovered_cases=total_recovered_cases
#         )
#         return district_report

#     def _get_mandal_reports_of_day(self, stats, mandals):
#         next = 0
#         reports = []
#         stat, next = self._get_next_stat_for_mandal(stats, next)
#         get_next = False
#         next += 1
#         total_cases, total_deaths, total_recovered_cases = \
#             0, 0, 0
#         print(mandals)
#         for mandal in mandals:
#             today_cases, today_deaths, today_recovered = 0, 0, 0
#             if mandal.id == stat['mandal_id']:
#                 today_cases, today_deaths, today_recovered = \
#                     stat['total_cases'], stat['total_deaths'], \
#                         stat['total_recovered_cases']
#                 get_next = True
        
#             total_cases += today_cases
#             total_recovered_cases += today_recovered
#             total_deaths += today_deaths
#             reports.append(
#                 MandalReportOfDay(
#                     mandal_id=mandal.id,
#                     mandal_name=mandal.name,
#                     total_cases=today_cases,
#                     total_deaths=today_deaths,
#                     total_recovered_cases=today_recovered
#                 )
#             )
#             if get_next:
#                 stat, next = self._get_next_stat_for_mandal(stats, next)
#         return reports, total_cases, total_deaths,\
#             total_recovered_cases

#     def _get_next_stat_for_mandal(self, stats, next):
#         if next < len(stats) and stats:
#             return stats[next], next+1
#         return {'mandal_id':None}, next+1

    
        