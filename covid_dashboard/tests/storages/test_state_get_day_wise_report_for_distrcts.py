import pytest
import datetime
from covid_dashboard.storages.state_storage_implementation \
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions import InvalidStateId
from covid_dashboard.interactors.storages.dtos import DistrictDayReportDto


class TestStateGetDayWiseReportWithDistricts:

    @pytest.mark.django_db
    def test_state_get_day_wise_report_with_district(self, states,
            districts, mandals, stats):

        # Arrange
        district_ids = [1,2]
        storage = StateStorageImplementation()
        expected_district_day_report_dtos = [
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 25),
                total_confirmed=14,
                total_recovered=7,
                total_deaths=0,
                district_id=1
            ),
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 26),
                total_confirmed=10,
                total_recovered=2,
                total_deaths=2,
                district_id=1
            ),
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 27),
                total_confirmed=10,
                total_recovered=2,
                total_deaths=0,
                district_id=1
            ),
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 25),
                total_confirmed=20,
                total_recovered=0,
                total_deaths=6,
                district_id=2
            ),
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 26),
                total_confirmed=7,
                total_recovered=3,
                total_deaths=0,
                district_id=2
            ),
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 27),
                total_confirmed=11,
                total_recovered=3,
                total_deaths=5,
                district_id=2
            ),
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 26),
                total_confirmed=1,
                total_recovered=0,
                total_deaths=0,
                district_id=3
            ),
            DistrictDayReportDto(
                date=datetime.date(2020, 5, 27),
                total_confirmed=3,
                total_recovered=1,
                total_deaths=1,
                district_id=3
            )
        ]

        # Act
        district_day_report_dtos = storage.get_day_wise_report_for_distrcts(
            district_ids=district_ids)

        # Assert
        assert district_day_report_dtos == expected_district_day_report_dtos