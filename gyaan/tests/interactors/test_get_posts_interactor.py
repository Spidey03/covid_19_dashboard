import pytest
from mock import create_autospec
from gyaan.interactors.get_posts_interactor \
    import GetPostsInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import DomainDetailsDto
from gyaan.exceptions.exceptions \
    import DomainNotExists, UserIsNotFollwerOfDomain
from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden


class TestGetPosts:
    def test_when_invalid_post_ids_given_raise_invalid_posts_ids_exception(self):
        # Arrange
        post_ids = [1,2,3]

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.get_valid_post_ids.return_value = [1,2]
        presenter.raise_invalid_post_ids_exception.side_effect = NotFound
        interactor = GetPostsInteractor(storage=storage)

        # Act
        with pytest.raises(NotFound):
            interactor.get_posts_wrapper(post_ids=post_ids, presenter=presenter)

        # Assert
        storage.get_valid_post_ids.assert_called_once_with(post_ids)

    def test_when_valid_post_ids_given(self, posts, post_tags,
            post_tag_details, post_reaction_counts, post_comment_counts,
            comment_reaction_counts, comment_replies_count, comments, experts,
            response_get_posts, post_complete_details):

        # Arrange
        post_ids, comment_ids, user_ids = [1,2], [1,2], [1,2]
        expected_output = response_get_posts
        users = experts

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.get_valid_post_ids.return_value = post_ids
        storage.get_post_details.return_value = posts
        storage.get_posts_tags.return_value = post_tag_details
        storage.get_post_reactions_count.return_value = post_reaction_counts
        storage.get_post_comments_count.return_value = post_comment_counts
        storage.get_posts_latest_comments.return_value = comment_ids
        storage.get_comments_reactions_count.return_value = comment_reaction_counts
        storage.get_comments_replies_count.return_value = comment_replies_count
        storage.get_comments.return_value = comments
        storage.get_users_details.return_value = users
        presenter.response_get_posts.return_value = response_get_posts

        interactor = GetPostsInteractor(storage=storage)

        # Act
        output = interactor.get_posts_wrapper(post_ids=post_ids, presenter=presenter)

        # Assert
        assert output == expected_output
        storage.get_valid_post_ids.assert_called_once_with(post_ids)
        storage.get_post_details.assert_called_once_with(post_ids)
        storage.get_posts_tags.assert_called_once_with(post_ids)
        storage.get_post_reactions_count.assert_called_once_with(post_ids)
        storage.get_post_comments_count.assert_called_once_with(post_ids)
        storage.get_posts_latest_comments.assert_called_once_with(
            post_ids =post_ids, limit=2)
        storage.get_comments_reactions_count.assert_called_once_with(comment_ids)
        storage.get_comments_replies_count.assert_called_once_with(comment_ids)
        storage.get_comments.assert_called_once_with(comment_ids)
        storage.get_users_details.assert_called_once_with(user_ids)
        presenter.response_get_posts.assert_called_once_with(post_complete_details)
        