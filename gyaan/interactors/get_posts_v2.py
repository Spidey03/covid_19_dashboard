from typing import List

from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.storages.dtos_v3 import *

class InvalidPostIds(Exception):
    def __init__(self, invalid_post_ids: List[int]):
        self.invalid_post_ids = invalid_post_ids


class GetPosts:

    def __init__(self, post_storage: PostPresenterInterface):
        self.post_storage = post_storage

    def get_posts_wrapper(self, user_id: int, post_ids: List[int],
                          post_presenter: PostPresenterInterface):
        try:
            return self.get_posts_response(
                user_id=user_id,
                post_ids=post_ids,
                post_presenter=post_presenter
            )
        except InvalidPostIds as err:
            invalid_post_ids = err.invalid_post_ids
            post_presenter.raise_exception_for_invalid_post_ids(
                invalid_post_ids=invalid_post_ids
            )

    def get_posts_response(self,user_id: int, post_ids: List[int],
                          post_presenter: PostPresenterInterface):
        # completed_post_details = self.get_posts(post_ids=post_ids)

        completed_post_details = self.get_posts_details(
            user_id=user_id,
            post_ids=post_ids
        )

        return post_presenter.get_posts_response(completed_post_details)

    def get_posts_details(self, user_id: int, post_ids: List[int]):

        post_ids = self._get_unique_post_ids(post_ids)
        self._validate_post_ids(post_ids=post_ids)

        # TODO: get post details given post ids
        post_dtos = self.post_storage.get_post_details(
            post_ids=post_ids
        )

        # TODO: get post tags
        post_tag_details = self.post_storage.get_post_tag_dtos(
            post_ids=post_ids
        )
        # TODO: get post reactions count
        post_reaction_counts = self.post_storage.get_post_reactions_count(
            post_ids=post_ids)

        # TODO: get post comments count
        post_comment_counts = self.post_storage.get_post_comments_count(
            post_ids=post_ids)


        # TODO: get latest comments given comment ids
        comment_ids = self.post_storage \
            .get_latest_comments_ids_with_approved_comment_id(
                post_ids=post_ids
            )
        comment_dtos = self.post_storage.get_comment_dtos(
            comment_ids=comment_ids
        )

        # TODO: get lateset comments reactions count
        comment_reaction_counts = \
            self.post_storage.get_comment_reactions_count(
                comment_ids=comment_ids)

        # TODO: get replies comments count
        comment_replies_counts = self.post_storage.get_comment_replies_count(
            comment_ids=comment_ids)

        # TODO: get user dtos
        user_ids = [post_dto.posted_by_id for post_dto in post_dtos]
        user_ids += [
            comment_dto.commented_by_id
            for comment_dto in comment_dtos
        ]
        user_ids = list(set(user_ids))
        user_dtos = self.post_storage.get_user_dtos(user_ids=user_ids)

        return  CompletePostDetails(
            post_dtos=post_dtos,
            post_reaction_counts=post_reaction_counts,
            comment_counts=post_comment_counts,
            comment_reaction_counts=comment_reaction_counts,
            reply_counts=comment_replies_counts,
            comment_dtos=comment_dtos,
            post_tag_ids=post_tag_details.post_tag_ids,
            tags=post_tag_details.tags,
            users_dtos=user_dtos
        )

    # TODO: validate unique post ids from database
    def _validate_post_ids(self, post_ids):
        valid_post_ids = self.post_storage.get_valid_post_ids(post_ids)

        invalid_post_ids = [
            post_id
            for post_id in post_ids if post_id not in valid_post_ids
        ]

        if invalid_post_ids:
            raise InvalidPostIds(invalid_post_ids=invalid_post_ids)


    # TODO: get unique post ids
    @staticmethod
    def _get_unique_post_ids(post_ids: List[int]):
        return list(set(post_ids))


        # # TODO: get approved answers given post ids
        # post_approved_comment_ids = \
        #     self.post_storage.get_post_approved_answer_ids(
        #         post_ids=post_ids)
        # post_approved_comment_dtos = \
        #     self.post_storage.get_post_approved_answer_dtos(
        #         post_approved_comment_ids=post_approved_comment_ids
        #     )

        # # TODO: check is user reacted to post or not
        # is_user_reacted_to_posts = \
        #     self.post_storage.get_user_reaction_status(post_ids=post_ids)