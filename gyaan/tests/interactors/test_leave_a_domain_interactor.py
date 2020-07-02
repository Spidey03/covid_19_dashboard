import pytest

from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound

from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface
from gyaan.interactors.leave_a_domain_interactor \
    import LeaveDomainInteractor

def test_leave_a_domain_with_valid_details():
    # Arrange
    user_id = 1
    domain_id = 1
    true = True

    domain_storage = create_autospec(DomainStorageInterface)
    domain_presenter = create_autospec(DomainPresenterInterface)
    interactor = LeaveDomainInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    domain_storage.validate_domain_id.return_value = true

    # Act
    interactor.leave_a_domain(user_id=user_id, domain_id=domain_id)

    # Assert
    domain_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    domain_storage.leave_a_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )


def test_leave_a_domain_with_invalid_domain_id_raises_exception():
    # Arrange
    user_id = 1
    domain_id = 10
    false = False

    domain_storage = create_autospec(DomainStorageInterface)
    domain_presenter = create_autospec(DomainPresenterInterface)
    interactor = LeaveDomainInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    domain_storage.validate_domain_id.return_value = false
    domain_presenter.raise_exception_for_invalid_domain_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.leave_a_domain(
            user_id=user_id, domain_id=domain_id
        )

    # Assert
    domain_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id)
    domain_presenter.raise_exception_for_invalid_domain_id.assert_called_once()
