import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.storages.district_storage_implementation\
    import DistrictStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos import DailyCumulativeReport
from covid_dashboard.tests.storages.conftest import *
from collections import defaultdict
from django.db.models import Sum, F, Prefetch
from covid_dashboard.models\
    import State, District, Mandal, Stats

@pytest.mark.django_db
def test_get_daily_cumulative_report_for_district_storage(all_states, all_districts,
        all_mandals, all_stats):
    # Arrange
    district_id = 1
    storage = DistrictStorageImplementation()
    expected_result = DailyCumulativeReport(
        report = [
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 20),
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0,
                active_cases=0
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 21),
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0,
                active_cases=0
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 22),
                total_cases=6,
                total_deaths=3,
                total_recovered_cases=5,
                active_cases=-2
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 23),
                total_cases=28,
                total_deaths=8,
                total_recovered_cases=13,
                active_cases=7
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 24),
                total_cases=57,
                total_deaths=27,
                total_recovered_cases=17,
                active_cases=13
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 25),
                total_cases=87,
                total_deaths=32,
                total_recovered_cases=27,
                active_cases=28
            )
        ] 
    )

    # Act
    result = storage.get_daily_cumulative_report_for_district(district_id)

    # Assert
    assert result == expected_result