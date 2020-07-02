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
    def raiseinvalidusername(self):
        pass

    @abstractmethod
    def raiseinvalidpassword(self):
        pass

    @abstractmethod
    def raise_user_not_admin(self):
        pass