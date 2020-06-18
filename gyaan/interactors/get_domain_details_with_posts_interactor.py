from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.exceptions.exceptions \
    import DomainNotExists, UserIsNotFollwerOfDomain
from gyaan.interactors.storages.dtos import DomainDetailsWithPostsDto
from gyaan.exceptions.exceptions \
    import DomainNotExists, UserIsNotFollwerOfDomain, InvalidPostIdsException, \
        InvalidValueForLimit, InvalidValueForOffset


class GetDomainDetailsWithPostsInteractor:

    def __init__(self, storage=StorageInterface):

        self.storage = storage

    def get_domain_details_with_posts_wrapper(self, user_id: int,
            domain_id: int, offset: int, limit: int,
            presenter: PresenterInterface):

        try:
            domain_details_with_posts =self.get_domain_details_with_posts(
                user_id=user_id, domain_id=domain_id,
                offset=offset, limit=limit)
            response = presenter.response_get_domain_details_with_posts(
                domain_details_with_posts)
            return response
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

    def get_domain_details_with_posts(self, user_id: int, domain_id: int,
            offset: int, limit: int):

        domain_details = self._get_domain_details(user_id=user_id,
            domain_id=domain_id)

        domain_posts = self._get_domain_posts(user_id=user_id,
            domain_id=domain_id, offset=offset, limit=limit)

        domain_details_with_posts = DomainDetailsWithPostsDto(
            domain_details=domain_details,
            domain_posts=domain_posts
        )
        return domain_details_with_posts


    def _get_domain_details(self, user_id: int, domain_id: int):

        from gyaan.interactors.get_domain_details_interactor \
            import GetDomainDetailsInteractor
        get_domain_details_interactor = \
            GetDomainDetailsInteractor(storage=self.storage)

        domain_details = get_domain_details_interactor.get_domain_details(
            user_id=user_id, domain_id=domain_id)
        return domain_details

    def _get_domain_posts(self, user_id: int, domain_id: int,
            offset: int, limit: int):

        from gyaan.interactors.get_domain_posts_interactor \
            import GetDomainPostsInteractor
        get_doamin_posts_interactor = \
            GetDomainPostsInteractor(storage=self.storage)

        domain_posts = get_doamin_posts_interactor.get_domain_posts(
            user_id=user_id, domain_id=domain_id, offset=offset, limit=limit)
        return domain_posts
