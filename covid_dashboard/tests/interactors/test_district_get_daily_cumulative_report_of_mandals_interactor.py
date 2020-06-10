import pytest
from collections import defaultdict
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.\
    district_get_daily_cumulative_report_of_mandals_interactor\
        import GetDailyCumulativeReportOfMandalsForDistrict
from covid_dashboard.tests.interactors.conftest import *
from covid_dashboard.interactors.storages.dtos\
    import (MandalReportDto, DailyCumulativeMandalWiseReportDto)
        


def get_daily_cumulative_report_of_mandals_for_district():
    # Arrange
    import datetime
    district_id = 1
    storage = create_autospec(DistrictStorageInterface)
    presenter = create_autospec(PresenterInterface)
    report = {
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
                        'active_cases': 2
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 23),
                        'total_cases': 11,
                        'total_deaths': 2,
                        'total_recovered_cases': 4,
                        'active_cases': 5
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 24),
                        'total_cases': 16,
                        'total_deaths': 6,
                        'total_recovered_cases': 6,
                        'active_cases': 4
                    })
                ],
                2: [
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 22),
                        'total_cases': 1,
                        'total_deaths': 2,
                        'total_recovered_cases': 3,
                        'active_cases': -4
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 23),
                        'total_cases': 7,
                        'total_deaths': 3,
                        'total_recovered_cases': 7,
                        'active_cases': -3
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 24),
                        'total_cases': 14,
                        'total_deaths': 3,
                        'total_recovered_cases': 7,
                        'active_cases': 4
                    })
                ],
                3: [
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 23),
                        'total_cases': 10,
                        'total_deaths': 3,
                        'total_recovered_cases': 2,
                        'active_cases': 5
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 24),
                        'total_cases': 27,
                        'total_deaths': 18,
                        'total_recovered_cases': 4,
                        'active_cases': 5
                    }),
                    defaultdict(int, {
                        'date': datetime.date(2020, 5, 25),
                        'total_cases': 57,
                        'total_deaths': 23,
                        'total_recovered_cases': 14,
                        'active_cases': 20
                    })
                ]
            }
        )
    }
    expected_output = {
        "district_name":"Kurnool",
        "mandals":[
            {
                "mandal_id":1,
                "mandal_name":"Kallur",
                "total_cases":10,
                "total_deaths":5,
                "total_recovered_cases":4,
                "active_cases":1
            },
            {
                "mandal_id":2,
                "mandal_name":"Adoni",
                "total_cases":3,
                "total_deaths":0,
                "total_recovered_cases":1,
                "active_cases":2
            }
        ]
    }
    interactor = GetDailyCumulativeReportOfMandalsForDistrict(
        storage=storage, presenter=presenter)
    storage.get_daily_cumulative_report_of_mandals_for_district\
        .return_value = report
    storage._get_initial_and_final_date.return_value = \
        (datetime.date(2020, 5, 23), datetime.date(2020, 5, 25))
    presenter.get_response_for_daily_cumulative_report_of_mandals_for_district\
        .return_value = expected_output
    
    # Act
    result = interactor.get_daily_cumulative_report_of_mandals_for_district(
        district_id)

    # Assert
    assert result == expected_output
    storage.get_daily_cumulative_report_of_mandals_for_district.\
        assert_called_once_with(district_id)
    presenter.get_response_for_daily_cumulative_report_of_mandals_for_district.\
        assert_called_once()