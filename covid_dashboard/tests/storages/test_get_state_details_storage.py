import pytest
from covid_dashboard.storages.state_storage_implementation \
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions import InvalidStateId


class TestGetStateDetails:

    @pytest.mark.django_db
    def test_when_invalid_state_id_given(self):

        # Arrange
        state_id = 4
        storage = StateStorageImplementation()

        # Assert
        with pytest.raises(InvalidStateId):
            storage.get_state_details(state_id=state_id)

    @pytest.mark.django_db
    def test_when_valid_state_id_given(self, states, state_dto):

        # Arrange
        state_id = 1
        storage = StateStorageImplementation()

        # Act
        state_dto_response = storage.get_state_details(state_id=state_id)

        # Assert
        assert state_dto_response == state_dto
        
