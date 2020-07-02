from unittest.mock import create_autospec, patch
import pytest

from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.domain_with_posts import \
    DomainWithPosts
from gyaan.interactors.get_domain_details_v2 import DomainDetailsInteractor
from gyaan.interactors.get_domain_posts_v2 import GetDomainPostsInteractor
from gyaan.exceptions.custom_exceptions import InvalidLimit, InvalidOffset
from gyaan.interactors.storages.dtos_v3 import DomainDetailsWithPosts

def test_get_domain_with_posts_with_invalid_domain_id():
    # Arrange
    user_id = 1
    domain_id = 1
    false = False
    offset = 0
    limit = 5

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = DomainWithPosts(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = false
    post_presenter \
        .raise_exception_for_invalid_domain_id_v2.return_value = domain_id

    # Act
    interactor.domain_with_posts_wrapper(
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

def test_get_domain_with_posts_invalid_user_raises_user_not_member_exception():
    # Arrange
    user_id = 1
    domain_id = 1
    false = False
    true = True
    offset = 5
    limit = 5

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = DomainWithPosts(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = true
    post_storage.is_user_following_domain.return_value = false

    # Act
    interactor.domain_with_posts_wrapper(
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


@patch.object(DomainDetailsInteractor, 'get_domain_details')
@patch.object(GetDomainPostsInteractor, 'get_domain_posts')
def test_get_domain_with_posts_with_valid_details(
        domain_posts_mock, domain_details_mock):
    # Arrange
    user_id = 1
    domain_id = 1
    true = True
    offset = 5
    limit = 5
    domain_with_posts_response = DomainDetailsWithPosts(
        post_details=[], domain_details=[])

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = DomainWithPosts(post_storage=post_storage)

    domain_details_mock.return_value = []
    domain_posts_mock.return_value = []

    post_storage.validate_domain_id.return_value = true
    post_storage.is_user_following_domain.return_value = true
    post_presenter.get_domain_with_posts_response.return_value = \
        domain_with_posts_response

    # Act
    interactor.domain_with_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        post_presenter=post_presenter
    )

    # Assert
    # post_storage.validate_domain_id.assert_called_once_with(
    #     domain_id=domain_id
    # )
    post_presenter.get_domain_with_posts_response.assert_called_once_with(
        domain_with_posts_response)
