from unittest.mock import create_autospec

import pytest

from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.get_posts_v2 import GetPosts

def test_get_posts_with_invalid_post_ids_return_unique_ids():
    # Arrange
    post_ids = [1,1,1,3,4]
    unique_post_ids = [1,3,4]
    user_id = 1
    valid_post_ids = [1,3]
    invalid_post_ids = [4]

    post_presenter = create_autospec(PostPresenterInterface)
    post_storage = create_autospec(PostStorageInterface)
    interactor = GetPosts(post_storage=post_storage)

    post_storage.get_valid_post_ids.return_value = valid_post_ids

    # Act
    interactor.get_posts_wrapper(
        user_id=user_id,
        post_ids=post_ids,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.get_valid_post_ids.assert_called_once_with(
        post_ids=unique_post_ids
    )
    actual_output = post_presenter.raise_exception_for_invalid_post_ids \
        .call_args.kwargs
    assert actual_output['invalid_post_ids'] == invalid_post_ids


def test_get_posts_with_valid_details(
        user_dtos, post_dtos, comment_dtos_v2, post_tag_details_dtos,
        post_reaction_counts, comment_reaction_counts, post_comment_counts,
        comment_replies_counts
    ):
    # Arrange
    user_id = 1
    post_ids = [1,2,3,4]
    comment_ids = [1,2,3,4]
    user_ids = [1,2]
    presenter_output = {}

    post_presenter = create_autospec(PostPresenterInterface)
    post_storage = create_autospec(PostStorageInterface)
    interactor = GetPosts(post_storage=post_storage)

    post_storage.get_valid_post_ids.return_value = post_ids
    post_storage.get_post_details.return_value = post_dtos
    post_storage.get_post_tag_dtos.return_value = post_tag_details_dtos
    post_storage.get_post_reactions_count.return_value = post_reaction_counts
    post_storage.get_post_comments_count.retun_value = post_comment_counts
    post_storage.get_latest_comments_ids_with_approved_comment_id.return_value = \
        comment_ids
    post_storage.get_comment_dtos.return_value = comment_dtos_v2
    post_storage.get_comment_reactions_count.return_value = \
        comment_reaction_counts
    post_storage.get_comment_replies_count.return_value = \
        comment_replies_counts
    post_storage.get_user_dtos.return_value = user_dtos

    post_presenter.get_posts_response.return_value = presenter_output

    # Act
    actual_output = interactor.get_posts_wrapper(
        user_id=user_id,
        post_ids=post_ids,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.get_valid_post_ids.assert_called_once_with(
        post_ids=post_ids)
    post_storage.get_post_details.assert_called_once_with(
        post_ids=post_ids)
    post_storage.get_post_tag_dtos.assert_called_once_with(
        post_ids=post_ids)
    post_storage.get_post_reactions_count.assert_called_once_with(
        post_ids=post_ids)
    post_storage.get_post_comments_count.assert_called_once_with(
        post_ids=post_ids)
    post_storage.get_latest_comments_ids_with_approved_comment_id \
        .assert_called_once_with(post_ids=post_ids)
    post_storage.get_comment_dtos.assert_called_once_with(
        comment_ids=comment_ids)
    post_storage.get_comment_reactions_count.assert_called_once_with(
        comment_ids=comment_ids)
    post_storage.get_comment_replies_count.assert_called_once_with(
        comment_ids=comment_ids)
    post_storage.get_user_dtos.assert_called_once_with(
        user_ids=user_ids)