import pytest

from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound

from gyaan.interactors.create_post_interactor import CreatePostInteractor
from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface

def test_create_post_interactor_with_valid_details():
    # Arrange
    user_id = 1
    title = "First post"
    description = "dummmy post"
    tag_ids = [1,2,3,4]
    domain_id = 1
    true = True

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = CreatePostInteractor(
        post_storage=post_storage,
        post_presenter=post_presenter
    )
    post_storage.validate_domain_id.return_value = true

    # Act
    interactor.create_post(user_id=user_id, title=title,
                           description=description,
                           domain_id=domain_id,
                           tag_ids=tag_ids)

    # Assert
    post_storage.create_post.assert_called_once_with(
        user_id=user_id, title=title,
        description=description,
        domain_id=domain_id,
        tag_ids=tag_ids
    )

def test_create_post_with_invalid_domian_id_raises_exception():
    # Arrange
    user_id = 1
    title = "First post"
    description = "dummmy post"
    tag_ids = [1,2,3,4]
    domain_id = 10
    false = False

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = CreatePostInteractor(
        post_storage=post_storage,
        post_presenter=post_presenter
    )
    post_storage.validate_domain_id.return_value = false
    post_presenter.raise_exception_for_invalid_domain_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.create_post(
            user_id=user_id, title=title, description=description,
            domain_id=domain_id, tag_ids=tag_ids)

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    post_presenter.raise_exception_for_invalid_domain_id.assert_called_once()
