from abc import ABC
from abc import abstractmethod
from covid_dashboard.interactors.storages.dtos import *

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_user_name(self):
        pass

    @abstractmethod
    def raise_invalid_password(self):
        pass

    @abstractmethod
    def login_response(self, user_token_dto):
        pass

    @abstractmethod
    def raise_invalid_state_id(self, state_id: int):
        pass

    @abstractmethod
    def raise_invalid_date_format(self):
        pass

    @abstractmethod
    def response_state_cumulative_report(self, 
            state_cumulative_report_dto: CompleteStateCumulativeReportDto):
        pass

    @abstractmethod
    def resonse_state_day_wise_report(self,
            day_wise_report_dtos: List[DayWiseReportDto]):
        pass

    @abstractmethod
    def response_day_wise_report_with_districts(self, 
            all_district_reports: List[DistrictDayWiseReportDto]):
        pass