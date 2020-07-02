from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound

from gyaan.constants.exception_messages import (
    INVALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_POST_ID,
    INVALID_COMMENT_ID,
    INVALID_DOMAIN_ID
)
from gyaan.interactors.storages.dtos import (
    PostsCompleteDto
)
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface

from gyaan.interactors.storages.dtos import *
import pytest
from gyaan.tests.presenters.conftest import *

class PresenterImplementaion(PresenterInterface):

    def raise_invalid_username_exception(self):
        raise NotFound(*INVALID_USERNAME)

    def raise_invalid_password_exception(self):
        raise NotFound(*INVALID_PASSWORD)

    def raise_exception_for_invalid_post_id(self):
        raise NotFound(*INVALID_POST_ID)

    def raise_exception_for_invalid_comment_id(self):
        raise NotFound(*INVALID_COMMENT_ID)

    def raise_exception_for_invalid_domain_id(self):
        raise NotFound(*INVALID_DOMAIN_ID)

    def sign_in_response(self, user_auth_tokens_dto):
        response = {
            "user_id": user_auth_tokens_dto.user_id,
            "access_token": user_auth_tokens_dto.access_token,
            "refresh_token": user_auth_tokens_dto.refresh_token,
            "expires_in": str(user_auth_tokens_dto.expires_in)
        }
        return response

    # get_user_metrics_response
    def get_user_metrics_response(self, user_domain_post_metrics_dto):
        user_dto = user_domain_post_metrics_dto.user_dto
        following_domain_dtos = user_domain_post_metrics_dto.following_domain_dtos
        suggested_domain_dtos = user_domain_post_metrics_dto.suggested_domain_dtos
        user_post_metrics_dto = user_domain_post_metrics_dto.user_post_metrics_dto
        pending_post_metrics_dto = user_domain_post_metrics_dto.pending_post_metrics_dto

        response_dict = {
            "user": self.get_user_dict(user_dto),
            "following_domains": self._get_following_domains_list(
                following_domain_dtos),
            "suggested_domains": self._get_suggested_domain_list(
                suggested_domain_dtos),
            "user_post_metrics": self._get_user_post_metrics_dict(
                user_post_metrics_dto),
            "pending_post_metrics": self._get_pending_post_metrics_dict(
                pending_post_metrics_dto)
        }
        return response_dict

    @staticmethod
    def _get_pending_post_metrics_dict(pending_post_metrics_dto):
        user_post_metrics_dict = {
            "total_review_posts": pending_post_metrics_dto.pending_posts_count,
            "pending_for_review": [
                {
                    "domain_id": domain.domain_id,
                    "name": domain.name,
                    "picture": domain.picture,
                    "review_posts_count": domain.posts_count
                } for domain in pending_post_metrics_dto.pending_posts_in_each_domain_dtos
                ]
        }
        return user_post_metrics_dict

    @staticmethod
    def _get_user_post_metrics_dict(user_post_metrics_dto):
        user_post_metrics_dict = {
            "total_posts": user_post_metrics_dto.total_posts,
            "posts_in_each_domain": [
                {
                    "domain_id": domain.domain_id,
                    "name": domain.name,
                    "picture": domain.picture,
                    "posts_count": domain.posts_count
                } for domain in user_post_metrics_dto.posts_in_each_domain_dtos
                ]
        }
        return user_post_metrics_dict

    @staticmethod
    def _get_suggested_domain_list(suggested_domain_dtos):

        suggested_domains = [
            {
                "domain_id": domain.domain_dto.domain_id,
                "name": domain.domain_dto.name,
                "picture": domain.domain_dto.picture,
                "follow_request": domain.is_requested
            } for domain in suggested_domain_dtos
            ]
        return suggested_domains


    @staticmethod
    def _get_following_domains_list(following_domain_dtos):

        following_domains = [
            {
                "domain_id": domain.domain_id,
                "name": domain.name,
                "picture": domain.picture
            } for domain in following_domain_dtos
            ]
        return following_domains

    # get_posts_interactor_response

    def get_posts_response(self, all_posts_details_dto: PostsCompleteDto):
        posts_details_response_list = []
        post_complete_details_dtos = all_posts_details_dto.posts_dtos
        for post_complete_dto in post_complete_details_dtos:
            posts_details_response_list.append(
                    self.get_post_complete_dict(post_complete_dto)
                )
        return posts_details_response_list


    def get_post_complete_dict(self, post_complete_dto):
        post_dto = post_complete_dto.post_dto
        print(post_dto)
        print(post_complete_dto)
        post_complete_dict = {
            "post_id": post_dto.post_id,
            "posted_by": self.get_user_dict(post_dto.posted_by),
            "title": post_dto.title,
            "description": post_dto.description,
            "posted_at": str(post_dto.posted_at),
            "tags": post_dto.tags,
            "comments_count": post_dto.comments_count,
            "reactions_count": post_dto.reactions_count,
            "domain": self.get_domain_dict(post_dto.domain),
            "is_reacted": post_complete_dto.is_reacted,
            "latest_comments": [self.get_comment_dict(comment_dto) for
                comment_dto in post_complete_dto.comment_dtos]
        }
        is_post_has_no_answer = post_complete_dto.answer_dto == None
        if is_post_has_no_answer:
            post_complete_dict.update(
                {
                    "approved_answer": None
                }
            )
        else:
            post_complete_dict.update(
                {
                    "approved_answer": self.get_answer_dict(
                post_complete_dto.answer_dto)
                }
            )
        return post_complete_dict

    @staticmethod
    def get_user_dict(user_dto):
        return {
            "user_id": user_dto.user_id,
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic
        }

    @staticmethod
    def get_domain_dict(domain_dto):
        return {
            "domain_id": domain_dto.domain_id,
            "name": domain_dto.name,
            "picture": domain_dto.picture
        }

    def get_answer_dict(self, answer_dto):
        answer_dict = self.get_comment_dict(answer_dto)
        is_answer = answer_dto.approved_by != None
        if is_answer:
            answer_dict.update({
                "approved_by": self.get_user_dict(answer_dto.approved_by)
            })
        else:
            answer_dict.update({
                "approved_by": None
            })

        return answer_dict


    def get_comment_dict(self, comment_dto):
        comment_dict =  {
            "comment_id": comment_dto.comment_id,
            "content": comment_dto.content,
            "commented_at": comment_dto.commented_at,
            "commented_by": self.get_user_dict(comment_dto.commented_by),
            "reactions_count": comment_dto.reactions_count,
            "replies_count": comment_dto.replies_count
        }
        reply_list = []
        for reply_dto in comment_dto.reply_dtos:
            reply_list.append(self.get_reply_dict(reply_dto))
        comment_dict.update(
            {
                "replies": reply_list
            }
            )
        return comment_dict

    def get_reply_dict(self, reply_dto):
        return {
            "comment_id": reply_dto.comment_id,
            "content": reply_dto.content,
            "commented_at": reply_dto.commented_at,
            "commented_by": self.get_user_dict(reply_dto.commented_by),
            "reactions_count": reply_dto.reactions_count
        }

    # Get domain Metrics response

    def get_domain_metrics_response(
            self, domain_expert_details_presenter_dto: DomainExpertDetailsPresenterDto):

        domain_details_dto = \
            domain_expert_details_presenter_dto.domain_details_dto
        domain_expert_details_dto = \
            domain_expert_details_presenter_dto.domain_expert_details_dto
        post_review_requests_dto = domain_expert_details_presenter_dto \
            .post_review_requests_dto
        domain_join_request_details_dtos = domain_expert_details_presenter_dto. \
            domain_join_request_details_dtos

        domain_metrics_response = {
            "domain_id": domain_details_dto.domain_id,
            "name": domain_details_dto.name,
            "picture": domain_details_dto.picture,
            "description": domain_details_dto.description,
            "experts": self._convert_domain_expert_dto_to_dict(
                domain_expert_details_dto),
            "no_of_followers": domain_details_dto.no_of_followers,
            "total_posts": domain_details_dto.total_posts,
            "likes": domain_details_dto.likes,
            "is_following": domain_expert_details_presenter_dto.is_following,
        }
        is_user_expert_for_this_domain = post_review_requests_dto != None
        if is_user_expert_for_this_domain:
            domain_metrics_response.update({
                "domain_expert_metrics": {
                    "post_review_requests": self. \
                        _convert_post_review_requests_dto_to_dict(
                            post_review_requests_dto
                        ),
                    "user_requests": self._convert_requests_dto_to_dict(
                            domain_join_request_details_dtos
                        )

                }
            })
        else:
            domain_metrics_response.update({
                "domain_expert_metrics": None
            })

        return domain_metrics_response


    def _convert_domain_expert_dto_to_dict(self, domain_expert_details_dto):
        return {
            "total_experts": domain_expert_details_dto.total_experts,
            "domain_experts": [self.get_user_dict(userdto) for userdto in \
                domain_expert_details_dto.domain_experts]
        }

    @staticmethod
    def _convert_post_review_requests_dto_to_dict(post_review_requests_dto):
        return {
            "total_posts": post_review_requests_dto.pending_posts_count,
            "pending_for_review": [{
                "domain_id": pending.domain_id,
                "name": pending.name,
                "picture": pending.picture,
                "review_posts_count": pending.posts_count
            } for pending in \
                post_review_requests_dto.pending_posts_in_each_domain_dtos]
        }

    def _convert_requests_dto_to_dict(self, domain_join_request_details_dtos):
        return {
            "total_requests": domain_join_request_details_dtos.requests_count,
            "requests": [self.get_request_user_dict(userdto) for userdto in \
                domain_join_request_details_dtos.domain_join_request_dtos]
        }

    @staticmethod
    def get_request_user_dict(user_dto):
        return {
            "request_id": user_dto.user_id,
            "name": user_dto.name,
            "profile_pic": user_dto.profile_pic
        }
