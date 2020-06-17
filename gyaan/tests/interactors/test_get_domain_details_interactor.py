import pytest
from mock import create_autospec
from gyaan.interactors.get_domain_details_interactor \
    import GetDomainDetailsInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import DomainDetailsDto
from gyaan.exceptions.exceptions \
    import DomainNotExists, UserIsNotFollwerOfDomain
from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden


class TestGetDomainDetails():

    def test_when_domain_not_exists_raise_exception_domain_not_exist(self):
        # Arrange
        user_id, domain_id = 5, 3

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.get_domain_details.side_effect = DomainNotExists
        presenter.raise_domain_does_not_exists.side_effect = NotFound
        interactor = GetDomainDetailsInteractor(storage=storage)

        # Act
        with pytest.raises(NotFound):
            interactor.get_domain_details_wrapper(user_id=user_id,
                domain_id=domain_id, presenter=presenter)

        # Assert
        storage.get_domain_details.assert_called_once_with(domain_id=domain_id)


    def test_when_user_is_not_follower_raise_exception_user_is_not_follower_exception(
            self, domain_dto):
        # Arrange
        user_id, domain_id = 1, 1

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.get_domain_details.return_value = domain_dto
        storage.check_user_is_follower_of_domain.return_value = False
        presenter.raise_user_not_follower.side_effect = Forbidden
        interactor = GetDomainDetailsInteractor(storage=storage)

        # Act
        with pytest.raises(Forbidden):
            interactor.get_domain_details_wrapper(user_id=user_id,
                domain_id=domain_id, presenter=presenter)

        # Assert
        storage.get_domain_details.assert_called_once_with(
            domain_id=domain_id)
        storage.check_user_is_follower_of_domain.assert_called_once_with(
            user_id, domain_id)

    def test_when_valid_details_given(self, domain_dto, domain_stats,
            experts, domain_join_requests, requested_users,
            response_get_domain_details):
        # Arrange
        user_id, domain_id = 1, 1
        expert_ids = [1,2]

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        is_user_domain_expert = True
        expected_output = response_get_domain_details
        storage.get_domain_details.return_value = domain_dto
        storage.check_user_is_follower_of_domain.return_value = True
        storage.get_domain_stats.return_value = domain_stats
        storage.get_domain_expert_ids.return_value = expert_ids
        storage.get_users_details.return_value = experts
        storage.is_user_domain_expert.return_value = is_user_domain_expert
        storage.get_domain_join_request.return_value = domain_join_requests
        storage.get_users_details.return_value = requested_users
        presenter.get_response_for_domain_details.return_value = expected_output
        domain_details_dto = DomainDetailsDto(
            domain=domain_dto,
            domain_stats=domain_stats,
            domain_experts=experts,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            requested_users_dto=requested_users
        )
        interactor = GetDomainDetailsInteractor(storage=storage)

        # Act
        output = interactor.get_domain_details_wrapper(user_id=user_id,
            domain_id=domain_id, presenter=presenter)

        # Assert
        storage.get_domain_details.assert_called_once_with(
            domain_id=domain_id)
        storage.check_user_is_follower_of_domain.assert_called_once_with(
            user_id, domain_id)
        storage.get_domain_stats.assert_called_once_with(domain_id=domain_id)
        storage.get_domain_expert_ids.assert_called_once_with(domain_id=domain_id)
        storage.get_domain_join_request.assert_called_once_with(domain_id=domain_id)
        assert storage.get_users_details.call_count == 2
        assert output == expected_output