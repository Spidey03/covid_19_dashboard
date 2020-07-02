from abc import ABC, abstractmethod

from typing import List

from gyaan.interactors.storages.dtos_v2 import (
    PostDetailsDto, DomainPostsDetailsDto
)
from gyaan.interactors.storages.dtos_v3 import *

class PostStorageInterface(ABC):

    @abstractmethod
    def validate_post_id(self, post_id: int):
        pass

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def get_post_details_dto(self, post_id: int) -> PostDetailsDto:
        pass

    @abstractmethod
    def get_domain_posts_details_dto(self, domain_id: int, limit: int,
                                     offset: int) -> DomainPostsDetailsDto:
        pass

    @abstractmethod
    def get_user_posts_details_dto(
        self, user_id: int, limit: int, offset: int) -> DomainPostsDetailsDto:
        pass


    @abstractmethod
    def create_post(self, user_id: int, title: str, domain_id: int,
                    content: str, tag_ids: List[int]):
        pass

    # gyaan/v2
    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_post_details(self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_post_tag_dtos(self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_post_reactions_count(self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_post_comments_count(self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_user_reaction_status(self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_latest_comments_ids_with_approved_comment_id(
            self, post_ids: List[int]):
        pass

    @abstractmethod
    def get_comment_dtos(self, comment_ids: List[int]):
        pass

    @abstractmethod
    def get_comment_reactions_count(self, comment_ids: List[int]):
        pass

    @abstractmethod
    def get_comment_replies_count(self, comment_ids: List[int]):
        pass

    @abstractmethod
    def get_user_dtos(self, user_ids: List[int]):
        pass

    @abstractmethod
    def get_domain_post_ids(self, domain_id: int, offset: int, limit: int):
        pass

    @abstractmethod
    def is_user_following_domain(self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain(self, domain_id: int) -> DomainDTO:
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> DomainStatsDTO:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_users_details(
            self, user_ids: List[int]) -> List[UserDetailsDTO]:
        pass

    @abstractmethod
    def is_user_domain_expert(
            self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_join_requests(
            self, domain_id: int) -> List[DomainJoinRequestDTO]:
        pass
