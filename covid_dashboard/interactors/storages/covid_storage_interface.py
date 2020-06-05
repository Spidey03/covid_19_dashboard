# from abc import ABC
# from abc import abstractmethod
# from covid_dashboard.models\
#     import State, District, Mandal, Stats
# from covid_dashboard.interactors.storages.dtos\
#     import (DailyCumulativeReport, CumulativeReportOnSpecificDay,
#             StateDto, DistrictStatDto, DistrictDto)
# from covid_dashboard.exceptions.exceptions\
#     import InvalidStateId, InvalidDistrictId


# class CovidStorageInterface(ABC):

#     # # Done
#     # @abstractmethod
#     # def is_state_id_valid(self, state_id: int):
#     #     pass


#     @abstractmethod
#     def is_district_id_valid(self, district_id: int):
#         pass

#     # # Done
#     # @abstractmethod
#     # def get_state_wise_daily_report(self) -> StateDto:
#     #     pass

#     # # Done
#     # @abstractmethod
#     # def get_state_wise_cumulative_report(self) -> StateDto:
#     #     pass

#     # # Done
#     # @abstractmethod
#     # def get_daily_cumulative_report(self) -> DailyCumulativeReport:
#     #     pass

#     # # Done
#     # @abstractmethod
#     # def get_district_daily_cumulative_report(self):
#     #     pass

#     # @abstractmethod
#     # def is_valid_total_confirmed(self, total_confirmed: int):
#     #     pass

#     # @abstractmethod
#     # def is_valid_total_deaths(self, total_deaths: int):
#     #     pass

#     # @abstractmethod
#     # def is_valid_total_recovered(self, total_recovered: int):
#     #     pass

#     # @abstractmethod
#     # def is_valid_mandal_id(self, mandal_id: int):
#     #     pass

#     # @abstractmethod
#     # def add_new_statistics(self, mandal_id: int, total_confirmed: int,
#     #         date, total_deaths: int, total_recovered: int):
#     #     pass

#     # @abstractmethod
#     # def update_statistics(self, mandal_id: int, total_confirmed: int,
#     #         date, total_deaths: int, total_recovered: int):
#     #     pass

#     # @abstractmethod
#     # def is_statistics_valid(self, total_confirmed: int, 
#     #         total_deaths: int, total_recovered: int):
#     #     pass

#     # @abstractmethod
#     # def is_already_exist(self, mandal_id: int, date: int):
#     #     pass
#     # # @abstractmethod
#     # def is_valid_date(self, date):
#     #     pass

#     # @abstractmethod
#     # def get_report_of_state_for_date(self, date):
#     #     pass

#     @abstractmethod
#     def check_is_date_valid(self, date):
#         pass

#     # @abstractmethod
#     # def get_state_wise_daily_cases_report(self):
#     #     pass

#     @abstractmethod
#     def get_district_cumulative_report(self, till_date, district_id):
#         pass


#     @abstractmethod
#     def get_daily_cumulative_report_for_district(self):
#         pass
    
    
#     @abstractmethod
#     def get_daily_cumulative_report_of_mandals_for_district(self,
#             district_id: int):
#         pass


#     @abstractmethod
#     def get_district_report_of_specific_day(
#             self, date, district_id):
#         pass

