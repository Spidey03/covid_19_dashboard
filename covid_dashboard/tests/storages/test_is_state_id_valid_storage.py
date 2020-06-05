import pytest
from unittest.mock import create_autospec
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidStateId

@pytest.mark.django_db
def test_is_state_id_valid_when_invalid_state_id_raises_exception():
    # Arrange
    state_id = 1
    storage = StateStorageImplementation()

    # Act
    with pytest.raises(InvalidStateId):
        storage.is_state_id_valid(state_id=state_id)


@pytest.mark.django_db
def test_is_state_id_valid_when_valid_state_id(states):
    # Arrange
    state_id = 1
    storage = StateStorageImplementation()

    # Act
    result = storage.is_state_id_valid(state_id=state_id)

    # Assert
    assert result == None