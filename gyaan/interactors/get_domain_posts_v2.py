from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.mixin_interactor \
    import DomainValidationMixin, InvalidDomainId
from gyaan.exceptions.custom_exceptions \
    import UserNotDomainMember, InvalidLimit, InvalidOffset

class GetDomainPostsInteractor(DomainValidationMixin):

    def __init__(self, post_storage: PostStorageInterface):
        self.post_storage = post_storage

    def get_domain_posts_wrapper(self, user_id: int, domain_id: int,
                                 offset: int, limit: int,
                                 post_presenter: PostPresenterInterface):

        try:
            return self.get_domain_posts_response(
                user_id=user_id,
                domain_id=domain_id,
                offset=offset,
                limit=limit,
                post_presenter=post_presenter
            )
        except InvalidDomainId as err:
            invalid_domain_id = err.domain_id
            return post_presenter.raise_exception_for_invalid_domain_id_v2(
                invalid_domain_id=invalid_domain_id
            )
        except InvalidOffset:
            return post_presenter.raise_exception_for_invalid_offset()
        except InvalidLimit:
            return post_presenter.raise_exception_for_invalid_limit()
        except UserNotDomainMember:
            return post_presenter.raise_exception_for_user_not_domain_member()


    def get_domain_posts_response(self, user_id: int, domain_id: int,
                                  offset: int, limit: int,
                                  post_presenter: PostPresenterInterface):
        domain_post_details_dtos = self.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )
        return post_presenter.get_domain_posts_response_v2(
            domain_post_details_dtos)

    def get_domain_posts(self, user_id: int, domain_id: int,
                         offset: int, limit: int):

        self.validate_domain_id(domain_id=domain_id)
        self.validate_offset_and_limit(offset, limit)
        self.is_user_following_domain(user_id, domain_id)

        # is_user_following_domain = self.post_storage.is_user_following_domain(
        #     user_id=user_id, domain_id=domain_id)
        # if not is_user_following_domain:
        #     raise UserNotDomainMember

        post_ids = self.post_storage.get_domain_post_ids(
            domain_id, limit, offset)

        from gyaan.interactors.get_posts_v2 import GetPosts
        get_posts_interactor = GetPosts(post_storage=self.post_storage)

        return get_posts_interactor.get_posts_details(
            user_id=user_id,
            post_ids=post_ids
        )
