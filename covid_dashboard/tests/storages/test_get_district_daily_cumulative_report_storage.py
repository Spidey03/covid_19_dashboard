import pytest
from datetime import datetime
from collections import defaultdict
from unittest.mock import create_autospec
# from covid_dashboard.models import *
# from django.db.models import Sum, F, Prefetch
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.exceptions.exceptions\
    import InvalidDistrictId
from covid_dashboard.interactors.storages.dtos import DailyCumulativeDistrictWise
from covid_dashboard.tests.storages.conftest import *
# from covid_dashboard.tests.interactors.conftest import *
# get_district_daily_cumulative_report

@pytest.mark.django_db
def test_get_district_daily_cumulative_report_storage(
        states, districts, mandals, stats):

    # Arrange
    storage = StateStorageImplementation()
    district_id = 1
    districts_df = defaultdict(list)
    district_statistics = defaultdict(int)
    district_statistics['date'] = datetime.date(2020, 5, 28)
    district_statistics['total_cases'] = 10
    district_statistics['total_deaths'] = 0
    district_statistics['total_recovered_cases'] = 10
    # district_statistics['active_cases'] = 0
    districts_df[1].append(district_statistics)

    district_statistics = defaultdict(int)
    district_statistics['date'] = datetime.date(2020, 5, 28)
    district_statistics['total_cases'] = 10
    district_statistics['total_deaths'] = 0
    district_statistics['total_recovered_cases'] = 10
    # district_statistics['active_cases'] = 0
    districts_df[2].append(district_statistics)

    expected_result = {
        "state_name":'Andhrapradesh',
        "districts":{
            1: {
                'district_id': 1,
                'district_name': 'Kurnool'
            },
            2: {
                'district_id': 2,
                'district_name': 'Nellore'
            
            }
        },
        "reports":districts_df
    }
    # Act
    result = storage.get_district_daily_cumulative_report()

    # Assert
    assert result == expected_result



@pytest.mark.django_db
def test_get_district_daily_cumulative_report_storage_with_multiple_districts(
        states, districts3, mandals3, stats3):
    # Arrange
    storage = StateStorageImplementation()
    district_id = 1
    districts_df = defaultdict(list)
    district_statistics = defaultdict(int)
    district_statistics = {
        'date':datetime.date(2020, 5, 26),
        'total_cases':30,
        'total_deaths':3,
        'total_recovered_cases':0,
        # 'active_cases':27
    }
    districts_df[2].append(district_statistics)
    district_statistics = {
        'date':datetime.date(2020, 5, 27),
        'total_cases':40,
        'total_deaths':3,
        'total_recovered_cases':0,
        # 'active_cases':37
    }
    districts_df[2].append(district_statistics)
    district_statistics = {
        'date':datetime.date(2020, 5, 28),
        'total_cases':40,
        'total_deaths':3,
        'total_recovered_cases':0,
        # 'active_cases':37
    }
    districts_df[2].append(district_statistics)
    district_statistics = {
        'date':datetime.date(2020, 5, 28),
        'total_cases':20,
        'total_deaths':0,
        'total_recovered_cases':20,
        # 'active_cases':0
    }
    districts_df[1].append(district_statistics)

    expected_result ={
        "state_name":'Andhrapradesh',
        "districts":{1: {'district_id': 1, 'district_name': 'Kurnool'}, 2: {'district_id': 2, 'district_name': 'Nellore'}, 3: {'district_id': 3, 'district_name': 'Ananthapuram'}},
        "reports":districts_df
    }
    # Act
    result = storage.get_district_daily_cumulative_report()

    # Assert
    assert result == expected_result
    
    

@pytest.mark.django_db
def test_get_district_daily_cumulative_report_storage_v2(
        all_states, all_districts, all_mandals, all_stats):
    # Arrange
    storage = StateStorageImplementation()
    
    reports = defaultdict(list)
    district_statistics = defaultdict(int)
    district_statistics = {
        'date': datetime.date(2020, 5, 20),
        'total_cases': 5,
        'total_deaths': 0,
        'total_recovered_cases': 5,
        # 'active_cases': 0
    }
    reports[2].append(district_statistics)
    district_statistics = {
        'date': datetime.date(2020, 5, 21),
        'total_cases': 25,
        'total_deaths': 0,
        'total_recovered_cases': 15,
        # 'active_cases': 10
    }
    reports[2].append(district_statistics)
    district_statistics = {
        'date': datetime.date(2020, 5, 22),
        'total_cases': 35,
        'total_deaths': 0,
        'total_recovered_cases': 20,
        # 'active_cases': 15
    }
    reports[2].append(district_statistics)
    district_statistics = {
        'date': datetime.date(2020, 5, 23),
        'total_cases': 40,
        'total_deaths': 0,
        'total_recovered_cases': 20,
        # 'active_cases': 20
    }
    reports[2].append(district_statistics)

    district_statistics = {
        'date': datetime.date(2020, 5, 22),
        'total_cases': 6,
        'total_deaths': 3,
        'total_recovered_cases': 5,
        # 'active_cases': -2
    }
    reports[1].append(district_statistics)
    district_statistics = {
        'date': datetime.date(2020, 5, 23),
        'total_cases': 28,
        'total_deaths': 8,
        'total_recovered_cases': 13,
        # 'active_cases': 7
    }
    reports[1].append(district_statistics)
        
    district_statistics = {
        'date': datetime.date(2020, 5, 24),
        'total_cases': 57,
        'total_deaths': 27,
        'total_recovered_cases': 17,
        # 'active_cases': 13
    }
    reports[1].append(district_statistics)
        
    district_statistics = {
        'date': datetime.date(2020, 5, 25),
        'total_cases': 87,
        'total_deaths': 32,
        'total_recovered_cases': 27,
        # 'active_cases': 28
    }
    reports[1].append(district_statistics)
    
    expected_result =  {
        "state_name":'Andhrapradesh',
        "districts":{
            1: {'district_id': 1, 'district_name': 'Kurnool'},
            2: {'district_id': 2, 'district_name': 'Nellore'}
            
        },
        "reports":reports
    }
    # Act
    result = storage.get_district_daily_cumulative_report()

    # Assert
    assert result == expected_result
    