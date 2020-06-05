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
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.tests.storages.conftest import *


@pytest.mark.django_db
def test_get_district_report_of_specific_day(all_states, all_districts, all_mandals, all_stats):
    # Arrange
    import datetime
    district_id = 1
    date = datetime.date(year=2020, month=5, day=24)
    storage = DistrictStorageImplementation()
    expected_result = DistrictReportOfDay(
        district_name='Kurnool',
        mandals=[
            MandalReportOfDay(
                mandal_id=1,
                mandal_name='Kallur',
                total_cases=5,
                total_deaths=4,
                total_recovered_cases=2
            ),
            MandalReportOfDay(
                mandal_id=2,
                mandal_name='Adoni',
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0
            ),
            MandalReportOfDay(
                mandal_id=3,
                mandal_name='Kodumur',
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0
            )
        ],
        total_cases=5,
        total_deaths=4,
        total_recovered_cases=2
    )

    # Act
    result = storage.get_district_report_of_specific_day(
        district_id=district_id, date=date)

    # Assert
    assert result == expected_result