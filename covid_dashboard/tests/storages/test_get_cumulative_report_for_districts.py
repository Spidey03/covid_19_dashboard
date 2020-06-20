import pytest
import datetime
from covid_dashboard.storages.state_storage_implementation \
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions import InvalidStateId
from covid_dashboard.interactors.storages.dtos import DistrictReportDto


class TestGetCumulativeReportForDistricts:

    @pytest.mark.django_db
    def test_get_report_when_no_district_has_stat_reports(self, states, districts, mandals, stats):

        # Arrange
        district_ids = [1,2]
        storage = StateStorageImplementation()
        till_date = datetime.date(year=2020, month=5, day=24)
        expected_district_report_dto_list =  [
            DistrictReportDto(district_id=1,
                total_confirmed=0,
                total_recovered=0,
                total_deaths=0
            ),
            DistrictReportDto(
                district_id=2,
                total_confirmed=0,
                total_recovered=0,
                total_deaths=0
            )
        ]

        # Act
        district_report_dto_list = \
            storage.get_cumulative_report_for_districts(
                district_ids, till_date=till_date)

        # Assert
        assert district_report_dto_list == expected_district_report_dto_list

    @pytest.mark.django_db
    def test_get_report_when_some_district_has_stat_reports(self, states, districts, mandals, stats):

        # Arrange
        district_ids = [1, 2, 4]
        storage = StateStorageImplementation()
        till_date = datetime.date(year=2020, month=5, day=25)
        expected_district_report_dto_list = [
            DistrictReportDto(
                district_id=1,
                total_confirmed=14,
                total_recovered=7,
                total_deaths=0
            ),
            DistrictReportDto(
                district_id=2,
                total_confirmed=20,
                total_recovered=0,
                total_deaths=6
            ),
            DistrictReportDto(
                district_id=4,
                total_confirmed=0,
                total_recovered=0,
                total_deaths=0
            )
        ]
        # Act
        district_report_dto_list = \
            storage.get_cumulative_report_for_districts(
                district_ids, till_date=till_date)

        # Assert
        assert district_report_dto_list == expected_district_report_dto_list
