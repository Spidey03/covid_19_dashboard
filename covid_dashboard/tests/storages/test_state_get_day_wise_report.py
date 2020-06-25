import pytest
import datetime
from covid_dashboard.storages.state_storage_implementation \
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions import InvalidStateId
from covid_dashboard.interactors.storages.dtos import DayReportDto

class TestStateGetDayWiseReport:

    @pytest.mark.django_db
    def test_get_day_wise_report(self, states, districts, mandals, stats):

        # Arrange
        state_id = 1
        expected_daily_report = [
            DayReportDto(
                date=datetime.date(2020, 5, 25),
                total_confirmed=34,
                total_recovered=7,
                total_deaths=6
            ),
            DayReportDto(
                date=datetime.date(2020, 5, 26),
                total_confirmed=18,
                total_recovered=5,
                total_deaths=2
            ),
            DayReportDto(
                date=datetime.date(2020, 5, 27),
                total_confirmed=24,
                total_recovered=6,
                total_deaths=6
            )
        ]
        storage = StateStorageImplementation()

        # Act
        daily_report_dto_list = storage.state_get_day_wise_report(
            state_id=state_id)

        assert daily_report_dto_list == expected_daily_report