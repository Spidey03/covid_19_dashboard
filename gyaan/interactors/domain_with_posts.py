from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.exceptions.custom_exceptions import UserNotDomainMember
from gyaan.interactors.mixin_interactor \
    import DomainValidationMixin, InvalidDomainId
from gyaan.interactors.storages.dtos_v3 import DomainDetailsWithPosts

class DomainWithPosts(DomainValidationMixin):

    def __init__(self, post_storage: PostStorageInterface):
        self.post_storage = post_storage

    def domain_with_posts_wrapper(self, user_id: int,
                                  domain_id: int,
                                  offset: int, limit: int,
                                  post_presenter: PostPresenterInterface):

        try:
            return self.get_domain_with_posts_response(
                user_id=user_id,
                domain_id=domain_id,
                offset=offset, limit=limit,
                post_presenter=post_presenter
            )

        except InvalidDomainId as err:
            invalid_domain_id = err.domain_id
            post_presenter.raise_exception_for_invalid_domain_id_v2(
                invalid_domain_id=invalid_domain_id
            )
        except UserNotDomainMember:
            post_presenter.raise_exception_for_user_not_domain_member()

    def get_domain_with_posts_response(self, user_id: int,
                                       domain_id: int,
                                       offset: int, limit: int,
                                       post_presenter: PostPresenterInterface):

        domain_with_posts_response = self.get_domain_with_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset, limit=limit
        )
        return post_presenter.get_domain_with_posts_response(
            domain_with_posts_response
        )

    def get_domain_with_posts(self, user_id: int, domain_id: int,
                              offset: int, limit: int):

        from gyaan.interactors.get_domain_details_v2 \
            import DomainDetailsInteractor
        from gyaan.interactors.get_domain_posts_v2 \
            import GetDomainPostsInteractor

        domain_details_interactor = \
            DomainDetailsInteractor(post_storage=self.post_storage)

        domain_details = \
            domain_details_interactor.get_domain_details(
                user_id=user_id,
                domain_id=domain_id
            )

        domain_posts_interactor = \
            GetDomainPostsInteractor(post_storage=self.post_storage)

        domain_posts = domain_posts_interactor.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset, limit=limit
        )
        return DomainDetailsWithPosts(
            domain_details=domain_details,
            post_details=domain_posts
        )
