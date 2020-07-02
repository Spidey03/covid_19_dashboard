from typing import List

from django.db.models import Count, Prefetch

from gyaan.models import *
from gyaan.interactors.storages.dtos_v2 import (
    PostDetailsDto, DomainPostsDetailsDto
)

from gyaan.interactors.storages.dtos_v2 import *
from gyaan.interactors.storages.dtos_v3 import *
from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface

class PostStorageImplementation(PostStorageInterface):

    def validate_post_id(self, post_id: int):
        bool_field = Post.objects.filter(id=post_id).exists()
        return bool_field

    def validate_domain_id(self, domain_id: int):
        bool_field = Domain.objects.filter(id=domain_id).exists()
        return bool_field


    def get_post_details_dto(self, post_id: int) -> PostDetailsDto:

        comment_queryset = Comment.objects \
            .select_related('commented_by', 'is_approved_by') \
        	.prefetch_related(
                    Prefetch('reaction_set', to_attr='comment_reactions')
            )

        tags_queryset = PostTags.objects \
            .select_related('tag')
        latest_post_version = PostVersion.objects \
            .filter(post__id=post_id) \
            .select_related('post__posted_by','post__domain') \
	        .prefetch_related(
                Prefetch('post__comments', queryset=comment_queryset,
                         to_attr="all_comments"),
                Prefetch('post__reaction_set', to_attr="post_reactions"),
                Prefetch('post_tags', queryset=tags_queryset)
            ).order_by('-approved_at').first()

        post_details_dto = self.convert_post_obj_to_dto(latest_post_version)

        return post_details_dto


    def convert_post_obj_to_dto(self, latest_post_version):
        post_dto = self._get_post_dto(latest_post_version)
        domain_dto = self._get_domain_dto(latest_post_version.post.domain)
        users_dto = self._get_all_users_dto(latest_post_version)
        comments_dto = self._get_all_comments_dto(
            latest_post_version.post.all_comments)
        reactions_dto = self._get_reactions_dto(
            latest_post_version.post.post_reactions)
        tags_dto = self._get_tags_dto(latest_post_version.post_tags.all())

        post_details_dto = PostDetailsDto(
            post_dto=post_dto, domain_dto=domain_dto, users_dto=users_dto,
            comments_dto=comments_dto, reactions_dto=reactions_dto,
            tags_dto=tags_dto
        )

        return post_details_dto


    @staticmethod
    def _get_post_dto(latest_post_version):
        post_dto = PostDto(
            user_id=latest_post_version.post.posted_by_id,
            post_id=latest_post_version.post.id,
            domain_id=latest_post_version.post.domain_id,
            title=latest_post_version.title,
            description=latest_post_version.description,
            posted_at=latest_post_version.approved_at
        )
        return post_dto

    @staticmethod
    def _get_domain_dto(domain):
        domain_dto = DomainDto(
            domain_id=domain.id,
            name=domain.name,
            description=domain.description,
            picture=domain.picture,
            experts=None,
            members=None
        )
        return domain_dto

    def _get_all_users_dto(self, latest_post_version):
        all_users_dto = []
        posted_by = latest_post_version.post.posted_by
        posted_by_dto = self._convert_user_obj_to_dto(posted_by)
        all_users_dto.append(posted_by_dto)

        comment_objs = latest_post_version.post.all_comments

        all_users_dto = all_users_dto + \
            [self._convert_user_obj_to_dto(comment.commented_by)
             for comment in comment_objs]

        return all_users_dto

    @staticmethod
    def _convert_user_obj_to_dto(user):
        user_dto = UserDto(
            user_id=user.id,
            name=user.name,
            profile_pic=user.profile_pic
        )
        return user_dto

    def _get_all_comments_dto(self, comment_objs):
        comments_dto = [self._convert_comment_obj_to_dto(comment)
                        for comment in comment_objs]
        return comments_dto


    @staticmethod
    def _convert_comment_obj_to_dto(comment):
        comment_dto = CommentDto(
            comment_id=comment.id,
            content=comment.content,
            user_id=comment.commented_by_id,
            is_answer=comment.is_answer,
            approved_by_id=comment.is_approved_by_id,
            post_id=comment.post_id,
            commented_at=comment.commented_at,
            parent_comment=comment.parent_comment_id
        )
        return comment_dto

    def _get_reactions_dto(self, reaction_objs):
        reactions_dto = [self._convert_reaction_obj_to_dto(reaction)
                        for reaction in reaction_objs]
        return reactions_dto

    @staticmethod
    def _convert_reaction_obj_to_dto(reaction):
        reaction_dto = ReactionDto(
            reaction_id=reaction.id,
            post_id=reaction.post_id,
            comment_id=reaction.comment_id,
            user_id=reaction.user_id
        )
        return reaction_dto

    def _get_tags_dto(self, post_tag_objs):
        tags_dto = [self._convert_tag_obj_to_dto(post_tag)
                    for post_tag in post_tag_objs]
        return tags_dto

    @staticmethod
    def _convert_tag_obj_to_dto(post_tag):
        post_tag_dto = TagDto(
            tag_id=post_tag.tag.id,
            name=post_tag.tag.name,
            post_id=post_tag.post_id,
            domain_id=post_tag.tag.domain_id
        )
        return post_tag_dto


    # get_domain_posts
    def get_domain_posts_details_dto(
        self, domain_id: int, limit: int, offset: int) -> DomainPostsDetailsDto:

        comment_queryset = Comment.objects \
            .select_related('commented_by', 'is_approved_by') \
        	.prefetch_related(
                    Prefetch('reaction_set', to_attr='comment_reactions')
            )

        tags_queryset = PostTags.objects \
            .select_related('tag')

        version_queryset = PostVersion.objects \
            .prefetch_related(
		        Prefetch('post_tags', queryset=tags_queryset)
	        ).order_by('-approved_by')

        domain_posts = Post.objects.filter(domain_id=domain_id) \
        	.select_related('posted_by', 'domain') \
        	.prefetch_related(
        		Prefetch('postversion_set', queryset=version_queryset,
        		         to_attr="version"),
        		Prefetch('comments', queryset=comment_queryset,
        		         to_attr="all_comments"),
        		Prefetch('reaction_set', to_attr="post_reactions")
        	)[offset:offset+limit]

        domain_posts_details_dto = self.get_all_posts_dto(domain_posts)
        return domain_posts_details_dto


    def get_all_posts_dto(self, domain_posts):

        posts_dto = [self._get_post_dto_from_post(post)
                     for post in domain_posts]
        domains_dto = [self._get_domain_dto(post.domain)
                       for post in domain_posts]
        users_dto = self._get_all_users_dto_from_post(domain_posts)
        comments_dto = self._get_all_posts_comments_dto_from_post(
            domain_posts)
        reactions_dto = self._get_all_posts_reactions_dto_from_post(
            domain_posts)
        tags_dto = self._get_all_posts_tags_dto_from_post(domain_posts)

        domain_posts_details_dto = DomainPostsDetailsDto(
            posts_dto=posts_dto,
            domains_dto=domains_dto,
            users_dto=users_dto,
            comments_dto=comments_dto,
            reactions_dto=reactions_dto,
            tags_dto=tags_dto
        )
        return domain_posts_details_dto


    def _get_all_users_dto_from_post(self, domain_posts):
        all_users_dto = []
        posted_by_users_dto = [self._convert_user_obj_to_dto(post.posted_by)
                               for post in domain_posts]
        commented_by_users_dto = self.get_commented_by_users_dto(domain_posts)
        posted_by_users_dto.extend(commented_by_users_dto)
        all_users_dto.extend(posted_by_users_dto)
        return all_users_dto


    def get_commented_by_users_dto(self, domain_posts):
        commented_by_users_dto = []
        for post in domain_posts:
            comments = post.all_comments
            post_commented_by_dtos = \
                self._get_comment_commented_by_dtos(comments)

            commented_by_users_dto.extend(post_commented_by_dtos)
        return commented_by_users_dto


    def _get_comment_commented_by_dtos(self, comments):
        commented_by_dtos = []
        commented_by_dtos = \
            [self._convert_user_obj_to_dto(comment.commented_by)
             for comment in comments]
        commented_by_dtos.extend(
            [self._convert_user_obj_to_dto(comment.is_approved_by)
             for comment in comments if comment.is_approved_by_id != None]
            )
        return commented_by_dtos


    def _get_all_posts_comments_dto_from_post(self, domain_posts):
        all_posts_comments_dto = []
        for post in domain_posts:
            comments = post.all_comments[:2]
            comments_dto = self._get_all_comments_dto(comments)
            all_posts_comments_dto.extend(comments_dto)
        return all_posts_comments_dto


    def _get_all_posts_reactions_dto_from_post(self, domain_posts):
        all_posts_reactions_dto = []
        for post in domain_posts:
            post_reactions_dto = self._get_post_reactions_dto_from_post(post)
            all_posts_reactions_dto.extend(post_reactions_dto)
        return all_posts_reactions_dto


    def _get_post_reactions_dto_from_post(self, post):
        post_reactions = self._get_reactions_dto(post.post_reactions)
        for comment in post.all_comments:
            comment_reactions = \
                self._get_reactions_dto(comment.comment_reactions)
            post_reactions.extend(comment_reactions)
        return post_reactions

    def _get_all_posts_tags_dto_from_post(self, domain_posts):
        all_posts_tags_dto = []
        for post in domain_posts:
            updated_post = post.version[0]
            post_tags_dto = self._get_updated_post_tags_dto(updated_post)
            all_posts_tags_dto.extend(post_tags_dto)
        return all_posts_tags_dto

    def _get_updated_post_tags_dto(self, updated_post):
        post_tags_dto = self._get_tags_dto(updated_post.post_tags.all())
        return post_tags_dto

    @staticmethod
    def _get_post_dto_from_post(post):
        updated_post = post.version[0]
        post_dto = PostDto(
            user_id=post.posted_by_id,
            post_id=post.id,
            domain_id=post.domain_id,
            title=updated_post.title,
            description=updated_post.description,
            posted_at=post.posted_at
        )
        return post_dto

    # get_posts
    def get_user_posts_details_dto(self, user_id: int, limit:int,
                                   offset: int) -> DomainPostsDetailsDto:

        comment_queryset = Comment.objects \
            .select_related('commented_by', 'is_approved_by') \
        	.prefetch_related(
                    Prefetch('reaction_set', to_attr='comment_reactions')
            )

        tags_queryset = PostTags.objects \
            .select_related('tag')

        version_queryset = PostVersion.objects \
            .prefetch_related(
		        Prefetch('post_tags', queryset=tags_queryset)
	        ).order_by('-approved_by')

        users_posts = Post.objects.filter(
                domain__domain_members__member_id=user_id) \
        	.select_related('posted_by', 'domain') \
        	.prefetch_related(
        		Prefetch('postversion_set', queryset=version_queryset,
        		         to_attr="version"),
        		Prefetch('comments', queryset=comment_queryset,
        		         to_attr="all_comments"),
        		Prefetch('reaction_set', to_attr="post_reactions")
        	)[offset:offset+limit]

        domain_posts_details_dto = self.get_all_posts_dto(users_posts)
        return domain_posts_details_dto

    def create_post(self, user_id: int, title: str, domain_id: int,
                    content: str, tag_ids: List[int]):
        post = Post.objects.create(
            is_approved=False,
            posted_by_id=user_id,
            domain_id=domain_id
        )

        PostVersion.objects.create(
            title=title,
            description=content,
            status=PostStatus.PENDING.value,
            post=post
        )

        post_id = post.id
        post_tags_instances = []
        for tag_id in tag_ids:
            post_tags_instances.append(
                PostTags(post_id=post_id,tag_id=tag_id)
            )

        PostTags.objects.bulk_create(post_tags_instances)


    # gyaan/v2
    def get_valid_post_ids(self, post_ids: List[int]):
        pass

    def get_post_details(self, post_ids: List[int]):
        pass

    def get_post_tag_dtos(self, post_ids: List[int]):
        pass

    def get_post_reactions_count(self, post_ids: List[int]):
        pass

    def get_post_comments_count(self, post_ids: List[int]):
        pass

    def get_user_reaction_status(self, post_ids: List[int]):
        pass

    def get_latest_comments_ids_with_approved_comment_id(
            self, post_ids: List[int]):
        pass

    def get_comment_dtos(self, comment_ids: List[int]):
        pass

    def get_comment_reactions_count(self, comment_ids: List[int]):
        pass

    def get_comment_replies_count(self, comment_ids: List[int]):
        pass

    def get_user_dtos(self, user_ids: List[int]):
        pass

    def get_domain_post_ids(self, domain_id: int, offset: int, limit: int):
        pass

    def is_user_following_domain(self, user_id: int, domain_id: int) -> bool:
        pass

    def get_domain(self, domain_id: int) -> DomainDTO:
        pass

    def get_domain_stats(self, domain_id: int) -> DomainStatsDTO:
        pass

    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    def get_users_details(
            self, user_ids: List[int]) -> List[UserDetailsDTO]:
        pass

    def is_user_domain_expert(
            self, user_id: int, domain_id: int) -> bool:
        pass

    def get_domain_join_requests(
            self, domain_id: int) -> List[DomainJoinRequestDTO]:
        pass
