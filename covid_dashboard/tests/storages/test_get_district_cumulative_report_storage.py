import pytest
from datetime import datetime
from collections import defaultdict
from unittest.mock import create_autospec
# from covid_dashboard.models import *
# from django.db.models import Sum, F, Prefetch
from covid_dashboard.storages.district_storage_implementation\
    import DistrictStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos\
    import DistrictReportDto, MandalReportDto
from covid_dashboard.tests.storages.conftest import *

@pytest.mark.django_db
def test_get_district_cumulative_report(
    all_states, all_districts, all_mandals, all_stats):
    # Arrange
    district_id=1
    till_date = datetime.date(year=2020, month=5, day=29)
    expected_result = DistrictReportDto(
         district_name='Kurnool',
         mandals=[
            MandalReportDto(
                mandal_id=1,
                 mandal_name='Kallur',
                 total_cases=16,
                 total_deaths=6,
                 total_recovered_cases=6,
                 active_cases=4
            ),
            MandalReportDto(
                mandal_id=2,
                 mandal_name='Adoni',
                 total_cases=14,
                 total_deaths=3,
                 total_recovered_cases=7,
                 active_cases=4
            ),
            MandalReportDto(
                mandal_id=3,
                 mandal_name='Kodumur',
                 total_cases=57,
                 total_deaths=23,
                 total_recovered_cases=14,
                 active_cases=20
            )
        ],
         total_cases=87,
         total_deaths=32,
         total_recovered_cases=27,
         active_cases=28
        )

    storage = DistrictStorageImplementation()

    # Act
    result = storage.get_district_cumulative_report(district_id=district_id,
        till_date=till_date)

    # Assert
    assert result == expected_result


@pytest.mark.django_db
def test_get_district_cumulative_report_v2(all_states, all_districts, all_mandals, all_stats):
    # Arrange
    district_id=2
    till_date = datetime.date(year=2020, month=5, day=29)
    expected_result = DistrictReportDto(
        district_name='Nellore',
        mandals=[
            MandalReportDto(
                mandal_id=4,
                mandal_name='Kota',
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0,
                active_cases=0
            ),
            MandalReportDto(
                mandal_id=5,
                mandal_name='Kavali',
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0,
                active_cases=0
            ),
            MandalReportDto(
                mandal_id=6,
                mandal_name='Kovuru',
                total_cases=40,
                total_deaths=0,
                total_recovered_cases=20,
                active_cases=20
            )
        ],
        total_cases=40,
        total_deaths=0,
        total_recovered_cases=20,
        active_cases=20
    )

    storage = DistrictStorageImplementation()

    # Act
    result = storage.get_district_cumulative_report(district_id=district_id,
        till_date=till_date)

    # Assert
    assert result == expected_result