import pytest
import datetime
from unittest.mock import create_autospec
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos import DailyCumulativeReport
from covid_dashboard.tests.storages.conftest import *
from collections import defaultdict
from django.db.models import Sum, F, Prefetch
from covid_dashboard.models\
    import State, District, Mandal, Stats



@pytest.mark.django_db
def get_daily_cumulative_report_storage(
        mandals, districts, states, stats):

    # Arrange
    storage = StateStorageImplementation()
    expected_result = daily_cumulative_report_dto

    # Act
    result = storage.get_daily_cumulative_report()

    # Assert
    assert result == expect
    ed_result


@pytest.mark.django_db
def get_daily_cumulative_report_storage_when_no_cases_for_a_district(
    mandals2, districts2, states, stats2):

    # Arrange
    report = CumulativeReportOnSpecificDay(
        date=datetime.date(2020, 5, 28),
        total_cases=20,
        total_deaths=0,
        total_recovered_cases=20,
        active_cases=0
    )
    storage = StateStorageImplementation()
    expected_result = DailyCumulativeReport(report=[report])

    # Act
    result = storage.get_daily_cumulative_report()

    # Assert
    assert result == expected_result


@pytest.mark.django_db
def test_get_daily_cumulative_report_storage(all_states, all_districts, all_mandals, all_stats):

    storage = StateStorageImplementation()
    state_id = 1
    expected_result = DailyCumulativeReport(
        report=[
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 20),
                total_cases=5, total_deaths=0,
                total_recovered_cases=5,
                active_cases=0
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 21),
                total_cases=25, total_deaths=0,
                total_recovered_cases=15,
                active_cases=10
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 22),
                total_cases=41, total_deaths=3,
                total_recovered_cases=25,
                active_cases=13
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 23),
                total_cases=68,
                total_deaths=8,
                total_recovered_cases=33,
                active_cases=27
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 24),
                total_cases=97,
                total_deaths=27,
                total_recovered_cases=37,
                active_cases=33
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 25),
                total_cases=127,
                total_deaths=32,
                total_recovered_cases=47,
                active_cases=48
            )
        ]
    )

    # Act
    result = storage.get_daily_cumulative_report()

    # Assert
    assert result == expected_result