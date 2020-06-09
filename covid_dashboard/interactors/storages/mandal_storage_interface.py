from abc import ABC
from abc import abstractmethod
from covid_dashboard.models\
    import State, District, Mandal, Stats
from covid_dashboard.interactors.storages.dtos\
    import (DailyCumulativeReport, CumulativeReportOnSpecificDay,
            StateDto, DistrictStatDto, DistrictDto)
from covid_dashboard.exceptions.exceptions\
    import InvalidStateId, InvalidDistrictId


class MandalStorageInterface(ABC):
    
    @abstractmethod
    def is_user_admin(self, user):
        pass

    @abstractmethod
    def is_valid_total_confirmed(self, total_confirmed: int):
        pass

    @abstractmethod
    def is_valid_total_deaths(self, total_deaths: int):
        pass

    @abstractmethod
    def is_valid_total_recovered(self, total_recovered: int):
        pass

    @abstractmethod
    def is_valid_mandal_id(self, mandal_id: int):
        pass

    @abstractmethod
    def check_is_date_valid(self, date):
        pass

    @abstractmethod
    def add_new_statistics(self, mandal_id: int, total_confirmed: int,
            date, total_deaths: int, total_recovered: int):
        pass

    @abstractmethod
    def update_statistics(self, mandal_id: int, total_confirmed: int,
            date, total_deaths: int, total_recovered: int):
        pass

    @abstractmethod
    def is_statistics_valid(self, total_confirmed: int, 
            total_deaths: int, total_recovered: int):
        pass

    @abstractmethod
    def is_already_exist(self, mandal_id: int, date: int):
        pass

    @abstractmethod
    def get_statistics(self, mandal_id):
        pass