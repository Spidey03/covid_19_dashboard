import pytest
from unittest.mock import create_autospec
from covid_dashboard.storages.mandal_storage_implementation\
    import MandalStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDetailsForTotalConfirmed

@pytest.mark.django_db
def test_is_valid_total_confirmed_when_invalid_details_given_raises_error():
    # Arrange
    total_confirmed = -1
    storage = MandalStorageImplementation()

    # Act
    with pytest.raises(InvalidDetailsForTotalConfirmed):
        storage.is_valid_total_confirmed(total_confirmed=total_confirmed)


@pytest.mark.django_db
def test_is_valid_total_confirmed(states):
    # Arrange
    total_confirmed = 1
    storage = MandalStorageImplementation()

    # Act
    result = storage.is_valid_total_confirmed(total_confirmed=total_confirmed)

    # Assert
    assert result == None