from abc import ABC
from abc import abstractmethod
from typing import List
from gyaan.interactors.storages.dtos import *

class StorageInterface(ABC):

    @abstractmethod
    def check_domain_is_valid(self, domain_id: int):
        pass

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

    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_post_details(self, post_ids: List[int]) -> List[PostDto]:
        pass

    @abstractmethod
    def get_posts_tags(self, post_ids: List[int]) -> List[PostTagDetailsDto]:
        pass

    @abstractmethod
    def get_post_reactions_count(self, post_ids: List[int]) -> List[PostReactionsCount]:
        pass

    @abstractmethod
    def get_post_comments_count(self, post_ids: List[int]) -> List[PostCommentsCount]:
        pass

    @abstractmethod
    def get_posts_latest_comments(self, post_ids: List[int], limit: int) -> List[int]:
        pass

    @abstractmethod
    def get_comments_reactions_count(self, comment_ids: List[int]) -> List[CommentReactionsCount]:
        pass

    @abstractmethod
    def get_comments_replies_count(self, comment_ids: List[int]) -> List[CommentRepliesCount]:
        pass

    @abstractmethod
    def get_comments(self, comment_ids: List[int]) -> List[CommentDto]:
        pass

    @abstractmethod
    def get_domain_post_ids(self, domain_id: int, offset: int, limit: int) -> List[int]:
        pass