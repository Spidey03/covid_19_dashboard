from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import (
    PendingPostMetrics, DomainJoinRequestWithCountDto,
    DomainExpertDetailsPresenterDto
)

class GetDomainMetricsInteractor:

    def __init__(self, domain_storage: DomainStorageInterface,
                 presenter: PresenterInterface):
        self.domain_storage = domain_storage
        self.presenter = presenter


    def get_domain_metrics(self, domain_id: int, user_id: int):

        is_not_valid_domain_id = not self.domain_storage.validate_domain_id(
            domain_id=domain_id
        )
        if is_not_valid_domain_id:
            self.presenter.raise_exception_for_invalid_domain_id()
            return

        domain_details_dto, domain_expert_details_dto = \
            self.domain_storage.get_domain_details_dto_with_experts_dtos(
                domain_id=domain_id)

        is_user_following_this_domain = self.domain_storage. \
            get_user_status_for_this_domain(user_id, domain_id)

        is_user_expert_for_this_domain = \
            self._validate_user_with_domain_experts(
                domain_expert_details_dto, user_id)

        domain_expert_details_presenter_dto = \
                DomainExpertDetailsPresenterDto(
                    domain_details_dto=domain_details_dto,
                    domain_expert_details_dto=domain_expert_details_dto,
                    is_following=is_user_following_this_domain,
                    post_review_requests_dto=None,
                    domain_join_request_details_dtos= \
                        None
                )

        if is_user_expert_for_this_domain:
            is_user_following_this_domain = True
            post_review_requests_dto = self.domain_storage. \
                get_post_review_requests_by_domain(user_id)
            post_review_requests_count = self._get_total_posts_count(
                post_review_requests_dto)

            pending_post_metrics_dto = PendingPostMetrics(
                pending_posts_count=post_review_requests_count,
                pending_posts_in_each_domain_dtos= \
                    post_review_requests_dto
            )


            domain_join_request_dtos = self.domain_storage. \
                get_domain_join_request_dtos(domain_id)

            domain_join_requests_count = len(domain_join_request_dtos)

            domain_join_request_details_dtos = DomainJoinRequestWithCountDto(
                requests_count=domain_join_requests_count,
                domain_join_request_dtos=domain_join_request_dtos
                )

            domain_expert_details_presenter_dto = \
                DomainExpertDetailsPresenterDto(
                    domain_details_dto=domain_details_dto,
                    domain_expert_details_dto=domain_expert_details_dto,
                    is_following=is_user_following_this_domain,
                    post_review_requests_dto=pending_post_metrics_dto,
                    domain_join_request_details_dtos= \
                        domain_join_request_details_dtos
                )

        response =self.presenter.get_domain_metrics_response(
            domain_expert_details_presenter_dto= \
                domain_expert_details_presenter_dto
        )
        return response


    @staticmethod
    def _validate_user_with_domain_experts(
        domain_expert_details_dto, user_id):
        domain_experts = domain_expert_details_dto.domain_experts
        bool_feild = user_id in [
            expert.user_id for expert in domain_experts]
        return bool_feild

    @staticmethod
    def _get_total_posts_count(post_review_requests_dto):
        total = 0
        for post in post_review_requests_dto:
            total = total+post.posts_count
        return total

