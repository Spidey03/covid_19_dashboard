import pytest
from unittest.mock import create_autospec
from covid_dashboard.storages.mandal_storage_implementation\
    import MandalStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDetailsForTotalRecovered

@pytest.mark.django_db
def test_is_valid_total_deaths_when_invalid_details_given_raises_error():
    # Arrange
    total_recovered = -10
    storage = MandalStorageImplementation()

    # Act
    with pytest.raises(InvalidDetailsForTotalRecovered):
        storage.is_valid_total_recovered(total_recovered=total_recovered)


@pytest.mark.django_db
def test_is_valid_total_deaths(states):
    # Arrange
    total_recovered = 1
    storage = MandalStorageImplementation()

    # Act
    result = storage.is_valid_total_recovered(total_recovered=total_recovered)

    # Assert
    assert result == None