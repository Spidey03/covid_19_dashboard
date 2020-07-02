import pytest
from unittest.mock import create_autospec

from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.mixin_interactor \
    import DomainValidationMixin, InvalidDomainId
from gyaan.interactors.storages.dtos_v3 import DomainDetailsDTO
from gyaan.interactors.get_domain_details_v2 import DomainDetailsInteractor

from gyaan.exceptions.custom_exceptions import UserNotDomainMember

def test_get_domain_detials_with_invalid_domain_id():
    # Arrange
    domain_id = 1
    user_id = 1
    false = False

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = DomainDetailsInteractor(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = false
    post_presenter.raise_exception_for_invalid_domain_id_v2.return_value = \
        domain_id

    # Act
    interactor.get_domain_details_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    post_presenter.raise_exception_for_invalid_domain_id_v2(
        invalid_domain_id=domain_id)

def test_get_domain_posts_with_invalid_user_raises_user_not_member_exception():
    # Arrange
    user_id = 1
    domain_id = 1
    false = False
    true = True
    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = DomainDetailsInteractor(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = true
    post_storage.is_user_following_domain.return_value = false

    # Act
    interactor.get_domain_details_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id)
    post_presenter.raise_exception_for_user_not_domain_member.assert_called_once()

def test_domain_detials_with_valid_details(
        user_dtos, domain_dtos, domain_stats_dtos,
        domain_join_requests_dtos):
    # Arraneg
    user_id = 1
    domain_id = 1
    domain_expert_ids = [1]
    domain_experts = user_dtos[0]
    requested_users = user_dtos[1]
    true = True

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = DomainDetailsInteractor(post_storage=post_storage)

    post_storage.validate_domain_id.return_value = true
    post_storage.is_user_following_domain.return_value = true
    post_storage.get_domain.return_value = domain_dtos[0]
    post_storage.get_domain_stats.return_value = domain_stats_dtos[0]
    post_storage.get_domain_expert_ids.return_value = domain_expert_ids
    post_storage.get_users_details.side_effect = \
        [domain_experts, requested_users]
    post_storage.is_user_domain_expert.return_value = true
    post_storage.get_domain_join_requests.return_value = \
        domain_join_requests_dtos

    # Act
    interactor.get_domain_details_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        post_presenter=post_presenter
    )

    # Assert
    post_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id)
    post_storage.is_user_following_domain.assert_called_once_with(
        user_id, domain_id)
    post_storage.get_domain.assert_called_once_with(domain_id)
    post_storage.get_domain_stats.assert_called_once_with(
        domain_id)
    post_storage.get_domain_expert_ids.assert_called_once_with(
        domain_id)
    users_output = post_storage.get_users_details.call_args_list
    post_storage.get_users_details.assert_has_calls(users_output)
    post_storage.is_user_domain_expert.assert_called_once_with(
        user_id, domain_id)
    post_storage.get_domain_join_requests.assert_called_once_with(
        domain_id)