from abc import ABC
from abc import abstractmethod
from covid_dashboard.models\
    import State, District, Mandal, Stats
from covid_dashboard.interactors.storages.dtos\
    import (DailyCumulativeReport, CumulativeReportOnSpecificDay,
            StateDto, DistrictStatDto, DistrictDto)
from covid_dashboard.exceptions.exceptions\
    import InvalidStateId, InvalidDistrictId


class DistrictStorageInterface(ABC):

    @abstractmethod
    def is_district_id_valid(self, district_id: int):
        pass

    @abstractmethod
    def check_is_date_valid(self, date):
        pass

    @abstractmethod
    def get_district_cumulative_report(self, till_date, district_id):
        pass


    @abstractmethod
    def get_daily_cumulative_report_for_district(self):
        pass
    
    
    @abstractmethod
    def get_daily_cumulative_report_of_mandals_for_district(self,
            district_id: int):
        pass


    @abstractmethod
    def get_district_report_of_specific_day(
            self, date, district_id):
        pass

    @abstractmethod
    def get_day_wise_district_details(self, district_id):
        pass

    @abstractmethod
    def get_day_wise_mandal_details(self, district_id):
        pass

