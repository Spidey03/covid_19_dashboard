import pytest

from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound

from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.domain_presenter_interface \
    import DomainPresenterInterface
from gyaan.interactors.get_domain_tags_interactor \
    import GetDomainTagsInteractor
from gyaan.interactors.storages.dtos_v2 import TagDto

def test_get_domain_tags_with_valid_domain_id_returns_tags_list():
    # Arrange
    domain_id = 1
    true = True
    storage_response = [
        TagDto(tag_id=1,name="tag1",post_id=None,domain_id=None),
        TagDto(tag_id=2,name="tag2",post_id=None,domain_id=None),
        TagDto(tag_id=3,name="tag3",post_id=None,domain_id=None),
    ]
    expected_output = storage_response

    domain_storage = create_autospec(DomainStorageInterface)
    domain_presenter = create_autospec(DomainPresenterInterface)
    interactor = GetDomainTagsInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    domain_storage.validate_domain_id.return_value = true
    domain_storage.get_domain_tags_dto.return_value = storage_response
    domain_presenter.get_domain_tags_response.return_value = expected_output


    # Act
    actual_output = interactor.get_domain_tags(domain_id=domain_id)

    # Assert
    assert actual_output == expected_output

    domain_storage.get_domain_tags_dto.assert_called_once_with(
        domain_id=domain_id
    )
    domain_presenter.get_domain_tags_response.assert_called_once_with(
        tags_dto=expected_output
    )

def test_get_domain_tags_with_no_tags_in_database_return_empty_list():
    # Arrange
    domain_id = 1
    true = True
    storage_response = []
    expected_output = storage_response

    domain_storage = create_autospec(DomainStorageInterface)
    domain_presenter = create_autospec(DomainPresenterInterface)
    interactor = GetDomainTagsInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    domain_storage.validate_domain_id.return_value = true
    domain_storage.get_domain_tags_dto.return_value = storage_response
    domain_presenter.get_domain_tags_response.return_value = expected_output


    # Act
    actual_output = interactor.get_domain_tags(domain_id=domain_id)

    # Assert
    assert actual_output == expected_output

    domain_storage.get_domain_tags_dto.assert_called_once_with(
        domain_id=domain_id
    )
    domain_presenter.get_domain_tags_response.assert_called_once_with(
        tags_dto=expected_output
    )

def test_get_domain_tags_with_invalid_domain_id_raises_exception():
    # Arrange
    domain_id = 10
    false = False

    domain_storage = create_autospec(DomainStorageInterface)
    domain_presenter = create_autospec(DomainPresenterInterface)
    interactor = GetDomainTagsInteractor(
        domain_storage=domain_storage,
        domain_presenter=domain_presenter
    )

    domain_storage.validate_domain_id.return_value = false
    domain_presenter.raise_exception_for_invalid_domain_id.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        assert interactor.get_domain_tags(domain_id=domain_id)

    # Assert
    domain_storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id)
    domain_presenter.raise_exception_for_invalid_domain_id.assert_called_once()