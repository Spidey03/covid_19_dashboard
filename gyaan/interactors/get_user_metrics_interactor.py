from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface

from gyaan.interactors.storages.dtos \
    import FollowingDomainDto, SuggestedDomainDto, DomainPostDto, \
    UserPostMetricsDto, PendingPostMetrics, UserDomainPostMetricsDto

class GetUserMetricsInteractor:

    def __init__(self, storage=StorageInterface,
                 presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def get_user_metrcis(self, user_id: int):


        user_dto = self.storage.get_user_dto(user_id)
        following_domain_dtos = self.storage.get_following_domain_dtos(
            user_id=user_id
        )
        some_domain_dtos = self.storage.get_some_domain_dtos(user_id)
        user_requested_domain_dtos = self.\
            storage.get_user_requested_domain_dtos(
                user_id=user_id
            )

        suggested_domain_dtos = self.get_suggested_domain_dtos(
            some_domain_dtos, user_requested_domain_dtos
        )

        approved_posts_in_each_domain_dtos = self.storage. \
            get_approved_posts_in_each_domain_dtos(user_id)

        approved_posts_count = self._get_total_posts_count(
            approved_posts_in_each_domain_dtos)

        user_post_metrics_dto = UserPostMetricsDto(
            total_posts=approved_posts_count,
            posts_in_each_domain_dtos=approved_posts_in_each_domain_dtos
        )

        pending_posts_in_each_domain_dtos = self.storage. \
            get_pending_posts_in_each_domain_dtos(user_id)

        pending_posts_count = self._get_total_posts_count(
            approved_posts_in_each_domain_dtos)

        pending_post_metrics_dto = PendingPostMetrics(
            pending_posts_count=pending_posts_count,
            pending_posts_in_each_domain_dtos= \
                pending_posts_in_each_domain_dtos)

        user_domain_post_metrics_dto = UserDomainPostMetricsDto(
            user_dto=user_dto,
            following_domain_dtos=following_domain_dtos,
            suggested_domain_dtos=suggested_domain_dtos,
            user_post_metrics_dto=user_post_metrics_dto,
            pending_post_metrics_dto=pending_post_metrics_dto
        )

        response = self.presenter.get_user_metrics_response(
            user_domain_post_metrics_dto=user_domain_post_metrics_dto
        )

        return response


    @staticmethod
    def _get_total_posts_count(posts_in_each_domain):
        total = 0
        for post in posts_in_each_domain:
            total = total+post.posts_count
        return total

    @staticmethod
    def get_suggested_domain_dtos(some_domain_dtos,
                                   user_requested_domain_dtos):
        user_requested_domain_ids = [request.domain_id for request in \
            user_requested_domain_dtos]
        suggested_domains_dtos = []
        for some_domain in some_domain_dtos:
            is_user_requested = some_domain.domain_id in \
                user_requested_domain_ids
            suggested_domains_dtos.append(
                SuggestedDomainDto(domain_dto=some_domain,
                                   is_requested=is_user_requested)
            )
        return suggested_domains_dtos
