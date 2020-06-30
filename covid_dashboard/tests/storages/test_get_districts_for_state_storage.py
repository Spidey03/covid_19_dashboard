import pytest
from covid_dashboard.storages.state_storage_implementation \
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions import InvalidStateId


class TestGetDistrictsForState:

    @pytest.mark.django_db
    def test_with_state_id_returns_district_dto_list(self, states, districts, district_dtos):

        # Arrange
        state_id = 1
        storage = StateStorageImplementation()

        # Act
        district_dtos_response = storage.get_districts_for_state(
            state_id=state_id)

        # Assert
        assert district_dtos == district_dtos_response
