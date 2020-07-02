import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec

from gyaan.exceptions.custom_exceptions import InvalidPostId, InvalidCommentId
from gyaan.interactors.create_reaction_interactor \
    import CreateReactionInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface

def test_create_reaction_to_post_with_valid_details():
    # Arrange
    user_id = 1
    entity_id = 1
    entity_type = "post"
    true = True

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateReactionInteractor(
        storage=storage,
        presenter=presenter
    )
    storage.validate_post_id.return_value = true

    # Act
    interactor.create_reaction(
        user_id=user_id, entity_type=entity_type, entity_id=entity_id
    )

    # Assert
    storage.validate_post_id.assert_called_once_with(
        post_id=entity_id
    )
    storage.create_reaction_to_post.assert_called_once_with(
        user_id=user_id,
        entity_id=entity_id,
    )


def test_create_reaction_to_comment_with_valid_details():
    # Arrange
    user_id = 1
    entity_id = 1
    entity_type = "comment"
    true = True

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateReactionInteractor(
        storage=storage,
        presenter=presenter
    )
    storage.validate_comment_id.return_value = true

    # Act
    interactor.create_reaction(
        user_id=user_id, entity_type=entity_type, entity_id=entity_id
    )

    # Assert
    storage.validate_comment_id.assert_called_once_with(
        comment_id=entity_id
    )
    storage.create_reaction_to_comment.assert_called_once_with(
        user_id=user_id,
        entity_id=entity_id
    )


def test_create_reaction_to_post_with_invalid_post_id_raises_exception():
    # Arrange
    user_id = 1
    entity_type = "post"
    entity_id = 10
    false = False

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateReactionInteractor(
        storage=storage,
        presenter=presenter
    )
    storage.validate_post_id.return_value = false
    presenter.raise_exception_for_invalid_post_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.create_reaction(user_id=user_id,
                                         entity_type=entity_type,
                                         entity_id=entity_id)

    # Assert
    storage.validate_post_id.assert_called_once_with(post_id=entity_id)
    presenter.raise_exception_for_invalid_post_id.assert_called_once()


def test_create_reaction_to_comment_with_invalid_comment_id_raises_exception():
    # Arrange
    user_id = 1
    entity_type = "comment"
    entity_id = 10
    false = False

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateReactionInteractor(
        storage=storage,
        presenter=presenter
    )
    storage.validate_comment_id.return_value = false
    presenter.raise_exception_for_invalid_comment_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.create_reaction(user_id=user_id,
                                         entity_type=entity_type,
                                         entity_id=entity_id)

    # Assert
    storage.validate_comment_id.assert_called_once_with(comment_id=entity_id)
    presenter.raise_exception_for_invalid_comment_id.assert_called_once()
