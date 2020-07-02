import datetime
from django.db.models import Prefetch, Count

from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.models import *
from gyaan.interactors.storages.dtos import *
from gyaan.interactors.storages.dtos_v2 import *
from gyaan.constants.enums import (
    PostStatus, JoinStatus, ReactionEntityType
)

class DomainStorageImplementation(DomainStorageInterface):

    def validate_domain_id(self, domain_id: int):
        bool_field = Domain.objects.filter(id=domain_id).exists()
        return bool_field

    # get_domain_metrics

    def get_domain_details_dto(self, domain_id: int):
        pass

    def get_domain_expert_details_dto(self, domain_id: int):
        pass


    def get_domain_details_dto_with_experts_dtos(self, domain_id: int):

        domain = Domain.objects \
            .filter(id=domain_id) \
            .prefetch_related('experts') \
            .annotate(
                experts_count=Count('experts', distinct=True),
                no_of_followers=Count('domain_members__member', distinct=True),
                total_posts=Count('posts', distinct=True)
            ).get()

        domain_experts = domain.experts.all()
        domain_details_dto = self._get_domain_details_dto(domain)
        domain_expert_details_dto = self.convert_expert_objs_to_dto(
            domain_experts)

        return domain_details_dto, domain_expert_details_dto

    def get_user_status_for_this_domain(
            self, user_id: int, domain_id: int) -> bool:

        bool_feild = DomainMembers.objects.filter(
            member_id=user_id,domain_id=domain_id).exists()
        return bool_feild

    def get_post_review_requests_by_domain(
            self, user_id: int) -> PendingPostMetrics:

        pending_posts_queryset = Domain.objects \
            .filter(domains__expert_id=1,
                    posts__postversion__status="PENDING") \
            .annotate(posts_count=Count('id'))

        post_review_requests_dto = [
            UserDomainPostDto(
                domain_id=domain.id,
                name=domain.name,
                picture=domain.picture,
                posts_count=domain.posts_count
                ) for domain in pending_posts_queryset
            ]
        return post_review_requests_dto

    def get_domain_join_request_dtos(
            self, domain_id: int) -> DomainJoinRequestWithCountDto:
        request_objs = DomainJoinRequest.objects \
            .filter(domain_id=domain_id,status='REQUESTED') \
            .select_related('user')
        domain_join_request_dtos = [
            UserDto(
                user_id=request.id,
                name=request.user.name,
                profile_pic=request.user.profile_pic
            ) for request in request_objs ]
        return domain_join_request_dtos

    @staticmethod
    def _get_domain_details_dto(domain):
        return DomainDetailsDto(
                domain_id=domain.id,
                name=domain.name,
                description=domain.description,
                picture=domain.picture,
                no_of_followers=domain.no_of_followers,
                total_posts=domain.total_posts,
                likes=0
            )

    def convert_expert_objs_to_dto(self, experts):
        return DomainExpertsDetailsDto(
            total_experts=len(experts),
            domain_experts=[self._get_user_dict(expert) \
                for expert in experts]
            )

    @staticmethod
    def _get_user_dict(user):
        return UserDto(
            user_id=user.id,
            name=user.name,
            profile_pic=user.profile_pic
            )

    # domain related actions in web application
    def get_domain_tags_dto(self, domain_id: int) -> List[TagDto]:
        domain_tags = Tags.objects.filter(domain_id=domain_id)

        domain_tags_dto = [self._get_tag_dto(tag) for tag in domain_tags]

        return domain_tags_dto

    @staticmethod
    def _get_tag_dto(tag):
        tag_dto = TagDto(
            tag_id=tag.id,
            name=tag.name,
            post_id=None,
            domain_id=tag.domain_id
        )
        return tag_dto


    def create_domain_join_request(self, user_id: int, domain_id: int):
        DomainJoinRequest.objects.create(
            user_id=user_id, domain_id=domain_id
        )

    def cancel_domain_join_request(self, user_id: int, domain_id: int):
        request_obj = DomainJoinRequest.objects.get(
            user_id=user_id, domain_id=domain_id)
        request_obj.delete()

    def leave_a_domain(self, user_id: int, domain_id: int):
        domain_member_obj = Domain.objects.get(
            member_id=user_id, domain_id=domain_id
        )
        domain_member_obj.delete()
        domain_expert_obj = DomainExpert.objects.get(
            expert_id=user_id, domain_id=domain_id
        )
        domain_expert_obj.delete()


    def approve_a_join_request(self,
                user_id: int, requested_user_id: int):

        is_user_expert = self.validate_expert_status(user_id=user_id)

        is_not_expert = not is_user_expert
        if is_not_expert:
            return
        request_obj = DomainJoinRequest.objects.get(id=request_id)

        request_obj.acted_by_id = user_id
        request_obj.acted_at = datetime.datetime.now()
        request_obj.status = JoinStatus.APPROVED.value
        request_obj.save()

        DomainMembers.objects.create(
            member_id=request_obj.user_id, domain_id=request_obj.domain_id)

    def reject_a_join_request(self,
                user_id: int, requested_user_id: int):

        is_user_expert = self.validate_expert_status(user_id=user_id)

        is_not_expert = not is_user_expert
        if is_not_expert:
            return

        request_obj = DomainJoinRequest.objects.get(id=request_id)

        request_obj.acted_by_id = user_id
        request_obj.acted_at = datetime.datetime.now()
        request_obj.status = JoinStatus.REJECTED.value
        request_obj.save()


    @staticmethod
    def validate_expert_status(user_id):
        bool_field = DomainExpert.objects.filter(
                    expert_id=user_id, domain_id=domain_id).exists()
        return bool_field
