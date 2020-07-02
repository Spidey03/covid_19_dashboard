from abc import ABC, abstractmethod

from gyaan.interactors.storages.dtos import (
    PostsCompleteDto
)
from typing import List

class StorageInterface(ABC):

    @abstractmethod
    def validate_post_id(self, post_id: int):
        pass

    @abstractmethod
    def validate_comment_id(self, comment_id: int):
        pass

    @abstractmethod
    def validate_username(self, username: str):
        pass

    @abstractmethod
    def validate_password_for_username(
            self, username: str, password: str) -> int:
        pass

    @abstractmethod
    def get_user_id(self, username: str, password: str):
        pass

    @abstractmethod
    def get_user_metrics(self):
        pass

    @abstractmethod
    def get_posts(self, limti: int, offset: int) -> PostsCompleteDto:
        pass

    @abstractmethod
    def get_latest_comments(self, post_id: int):
        pass

    @abstractmethod
    def get_reply_dtos(self, comment_id: int):
        pass

    @abstractmethod
    def get_answer_dto(self, post_id: int):
        pass

    @abstractmethod
    def get_reaction_status(self, user_id: int, post_id: int):
        pass

    @abstractmethod
    def get_post_tags(self, post_id: int):
        pass

    @abstractmethod
    def get_user_dto(self, user_id: int):
        pass

    @abstractmethod
    def get_following_domain_dtos(self, user_id: int):
        pass

    @abstractmethod
    def get_some_domain_dtos(self, user_id: int):
        pass

    @abstractmethod
    def get_user_requested_domain_dtos(self, user_id: int):
        pass

    @abstractmethod
    def get_approved_posts_in_each_domain_dtos(self, user_id: int):
        pass

    @abstractmethod
    def get_pending_posts_in_each_domain_dtos(self, user_id: int):
        pass

    @abstractmethod
    def create_reaction_to_comment(self, user_id: int, entity_id: str):
        pass

    @abstractmethod
    def get_parent_comment_id(self, comment_id: int) -> int:
        pass

    @abstractmethod
    def create_reaction_to_post(self, user_id: int, entity_id: str):
        pass

    @abstractmethod
    def create_comment_to_post(self, user_id: int, entity_id: int,
                               content: str):
        pass

    @abstractmethod
    def create_reply_to_comment(self, user_id: int, entity_id: int,
                               content: str):
        pass

    @abstractmethod
    def mark_as_answer(self, user_id: int, comment_id: int):
        pass