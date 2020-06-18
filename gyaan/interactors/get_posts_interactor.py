from typing import List
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import CompletePostDetailsDto
from gyaan.exceptions.exceptions import InvalidPostIdsException

class GetPostsInteractor:

    def __init__(self, storage=StorageInterface):

        self.storage = storage

    def get_posts_wrapper(self, post_ids: List[int], presenter: PresenterInterface):

        try:
            complete_post_details_dto = self.get_posts(post_ids)
            return presenter.response_get_posts(complete_post_details_dto)
        except InvalidPostIdsException:
            raise presenter.raise_invalid_post_ids_exception()

    def get_posts(self, post_ids: List[int]):
        
        # TODO: VALIDATE POST IDS
        valid_post_ids = self.storage.get_valid_post_ids(post_ids)
        invalid_post_ids = list(set(post_ids) - set(valid_post_ids))
        if invalid_post_ids:
            raise InvalidPostIdsException(invalid_post_ids)

        return self._get_posts_details(valid_post_ids)


    def _get_posts_details(self, post_ids: int):

        post_dtos = self.storage.get_post_details(post_ids=post_ids)
        post_tag_details_dtos = self.storage.get_posts_tags(post_ids=post_ids)
        post_reaction_count_dtos = \
            self.storage.get_post_reactions_count(post_ids=post_ids)
        post_comment_count_dtos = \
            self.storage.get_post_comments_count(post_ids=post_ids)

        comment_ids = self._get_posts_latest_comments(post_ids=post_ids)
        comment_reactions_count_dtos = \
            self.storage.get_comments_reactions_count(comment_ids=comment_ids)
        comment_replies_count_dtos = \
            self.storage.get_comments_replies_count(comment_ids=comment_ids)
        comment_dtos = self.storage.get_comments(comment_ids=comment_ids)

        user_ids = [post.posted_by for post in post_dtos]
        user_ids += [comment.commented_by for comment in comment_dtos]
        user_unique_ids = list(set(user_ids))
        user_unique_ids.sort()
        user_dtos = self.storage.get_users_details(ids=user_unique_ids)

        return CompletePostDetailsDto(
            post_dtos=post_dtos,
            post_reaction_counts=post_reaction_count_dtos,
            comment_counts=post_comment_count_dtos,
            comment_reaction_counts=comment_reactions_count_dtos,
            reply_counts=comment_replies_count_dtos,
            comment_dtos=comment_dtos,
            post_tag_details=post_tag_details_dtos,
            users_dtos=user_dtos
        )

    def _get_posts_latest_comments(self, post_ids: List[int]):

        limit = 2
        comment_ids = self.storage.get_posts_latest_comments(
            post_ids=post_ids, limit=limit)
        return comment_ids