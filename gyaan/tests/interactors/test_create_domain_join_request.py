import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec

from gyaan.exceptions.custom_exceptions import InvalidDomainId
from gyaan.interactors.create_domain_join_request_interactor \
    import CreateDomainJoinRequestInteractor
from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface


def test_create_domain_join_request_with_valid_domian_id():
    # Arrange
    user_id = 1
    domain_id = 1
    true = True

    domain_storage = create_autospec(DomainStorageInterface)
    domain_presenter = create_autospec(DomainPresenterInterface)
    interactor = CreateDomainJoinRequestInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )
    domain_storage.validate_domain_id.return_value = true

    # Act
    interactor.create_domain_join_request(
        user_id=user_id, domain_id=domain_id
    )

    # Assert
    domain_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    domain_storage.create_domain_join_request.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )


def test_create_domain_join_request_with_invalid_domian_id_raises_exception():
    # Arrange
    user_id = 1
    domain_id = 1
    false = False

    domain_storage = create_autospec(DomainStorageInterface)
    domain_presenter = create_autospec(DomainPresenterInterface)
    interactor = CreateDomainJoinRequestInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )
    domain_storage.validate_domain_id.return_value = false
    domain_presenter.raise_exception_for_invalid_domain_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.create_domain_join_request(user_id=user_id,
                                                     domain_id=domain_id)

    # Assert
    domain_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    domain_presenter.raise_exception_for_invalid_domain_id.assert_called_once()
