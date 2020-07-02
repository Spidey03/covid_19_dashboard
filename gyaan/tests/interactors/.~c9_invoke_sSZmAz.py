from unittest.mock import create_autospec, patch
import pytest

from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.get_domain_posts_v2 import \
    GetDomainPostsInteractor
from gyaan.interactors.get_posts_v2 import GetPosts
from gyaan.exceptions.custom_exceptions import InvalidLimit, InvalidOffset

def test_get_domain_posts_with_invalid_domain_id():
    # Arrange
    user_id = 1
    domain_id = 1
    false = False
    offset = 0
    limit = 5

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = GetDomainPostsInteractor(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = false
    post_presenter \
        .raise_exception_for_invalid_domain_id_v2.return_value = domain_id

    # Act
    interactor.get_domain_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id)
    actual_output = post_presenter \
        .raise_exception_for_invalid_domain_id_v2.call_args.kwargs
    assert actual_output['invalid_domain_id'] == domain_id


def test_get_domain_posts_with_invalid_offset_raises_exception():
    # Arrange
    user_id = 1
    domain_id = 1
    false = False
    true = True
    offset = -1
    limit = 5

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = GetDomainPostsInteractor(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = true

    # Act
    interactor.get_domain_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id)
    post_presenter.raise_exception_for_invalid_offset.assert_called_once()


def test_get_domain_posts_with_invalid_limit_raises_exception():
    # Arrange
    user_id = 1
    domain_id = 1
    false = False
    true = True
    offset = 5
    limit = -1

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = GetDomainPostsInteractor(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = true

    # Act
    interactor.get_domain_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id)
    post_presenter.raise_exception_for_invalid_limit.assert_called_once()


def test_get_domain_posts_with_invalid_user_raises_user_not_member_exception():
    # Arrange
    user_id = 1
    domain_id = 1
    false = False
    true = True
    offset = 5
    limit = 5

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = GetDomainPostsInteractor(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = true
    post_storage.is_user_following_domain.return_value = false

    # Act
    interactor.get_domain_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id)
    post_presenter.raise_exception_for_user_not_domain_member.assert_called_once()


@patch.object(GetPosts, 'get_posts_details')
def test_get_domain_posts_with_valid_details(get_posts_details_mock):
    # Arrange
    user_id = 1
    domain_id = 1
    true = True
    offset = 5
    limit = 5
    domain_post_details_dtos = []
    post_ids = [1,2,3]

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = GetDomainPostsInteractor(post_storage=post_storage)
    get_posts_details_mock.return_value = domain_post_details_dtos

    post_storage.validate_domain_id.return_value = true
    post_storage.is_user_following_domain.return_value = true
    post_storage.get_domain_post_ids.return_value = post_ids

    # Act
    interactor.get_domain_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    post_storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id,
        domain_id=domain_id
    )
    post_storage.get_domain_post_ids.assert_called_once_with(
        domain_id=domain_id,
        offset=offset,
        limit=limit
    )
    get_posts_details_mock.assert_called_once_with(
        user_id=user_id,
        post_ids=post_ids
    )
    post_presenter.get_domain_posts_response_v2.assert_called_once_with(
        domain_post_details_dtos=domain_post_details_dtos
    )
