from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound

from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.storages.dtos_v2 import (
    PostCompleteDetailsPresenterDto,
    PresenterDomainPostsDto, TagDto
)
from gyaan.constants.exception_messages \
    import (
        INVALID_POST_ID, INVALID_COMMENT_ID, INVALID_DOMAIN_ID
    )
from typing import List
from gyaan.constants.constants import get_datetime
from gyaan.interactors.storages.dtos_v3 import *

class PostPresenterImplementation(PostPresenterInterface):

    def raise_exception_for_invalid_post_id(self):
        raise NotFound(*INVALID_POST_ID)

    def raise_exception_for_invalid_domain_id(self):
        raise NotFound(*INVALID_DOMAIN_ID)

    def raise_exception_for_invalid_comment_id(self):
        raise NotFound(*INVALID_COMMENT_ID)

    def get_post_response(
            self, post_complete_details_dto: PostCompleteDetailsPresenterDto):

        post_details_dto = post_complete_details_dto.post_details_dto

        post_dict = self.convert_post_dto_to_dict(post_complete_details_dto)
        return post_dict

    def convert_post_dto_to_dict(self, post_complete_details_dto):
        post_details_dto = post_complete_details_dto.post_details_dto
        users_dto = post_details_dto.users_dto
        users_dict = self.convert_all_users_dto_to_dict(users_dto)
        post_dto = post_details_dto.post_dto
        tags_dto = post_details_dto.tags_dto
        comments_details_dto = post_complete_details_dto.comments_details_dto

        post_dict = {
            "post_id": post_dto.post_id,
            "posted_by": users_dict[post_dto.user_id],
            "title": post_dto.title,
            "description": post_dto.description,
            "posted_at": get_datetime(post_dto.posted_at),
            "tags": [self.convert_tag_dto_to_dict(tag_dto)
                     for tag_dto in tags_dto],
            "comments_count": post_complete_details_dto.comments_count,
            "reactions_count": post_complete_details_dto.post_reactions_count,
            "domain": self.convert_domain_dto_to_dict(
                post_details_dto.domain_dto),
            "is_reacted": post_complete_details_dto.is_user_reacted,
            "approved_answer": self.convert_answer_dto_to_dict(
                post_complete_details_dto.approved_answer_dto, users_dict,
                comments_details_dto),
            "latest_comments": [self.convert_comment_dto_to_dict(
                comment, users_dict) for comment in comments_details_dto]
        }

        return post_dict

    def convert_all_users_dto_to_dict(self, users_dto):
        users_dict = {}
        for user_dto in users_dto:
            users_dict[user_dto.user_id] = \
                self._convert_user_dto_to_dict(user_dto)
        return users_dict

    @staticmethod
    def _convert_user_dto_to_dict(user_dto):
        return {
            "user_id": user_dto.user_id,
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic
        }

    @staticmethod
    def convert_tag_dto_to_dict(tag_dto):
        return {
            "id": tag_dto.tag_id,
            "name": tag_dto.name
        }

    @staticmethod
    def convert_domain_dto_to_dict(domain_dto):
        return {
            "domain_id": domain_dto.domain_id,
            "name": domain_dto.name,
            "picture": domain_dto.picture
        }

    def convert_answer_dto_to_dict(self, answer_dto, users_dict,
                                   comments_details_dto):
        answer_dict = None
        is_answer_dto_exist = answer_dto != None
        if is_answer_dto_exist:
            for comment in comments_details_dto:
                is_same_comment_id = \
                    comment.comment_dto.comment_id == answer_dto.comment_id
                if is_same_comment_id:
                    answer_dict = self.convert_comment_dto_to_dict(
                        comment, users_dict)
                    if comment.comment_dto.approved_by_id != None:
                        answer_dict.update({
                                "approved_by": users_dict[
                                    comment.comment_dto.approved_by_id]
                            })
                    else:
                        answer_dict.update({
                                "approved_by": None
                            })
                    answer = comment

                # answer_dict, answer = self.update_with_approved_by(answer_dto, users_dict,
                #                                       comment)
            comments_details_dto.remove(answer)

        return answer_dict

    # def update_with_approved_by(self, answer_dto, users_dict, comment):
    #     answer_dict = None
    #     is_same_comment_id = \
    #         comment.comment_dto.comment_id == answer_dto.comment_id
    #     if is_same_comment_id:
    #         answer_dict = self.convert_comment_dto_to_dict(
    #             comment, users_dict)
    #         if comment.comment_dto.approved_by_id != None:
    #             answer_dict.update({
    #                     "approved_by": users_dict[
    #                         comment.comment_dto.approved_by_id]
    #                 })
    #         else:
    #             answer_dict.update({
    #                     "approved_by": None
    #                 })
    #         answer = comment
    #     return answer_dict, answer


    def convert_comment_dto_to_dict(self, comment, users_dict):
        comment_dto = comment.comment_dto

        return {
            "comment_id": comment_dto.comment_id,
            "content": comment_dto.content,
            "commented_at": get_datetime(comment_dto.commented_at),
            "comemnted_by": users_dict[comment_dto.user_id],
            "is_reacted": comment.is_user_reacted,
            "reactions_count": comment.reactions_count,
            "replies_count": comment.replies_count,
            "replies": [self.get_reply_dict(reply_dto, users_dict)
                        for reply_dto in comment.replies_dto]
        }

    @staticmethod
    def get_reply_dict(reply_dto, users_dict):
        return {
            "comemnt_id": reply_dto.reply_dto.comment_id,
            "content": reply_dto.reply_dto.content,
            "commented_at": get_datetime(reply_dto.reply_dto.commented_at),
            "commented_by": users_dict[reply_dto.reply_dto.user_id],
            "reactions_count": reply_dto.reactions_count,
            "is_reacted": reply_dto.is_user_reacted
        }

    # get_domains_posts
    def get_domain_posts_response(
            self, presenter_domain_posts_dto: PresenterDomainPostsDto):
        domain_posts_details_dto = \
            presenter_domain_posts_dto.domain_posts_details_dto
        posts_details_with_metrics_dto = \
            presenter_domain_posts_dto.posts_details_with_metrics_dto

        domains_dto = domain_posts_details_dto.domains_dto
        domains_dict = self.convert_all_domains_dto_to_dict(domains_dto)

        users_dto = domain_posts_details_dto.users_dto
        users_dict = self.convert_all_users_dto_to_dict(users_dto)

        tags_dto = domain_posts_details_dto.tags_dto

        posts_dto = domain_posts_details_dto.posts_dto
        all_posts_list = []
        for post_dto in posts_dto:
            post_dict = self.get_post_details(post_dto, users_dict,
                domains_dict, posts_details_with_metrics_dto, tags_dto)
            all_posts_list.append(post_dict)

        return all_posts_list

    def convert_all_domains_dto_to_dict(self, domains_dto):
        domains_dict = {}
        for domain_dto in domains_dto:
            domains_dict[domain_dto.domain_id] = \
                self.convert_domain_dto_to_dict(domain_dto)
        return domains_dict

    def get_post_details(self, post_dto, users_dict,
                domains_dict, posts_details_with_metrics_dto, tags_dto):

        for post_metric_dto in posts_details_with_metrics_dto:

            is_same_post_id = post_dto.post_id == post_metric_dto.post_id

            if is_same_post_id:
                post_complete_dict = self.get_post_complete_dict(
                    post_dto, users_dict, domains_dict, post_metric_dto,
                    tags_dto)
        return post_complete_dict

    def get_post_complete_dict(self, post_dto, users_dict, domains_dict,
                               post_metric_dto, tags_dto):

        comments_details_dto = post_metric_dto.parent_comments_with_replies_dto
        post_id = post_dto.post_id

        post_complete_dict = {
            "post_id": post_id,
            "posted_by": users_dict[post_dto.user_id],
            "title": post_dto.title,
            "description": post_dto.description,
            "posted_at": get_datetime(post_dto.posted_at),
            "tags": [self.convert_tag_dto_to_dict(tag_dto)
                     for tag_dto in tags_dto if tag_dto.post_id == post_id],
            "comments_count": post_metric_dto.comments_count,
            "reactions_count": post_metric_dto.post_reactions_count,
            "domain": domains_dict[post_dto.domain_id],
            "is_reacted": post_metric_dto.is_user_reacted,
            "approved_answer": self.convert_answer_dto_to_dict(
                post_metric_dto.approved_answer_dto, users_dict,
                comments_details_dto),
            "latest_comments": [self.convert_comment_dto_to_dict(
                comment, users_dict) for comment in comments_details_dto]
        }
        return post_complete_dict


    # gyaan/v2
    def raise_exception_for_invalid_post_ids(self,
                                             invalid_post_ids: List[int]):
        pass

    def get_posts_response(self, completed_post_details: CompletePostDetails):
        pass

    def raise_exception_for_invalid_domain_id_v2(self,
                                                 invalid_domain_id: int):
        pass

    def get_domain_posts_response_v2(self, domain_post_details_dtos):
        pass

    def raise_exception_for_user_not_domain_member(self):
        pass

    def raise_exception_for_invalid_offset(self):
        pass

    def raise_exception_for_invalid_limit(self):
        pass

    def get_domain_details_response(
            self, domain_details_dto: DomainDetailsDTO):
        pass

    def get_domain_with_posts_response(
            self, domain_with_posts_response: DomainDetailsWithPosts):
        pas