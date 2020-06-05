from abc import ABC
from abc import abstractmethod
from covid_dashboard.models\
    import State, District, Mandal, Stats
from covid_dashboard.interactors.storages.dtos\
    import (DailyCumulativeReport, CumulativeReportOnSpecificDay,
            StateDto, DistrictStatDto, DistrictDto)
from covid_dashboard.exceptions.exceptions\
    import InvalidStateId, InvalidDistrictId


class StateStorageInterface(ABC):

    @abstractmethod
    def is_state_id_valid(self, state_id: int):
        pass

    @abstractmethod
    def check_is_date_valid(self, date):
        pass

    @abstractmethod
    def get_state_wise_daily_report(self) -> StateDto:
        pass

    @abstractmethod
    def get_state_wise_cumulative_report(self) -> StateDto:
        pass

    @abstractmethod
    def get_daily_cumulative_report(self) -> DailyCumulativeReport:
        pass

    @abstractmethod
    def get_district_daily_cumulative_report(self):
        pass

    @abstractmethod
    def get_report_of_state_for_date(self, date):
        pass

    @abstractmethod
    def check_is_date_valid(self, date):
        pass

    @abstractmethod
    def get_state_wise_daily_cases_report(self):
        pass