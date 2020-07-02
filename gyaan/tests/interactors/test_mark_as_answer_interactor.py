import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec

from gyaan.exceptions.custom_exceptions import InvalidPostId, InvalidCommentId
from gyaan.interactors.mark_as_answer_interactor \
    import MarkAsAnswerInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_mark_as_answer_with_valid_details():
    # Arrange
    user_id = 1
    comment_id = 1
    true = True

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MarkAsAnswerInteractor(
        storage=storage,
        presenter=presenter
    )
    storage.validate_comment_id.return_value = true

    # Act
    interactor.mark_as_answer(user_id=user_id, comment_id=comment_id)

    # Assert
    storage.validate_comment_id.assert_called_once_with(
        comment_id=comment_id
    )
    storage.mark_as_answer.assert_called_once_with(
        user_id=user_id, comment_id=comment_id
    )

def test_mark_as_answer_with_invalid_comment_id_raises_exception():
    # Arrange
    user_id = 1
    comment_id = 10
    false = False

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MarkAsAnswerInteractor(
        storage=storage,
        presenter=presenter
    )
    storage.validate_comment_id.return_value = false
    presenter.raise_exception_for_invalid_comment_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.mark_as_answer(
            user_id=user_id, comment_id=comment_id
        )

    # Assert
    storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
    presenter.raise_exception_for_invalid_comment_id.assert_called_once()
