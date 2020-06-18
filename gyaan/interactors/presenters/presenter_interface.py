from abc import ABC
from abc import abstractmethod
from gyaan.interactors.storages.dtos \
    import DomainDetailsDto, CompletePostDetailsDto, DomainDetailsWithPostsDto


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

    @abstractmethod
    def raise_invalid_post_ids_exception(self):
        pass

    @abstractmethod
    def response_get_posts(self, complete_post_details_dto: CompletePostDetailsDto):
        pass

    @abstractmethod
    def raise_invalid_value_for_offset(self):
        pass
    
    @abstractmethod
    def raise_invalid_value_for_limit(self):
        pass

    @abstractmethod
    def response_get_domain_details_with_posts(self,
            domain_details_with_posts: DomainDetailsWithPostsDto):
        pass
