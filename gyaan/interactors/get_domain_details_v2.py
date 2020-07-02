from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.exceptions.custom_exceptions import UserNotDomainMember
from gyaan.interactors.mixin_interactor \
    import DomainValidationMixin, InvalidDomainId
from gyaan.interactors.storages.dtos_v3 import DomainDetailsDTO

class DomainDetailsInteractor(DomainValidationMixin):

    def __init__(self, post_storage: PostStorageInterface):
        self.post_storage = post_storage

    def get_domain_details_wrapper(self, user_id: int, domain_id: int,
                                   post_presenter: PostPresenterInterface):

        try:
            return self.get_domain_detials_response(
                user_id=user_id, domain_id=domain_id,
                post_presenter=post_presenter
            )
        except InvalidDomainId as err:
            invalid_domain_id = err.domain_id
            post_presenter.raise_exception_for_invalid_domain_id_v2(
                invalid_domain_id=invalid_domain_id
            )
        except UserNotDomainMember:
            post_presenter.raise_exception_for_user_not_domain_member()

    def get_domain_detials_response(self, user_id: int, domain_id: int,
                                    post_presenter: PostPresenterInterface):
        domain_details_dto = self.get_domain_details(user_id=user_id,
                                                 domain_id=domain_id)
        return post_presenter.get_domain_details_response(
            domain_details_dto)


    def get_domain_details(self, user_id: int, domain_id: int):
        # TODO: validate domain id
        self.validate_domain_id(domain_id)

        # TODO: validate user domain member
        self.is_user_following_domain(user_id, domain_id)

        domain_dto = self.post_storage.get_domain(domain_id)

        domain_stats = self.post_storage.get_domain_stats(domain_id)
        domain_expert_ids = self.post_storage.get_domain_expert_ids(domain_id)
        domain_experts = self.post_storage.get_users_details(domain_expert_ids)

        is_user_domain_expert, domain_join_requests, requested_user_dtos = \
            self._get_domain_expert_details(
                user_id=user_id, domain_id=domain_id
            )
        response = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats,
            domain_experts=domain_experts,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            join_requests=domain_join_requests,
            requested_users=requested_user_dtos
        )
        return response

    def _get_domain_expert_details(self, user_id: int, domain_id: int):
        is_user_domain_expert = self.post_storage.is_user_domain_expert(
            user_id, domain_id
        )
        domain_join_requests = []
        requested_user_dtos = []

        if is_user_domain_expert:
            domain_join_requests = self.post_storage.get_domain_join_requests(
                domain_id
            )
        if domain_join_requests:
            requested_user_dtos = self.post_storage.get_users_details(
                user_ids=[dto.user_id for dto in domain_join_requests]
            )
        return is_user_domain_expert, domain_join_requests, requested_user_dtos
