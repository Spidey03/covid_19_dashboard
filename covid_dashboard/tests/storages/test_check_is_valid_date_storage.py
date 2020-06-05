import pytest
from unittest.mock import create_autospec
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDate

@pytest.mark.django_db
def test_check_is_valid_date_v1():
    # Arrange
    import datetime
    date = datetime.date(year=3000, month=1, day=1)
    storage = StateStorageImplementation()

    # Act
    with pytest.raises(InvalidDate):
        storage.check_is_date_valid(date=date)
