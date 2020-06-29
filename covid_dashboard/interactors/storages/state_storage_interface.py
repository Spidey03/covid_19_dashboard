import datetime
from abc import ABC
from typing import List
from abc import abstractmethod
from covid_dashboard.interactors.storages.dtos import *

class StateStorageInterface(ABC):

    @abstractmethod
    def check_state_id_is_valid(self, state_id):
        pass

    @abstractmethod
    def get_initial_and_final_dates(self):
        pass

    @abstractmethod
    def get_state_details(self, state_id: int) -> StateDto:
        pass

    @abstractmethod
    def get_districts_for_state(self, state_id: int) -> List[DistrictDto]:
        pass

    @abstractmethod
    def get_cumulative_report_for_districts(self, district_ids: List[int],
            till_date: datetime.date) -> List[DistrictReportDto]:
        pass

    @abstractmethod
    def state_get_day_wise_report(self, state_id: int) -> List[DayReportDto]:
        pass

    @abstractmethod
    def get_day_wise_report_for_distrcts(self,
            district_ids: List[int]) -> DistrictDayReportDto:
        pass
