from abc import abstractmethod, ABC

from gyaan.interactors.storages.dtos_v2 import (
    PostCompleteDetailsPresenterDto,
    PresenterDomainPostsDto, TagDto
)
from typing import List
from gyaan.interactors.storages.dtos_v3 import *

class PostPresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_post_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_comment_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_domain_id(self):
        pass

    @abstractmethod
    def get_post_response(
            self, post_complete_details_dto: PostCompleteDetailsPresenterDto):
        pass


    @abstractmethod
    def get_domain_posts_response(
            self, presenter_domain_posts_dto: PresenterDomainPostsDto):
        pass

    # gyaan/v2
    @abstractmethod
    def raise_exception_for_invalid_post_ids(self,
                                             invalid_post_ids: List[int]):
        pass

    @abstractmethod
    def get_posts_response(self, completed_post_details: CompletePostDetails):
        pass

    @abstractmethod
    def raise_exception_for_invalid_domain_id_v2(self,
                                                 invalid_domain_id: int):
        pass

    @abstractmethod
    def get_domain_posts_response_v2(self, domain_post_details_dtos):
        pass

    @abstractmethod
    def raise_exception_for_user_not_domain_member(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit(self):
        pass

    @abstractmethod
    def get_domain_details_response(
            self, domain_details_dto: DomainDetailsDTO):
        pass

    @abstractmethod
    def get_domain_with_posts_response(
            self, domain_with_posts_response: DomainDetailsWithPosts):
        pas