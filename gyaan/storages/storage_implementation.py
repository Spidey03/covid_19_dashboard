from django.db.models import Prefetch, Count

from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.models import *
from gyaan.interactors.storages.dtos import *
from gyaan.constants.enums import (
    PostStatus, JoinStatus, ReactionEntityType
)


class StorageImplementation(StorageInterface):

    def validate_username(self, username):
        bool_feild = User.objects.filter(username=username).exists()
        return bool_feild

    def validate_password_for_username(self, username: str, password: str):

        user_obj = User.objects.get(username=username)
        is_valid_password_for_username = user_obj.check_password(password)

        print(is_valid_password_for_username)
        is_not_valid_password_for_username = not \
            is_valid_password_for_username
        print(is_not_valid_password_for_username)
        if is_not_valid_password_for_username:
            return False

        user_id = user_obj.id
        return user_id

    def get_user_id(self, username: str, password: str):
        user_obj = User.objects.get(username=username)
        return user_obj.id

    def get_user_metrics(self):
        pass

    def validate_post_id(self, post_id: int):
        bool_field = Post.objects.filter(id=post_id).exists()
        return bool_field

    def validate_comment_id(self, comment_id: int):
        bool_field = Comment.objects.filter(id=comment_id).exists()
        return bool_field


    # get_posts
    def get_posts(self, limit: int, offset: int):
        posts = Post.objects.select_related('domain','posted_by') \
            .order_by('-posted_at')[offset:offset+limit]
        post_dtos = []
        for post in posts:
            # print(post)
            domain_dto = DomainDto(
                domain_id=post.domain.id,
                name=post.domain.name,
                picture=post.domain.picture,
                members_dtos=[],
                request_dtos=[]
            )
            posted_by_dto = UserDto(
                user_id=post.posted_by.id,
                name=post.posted_by.name,
                profile_pic=post.posted_by.profile_pic
            )
            updated_post=post.postversion_set.order_by('-approved_at').first()

            post_dtos.append(
                GetPostDto(
                    post_id=post.id,
                    posted_by=posted_by_dto,
                    title=updated_post.title,
                    description=updated_post.description,
                    posted_at=post.posted_at,
                    tags=[],
                    comments_count=Comment.objects \
                        .filter(post_id=post.id).count(),
                    reactions_count=Reaction.objects \
                        .filter(post_id=post.id).count(),
                    domain=domain_dto,
                    )
                )
        return post_dtos

    def get_latest_comments(self, post_id: int):
        latest_comments = Comment.objects \
            .filter(post_id=post_id) \
            .select_related('commented_by') \
            .order_by('-commented_at')[:2]
        comment_dtos = []
        for comment in latest_comments:
            replies_count=Comment.objects.filter(
                parent_comment_id=comment.id).count()
            reactions_count=Reaction.objects.filter(
                comment_id=comment.id).count()

            comment_dtos.append(
                CommentDto(
                    comment_id=comment.id,
                    post_id=comment.post_id,
                    content=comment.content,
                    commented_at=comment.commented_at,
                    parent_comment=comment.parent_comment_id,
                    replies_count=replies_count,
                    reactions_count=reactions_count,
                    commented_by=self._convert_user_obj_to_dto(comment.commented_by),
                    reply_dtos=[]
                    )
                )
        return comment_dtos

    @staticmethod
    def _convert_user_obj_to_dto(user_obj):
        return UserDto(
            user_id=user_obj.id,
            name=user_obj.name,
            profile_pic=user_obj.profile_pic
            )

    def get_reply_dtos(self, comment_id: int):
        pass

    def get_answer_dto(self, post_id: int):
        answer_obj = Comment.objects \
            .filter(is_answer=True,post_id=post_id) \
            .select_related('commented_by').first()

        replies_count=Comment.objects.filter(
                parent_comment_id=answer_obj.id).count()
        reactions_count=Reaction.objects.filter(
            comment_id=answer_obj.id).count()
        answer_dto = AnswerDto(
            comment_id=answer_obj.id,
            post_id=answer_obj.post_id,
            commented_by=self._convert_user_obj_to_dto(
                answer_obj.commented_by),
            content=answer_obj.content,
            commented_at=answer_obj.commented_at,
            parent_comment=answer_obj.parent_comment_id,
            reactions_count=reactions_count,
            replies_count=replies_count,
            approved_by=None,
            reply_dtos=[]
        )
        return answer_dto

    def get_reaction_status(self, user_id: int, post_id: int):
        bool_feild = Reaction.objects.get(user_id=user_id,
                                          post_id=post_id).is_reacted
        return bool_feild

    def get_post_tags(self, post_id: int):
        pass

    def get_user_dto(self, user_id: int):
        user_obj = User.objects.get(id=user_id)
        return UserDto(
            user_id=user_obj.id,
            name=user_obj.name,
            profile_pic=user_obj.profile_pic
            )

    def get_following_domain_dtos(self, user_id: int):

        following_domains_queryset = DomainMembers.objects \
            .filter(member_id=user_id) \
            .select_related('domain')
        following_domains_list = []
        for domain_member in following_domains_queryset:
            domain = domain_member.domain
            following_domains_list.append(
                DomainDto(
                    domain_id=domain.id,
                    name=domain.name,
                    picture=domain.picture,
                    members_dtos=[],
                    request_dtos=[]
                    )
                )
        return following_domains_list

    def get_some_domain_dtos(self, user_id):

        some_domain_queryset = \
            Domain.objects \
                .exclude(domain_members__member_id=1)[:5]

        some_domains_list = []
        for domain in some_domain_queryset:
            some_domains_list.append(
                DomainDto(
                    domain_id=domain.id,
                    name=domain.name,
                    picture=domain.picture,
                    members_dtos=[],
                    request_dtos=[]
                    )
                )
        return some_domains_list

    def get_user_requested_domain_dtos(self, user_id: int):
        request_queryset = DomainJoinRequest.objects \
            .filter(user_id=user_id, status="REQUESTED") \
            .select_related('domain')
        requested_domain_list = [
            UserRequestedDomainDto(
                user_id=request.user_id,
                domain_id=request.domain_id,
                is_requested=True
                ) for request in request_queryset]
        return requested_domain_list

    def get_approved_posts_in_each_domain_dtos(self, user_id: int):
        approved_posts_queryset = Post.objects \
            .filter(is_approved=True, posted_by_id=user_id) \
            .select_related('domain') \
            .annotate(posts_count=Count('domain_id'))

        approved_posts_queryset = Domain.objects \
            .filter(posts__posted_by_id=user_id,
                    posts__postversion__status="APPROVED") \
            .annotate(posts_count=Count('id'))


        approved_posts_in_each_domain_dtos = [
            UserDomainPostDto(
                domain_id=domain.id,
                name=domain.name,
                picture=domain.picture,
                posts_count=domain.posts_count
                ) for domain in approved_posts_queryset
            ]
        return approved_posts_in_each_domain_dtos


    def get_pending_posts_in_each_domain_dtos(self, user_id: int):

        pending_posts_queryset = Domain.objects \
            .filter(posts__posted_by_id=user_id,
                    posts__postversion__status="PENDING") \
            .annotate(posts_count=Count('id'))

        pending_posts_in_each_domain_dtos = [
            UserDomainPostDto(
                domain_id=domain.id,
                name=domain.name,
                picture=domain.picture,
                posts_count=domain.posts_count
                ) for domain in pending_posts_queryset
            ]

        return pending_posts_in_each_domain_dtos


    def create_comment_to_post(self, user_id: int, entity_id: int,
                               content: str):

        Comment.objects.create(
            content=content,
            commented_by_id=user_id,
            post_id=entity_id,
            is_answer=False
        )

    def get_parent_comment_id(self, comment_id: int) -> int:
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return comment_id

        parent_comment_id = comment.parent_comment_id
        return parent_comment_id


    def create_reply_to_comment(self, user_id: int, entity_id: int,
                               content: str):

        Comment.objects.create(
            content=content,
            commented_by_id=user_id,
            post_id=entity_id,
            is_answer=False,
            parent_comment_id=entity_id
        )

    def mark_as_answer(self, user_id: int, comment_id: int):

        comment = Comment.objects.get(id=comment_id)
        comment.is_answer = True
        comment.is_approved_by_id = user_id
        comment.save()


    def create_reaction_to_comment(self, user_id, entity_id):
        try:
            reaction_obj = Reaction.objects.get(
                user_id=user_id, comment_id=entity_id)
        except Reaction.DoesNotExist:
            Reaction.objects.create(
                comment_id=entity_id,
                user_id=user_id,
            )
            return
        self.undo_reaction(reaction_obj)

    def create_reaction_to_post(self, user_id, entity_id):
        try:
            reaction_obj = Reaction.objects.get(
                user_id=user_id, post_id=entity_id)
        except Reaction.DoesNotExist:
            Reaction.objects.create(
                post_id=entity_id,
                user_id=user_id,
            )
            return
        self.undo_reaction(reaction_obj)

    @staticmethod
    def undo_reaction(reaction_obj):
        reaction_obj.delete()
