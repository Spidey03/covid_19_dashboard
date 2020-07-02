from abc import ABC, abstractmethod

from typing import List

from gyaan.interactors.storages.dtos import (
    PendingPostMetrics, DomainJoinRequestWithCountDto
)
from gyaan.interactors.storages.dtos_v2 import (
    TagDto
)

class DomainStorageInterface(ABC):

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def get_domain_details_dto(self, domain_id: int):
        pass

    @abstractmethod
    def get_domain_expert_details_dto(self, domain_id: int):
        pass


    @abstractmethod
    def get_domain_details_dto_with_experts_dtos(self, domain_id: int):
        pass


    @abstractmethod
    def get_user_status_for_this_domain(
            self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_post_review_requests_by_domain(
            self, user_id: int) -> PendingPostMetrics:
        pass

    @abstractmethod
    def get_domain_join_request_dtos(
            self, domain_id: int) -> DomainJoinRequestWithCountDto:
        pass

    @abstractmethod
    def get_domain_tags_dto(self, domain_id: int) -> TagDto:
        pass

    @abstractmethod
    def create_domain_join_request(self, user_id: int, domain_id: int):
        pass

    @abstractmethod
    def cancel_domain_join_request(self, user_id: int, domain_id: int):
        pass

    @abstractmethod
    def leave_a_domain(self, user_id: int, domain_id: int):
        pass

    @abstractmethod
    def approve_a_join_request(self,
                user_id: int, request_id: int):
        pass

    @abstractmethod
    def reject_a_join_request(self,
                user_id: int, request_id: int):
        pass
