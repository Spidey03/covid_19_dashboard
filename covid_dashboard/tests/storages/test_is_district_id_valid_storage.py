import pytest
from unittest.mock import create_autospec
from covid_dashboard.storages.district_storage_implementation\
    import DistrictStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId

@pytest.mark.django_db
def test_is_district_id_valid_when_invalid_district_id_raises_exception():
    # Arrange
    district_id = 1
    storage = DistrictStorageImplementation()

    # Act
    with pytest.raises(InvalidDistrictId):
        storage.is_district_id_valid(district_id=district_id)


@pytest.mark.django_db
def test_is_district_id_valid_when_valid_district_id(states, districts):
    # Arrange
    district_id = 1
    storage = DistrictStorageImplementation()

    # Act
    result = storage.is_district_id_valid(district_id=district_id)

    # Assert
    assert result == None