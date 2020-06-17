from abc import ABC
from abc import abstractmethod
from typing import List
from gyaan.interactors.storages.dtos \
    import DomainDto, UserDto, DomainStatDto, DomainJoinRequestDto

class StorageInterface(ABC):

    @abstractmethod
    def get_domain_details(self, domain_id: int) -> DomainDto:
        pass

    @abstractmethod
    def check_user_is_follower_of_domain(self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> DomainStatDto:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_users_details(self, ids: List[int]) -> List[UserDto]:
        pass

    @abstractmethod
    def is_user_domain_expert(self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_join_request(self, domain_id: int) -> List[DomainJoinRequestDto]:
        pass