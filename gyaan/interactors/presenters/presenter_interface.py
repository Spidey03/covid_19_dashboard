from abc import ABC
from abc import abstractmethod
from gyaan.interactors.storages.dtos import DomainDetailsDto


class PresenterInterface(ABC):

    @abstractmethod
    def raise_domain_does_not_exists(self):
        pass


    @abstractmethod
    def raise_user_not_follower(self):
        pass

    @abstractmethod
    def get_response_for_domain_details(self, domain_details_dto: DomainDetailsDto):
        pass