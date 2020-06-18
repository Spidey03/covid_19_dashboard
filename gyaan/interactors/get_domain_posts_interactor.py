from typing import List
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import CompletePostDetailsDto
from gyaan.exceptions.exceptions \
    import DomainNotExists, UserIsNotFollwerOfDomain, InvalidPostIdsException, \
        InvalidValueForLimit, InvalidValueForOffset


class GetDomainPostsInteractor:

    def __init__(self, storage=StorageInterface):

        self.storage = storage

    def get_domain_posts_wrapper(self, user_id: int, domain_id: int,
            offset: int, limit: int, presenter: PresenterInterface):
        try:
            complete_post_details_dto = \
                self.get_domain_posts(user_id=user_id, domain_id=domain_id,
                    offset=offset, limit=limit)
            return presenter.response_get_posts(complete_post_details_dto)
        except DomainNotExists:
            presenter.raise_domain_does_not_exists()
        except UserIsNotFollwerOfDomain:
            presenter.raise_user_not_follower()
        except InvalidValueForOffset:
            presenter.raise_invalid_value_for_offset()
        except InvalidValueForLimit:
            presenter.raise_invalid_value_for_limit()
        except InvalidPostIdsException:
            raise presenter.raise_invalid_post_ids_exception()

    def get_domain_posts(self, user_id: int, domain_id: int,
            offset: int, limit: int):

        self.storage.check_domain_is_valid(domain_id=domain_id)
        is_user_follower = self.storage.check_user_is_follower_of_domain(
            user_id=user_id, domain_id=domain_id)
        user_is_not_follower = not is_user_follower
        if user_is_not_follower:
            raise UserIsNotFollwerOfDomain

        self.check_offset_value_is_valid(offset=offset)
        self.check_limit_value_is_valid(offset=offset, limit=limit)

        post_ids = self.storage.get_domain_post_ids(domain_id=domain_id,
            offset=offset, limit=limit)

        from gyaan.interactors.get_posts_interactor import GetPostsInteractor
        get_posts_interactor = GetPostsInteractor(storage=self.storage)

        return get_posts_interactor.get_posts(post_ids=post_ids)

    def check_offset_value_is_valid(self, offset: int):
        if offset < 0:
            raise InvalidValueForOffset

    def check_limit_value_is_valid(self, offset: int, limit: int):
        if limit < 0 or limit <= offset:
            raise InvalidValueForLimit
