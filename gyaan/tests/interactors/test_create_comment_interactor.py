import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec

from gyaan.exceptions.custom_exceptions import InvalidPostId, InvalidCommentId
from gyaan.interactors.create_comment_interactor \
    import CreateCommentInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface

def test_create_comment_to_post_with_valid_details():
    # Arrange
    user_id = 1
    entity_id = 1
    entity_type = "post"
    content = "Comment Content"
    true = True

    storage = create_autospec(StorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = CreateCommentInteractor(
        storage=storage,
        post_presenter=post_presenter
    )
    storage.validate_post_id.return_value = true

    # Act
    interactor.create_comment(
        user_id=user_id, entity_type=entity_type, entity_id=entity_id,
        content=content
    )

    # Assert
    storage.validate_post_id.assert_called_once_with(
        post_id=entity_id
    )
    storage.create_comment_to_post.assert_called_once_with(
        user_id=user_id,
        entity_id=entity_id,
        content=content
    )


def test_create_reply_to_comment_with_valid_details():
    # Arrange
    user_id = 1
    entity_id = 1
    entity_type = "comment"
    content = "reply Content"
    true = True

    storage = create_autospec(StorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = CreateCommentInteractor(
        storage=storage,
        post_presenter=post_presenter
    )
    storage.validate_comment_id.return_value = true

    # Act
    interactor.create_comment(
        user_id=user_id, entity_type=entity_type, entity_id=entity_id,
        content=content
    )

    # Assert
    storage.validate_comment_id.assert_called_once_with(
        comment_id=entity_id
    )
    storage.create_reply_to_comment.assert_called_once_with(
        user_id=user_id,
        entity_id=entity_id,
        content=content
    )


def test_create_comment_to_post_with_invalid_post_id_raises_exception():
    # Arrange
    user_id = 1
    entity_type = "post"
    entity_id = 10
    content = "Comment Content"
    false = False

    storage = create_autospec(StorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = CreateCommentInteractor(
        storage=storage,
        post_presenter=post_presenter
    )
    storage.validate_post_id.return_value = false
    post_presenter.raise_exception_for_invalid_post_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.create_comment(user_id=user_id,
                                         entity_type=entity_type,
                                         entity_id=entity_id,
                                         content=content)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=entity_id)
    post_presenter.raise_exception_for_invalid_post_id.assert_called_once()


def test_create_reply_to_comment_with_invalid_comment_id_raises_exception():
    # Arrange
    user_id = 1
    entity_type = "comment"
    entity_id = 10
    content = "reply Content"
    false = False

    storage = create_autospec(StorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = CreateCommentInteractor(
        storage=storage,
        post_presenter=post_presenter
    )
    storage.validate_comment_id.return_value = false
    post_presenter.raise_exception_for_invalid_comment_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.create_comment(user_id=user_id,
                                         entity_type=entity_type,
                                         entity_id=entity_id,
                                         content=content)

    # Assert
    storage.validate_comment_id.assert_called_once_with(comment_id=entity_id)
    post_presenter.raise_exception_for_invalid_comment_id.assert_called_once()
