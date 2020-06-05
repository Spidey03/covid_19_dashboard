import pytest
import datetime
from collections import defaultdict
from unittest.mock import create_autospec
from covid_dashboard.storages.district_storage_implementation\
    import DistrictStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos\
    import DailyCumulativeMandalWiseReportDto
from covid_dashboard.tests.storages.conftest import *
from collections import defaultdict
from django.db.models import Sum, F, Prefetch
from covid_dashboard.models\
    import State, District, Mandal, Stats

@pytest.mark.django_db
def test_get_daily_cumulative_report_of_mandals_for_district_when_no_cases(
        all_districts, all_mandals, all_states):
    # Arrange
    district_id = 1
    expected_result = {
        "district_name":'Kurnool',
        "mandals":{
            1: {'mandal_id': 1, 'mandal_name': 'Kallur'},
            2: {'mandal_id': 2, 'mandal_name': 'Adoni'},
            3: {'mandal_id': 3, 'mandal_name': 'Kodumur'}
        },
        "reports":defaultdict(list)
    }
    storage = DistrictStorageImplementation()

    result = storage.get_daily_cumulative_report_of_mandals_for_district(
        district_id=district_id)

    assert result == expected_result



@pytest.mark.django_db
def test_get_daily_cumulative_report_of_mandals_for_district(
        all_mandals, all_states, all_districts, all_stats):
    # Arrange
    district_id = 1
    expected_result = {
        "district_name":'Kurnool',
        "mandals":{
            1: {'mandal_id': 1, 'mandal_name': 'Kallur'},
            2: {'mandal_id': 2, 'mandal_name': 'Adoni'},
            3: {'mandal_id': 3, 'mandal_name': 'Kodumur'}
        },
        "reports":defaultdict(list, 
            {
                1: [
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 22),
                        'total_cases': 5,
                        'total_deaths': 1,
                        'total_recovered_cases': 2,
                        # 'active_cases': 2
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 23),
                        'total_cases': 11,
                        'total_deaths': 2,
                        'total_recovered_cases': 4,
                        # 'active_cases': 5
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 24),
                        'total_cases': 16,
                        'total_deaths': 6,
                        'total_recovered_cases': 6,
                        # 'active_cases': 4
                    })
                ],
                2: [
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 22),
                        'total_cases': 1,
                        'total_deaths': 2,
                        'total_recovered_cases': 3,
                        # 'active_cases': -4
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 23),
                        'total_cases': 7,
                        'total_deaths': 3,
                        'total_recovered_cases': 7,
                        # 'active_cases': -3
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 24),
                        'total_cases': 14,
                        'total_deaths': 3,
                        'total_recovered_cases': 7,
                        # 'active_cases': 4
                    })
                ],
                3: [
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 23),
                        'total_cases': 10,
                        'total_deaths': 3,
                        'total_recovered_cases': 2,
                        # 'active_cases': 5
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 24),
                        'total_cases': 27,
                        'total_deaths': 18,
                        'total_recovered_cases': 4,
                        # 'active_cases': 5
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 25),
                        'total_cases': 57,
                        'total_deaths': 23,
                        'total_recovered_cases': 14,
                        # 'active_cases': 20
                    })
                ]
            }
        )
    }
    storage = DistrictStorageImplementation()

    result = storage.get_daily_cumulative_report_of_mandals_for_district(
        district_id=district_id)

    assert result == expected_result