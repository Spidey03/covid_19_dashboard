from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from covid_dashboard.interactors.storages.dtos\
    import (DailyCumulativeReport, CumulativeReportOnSpecificDay,
            StateDto, DistrictStatDto, DistrictDto)



class PresenterInterface(ABC):

    @abstractmethod
    def get_response_login_user(self, tokens_dto: UserAuthTokensDTO):
        pass


    @abstractmethod
    def get_response_for_state_wise_daily_report(
            self, daily_state_report_dto: StateDto):
        pass


    @abstractmethod
    def get_response_for_state_wise_cumulative_report(
            self, daily_state_report_dto: DistrictDto):
        pass



    @abstractmethod
    def get_daily_cumulative_report_response(self,
            daily_cumulative_report_dto: DailyCumulativeReport):
        pass

    @abstractmethod
    def raiseinvalidusername(self):
        pass

    @abstractmethod
    def raiseinvalidpassword(self):
        pass


    @abstractmethod
    def get_district_daily_cumulative_report_response(self,
            list_district_daily_cumulative):
        pass



    @abstractmethod
    def raise_invalid_details_for_total_confirmed(self):
        pass


    @abstractmethod
    def raise_invalid_details_for_total_deaths(self):
        pass


    @abstractmethod
    def raise_invalid_details_for_total_recovered(self):
        pass

    @abstractmethod
    def raise_invalid_details_for_mandal_id(self):
        pass
    
    
    @abstractmethod
    def raise_invalid_stats_details(self):
        pass


    # @abstractmethod
    # def raise_invalid_details_for_date(self):
    #     pass
    
    @abstractmethod
    def raise_stat_not_found(self):
        pass

    @abstractmethod
    def raise_details_already_exist(self):
        pass


    @abstractmethod
    def get_response_for_report_of_state_for_date(self, report):
        pass


    @abstractmethod
    def raise_invalid_date(self):
        pass


    @abstractmethod
    def get_response_for_state_wise_daily_cases_report(self,
            daily_state_report_dto):
        pass


    @abstractmethod
    def get_response_for_district_cumulative_report(self, report):
        pass

    
    @abstractmethod
    def get_response_for_daily_cumulative_report_for_district(self, report):
        pass


    @abstractmethod
    def raise_invalid_district_id(self):
        pass


    @abstractmethod
    def get_response_for_daily_cumulative_report_of_mandals_for_district(self,
            district_report):
        pass

    @abstractmethod
    def get_response_district_report_of_specific_day(self, report):
        pass

    @abstractmethod
    def get_response_for_get_statistics(self, report):
        pass
    
    @abstractmethod
    def get_response_get_day_wise_district_details(self, district_report_list):
        pass

    @abstractmethod
    def get_response_get_day_wise_mandal_details(self, district_report_dict):
        pass