from abc import ABC
from abc import abstractmethod

from gyaan.interactors.storages.dtos import (
    PostsCompleteDto,
    DomainExpertDetailsPresenterDto,
)

from gyaan.interactors.storages.dtos_v2 import (
    PostCompleteDetailsPresenterDto,
    PresenterDomainPostsDto, TagDto
)

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_username_exception(self):
        pass

    @abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abstractmethod
    def sign_in_response(self, user_auth_tokens_dto):
        pass

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
    def get_user_metrics_response(self, user_domain_post_metrics_dto):
        pass

    @abstractmethod
    def get_posts_response(self, all_posts_details_dto: PostsCompleteDto):
        pass

    @abstractmethod
    def get_domain_metrics_response(
            self, domain_expert_details_presenter_dto: \
                DomainExpertDetailsPresenterDto):
        pass
