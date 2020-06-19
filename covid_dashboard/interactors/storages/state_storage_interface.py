import datetime
from abc import ABC
from typing import List
from abc import abstractmethod
from covid_dashboard.interactors.storages.dtos import *

class StateStorageInterface(ABC):

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
