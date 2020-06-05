from abc import ABC
from abc import abstractmethod
from covid_dashboard.interactors.storages.dtos\
    import (DailyStateDataDto, CumulativeStateDataDto,
            DailyDistrictDataDto, CumulativeDistrictDataDto)


class CovidStorageInterface(ABC):

    @abstractmethod
    def is_state_id_valid(self, state_id: int):
        pass


    @abstractmethod
    def is_district_id_valid(self, district_id: int):
        pass


    @abstractmethod
    def get_state_wise_daily_data(self, state_id: int) -> DailyStateDataDto:
        pass


    @abstractmethod
    def get_state_wise_cumulative_data(
            self, state_id: int) -> CumulativeStateDataDto:
        pass


    @abstractmethod
    def get_district_wise_daily_data(self, district_id) -> DailyDistrictDataDto:
        pass


    @abstractmethod
    def get_district_wise_cumulative_data(self,
            district_id) -> CumulativeDistrictDataDto:
        pass




