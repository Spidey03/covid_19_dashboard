import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.presenters.conftest\
    import list_district_daily_cumulative
from covid_dashboard.interactors.storages.dtos import *

def test_get_district_report_of_specific_day():
    # Arrange
    report = DistrictReportOfDay(
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
    expected_response = {
        'district_name': 'Kurnool',
        'mandals': [
            {
                'mandal_id': 1,
                'mandal_name': 'Kallur',
                'total_cases': 5,
                'total_deaths': 4,
                'total_recovered_cases': 2
            },
            {
                'mandal_id': 2,
                'mandal_name': 'Adoni',
                'total_cases': 0,
                'total_deaths': 0,
                'total_recovered_cases': 0
            },
            {
                'mandal_id': 3,
                'mandal_name': 'Kodumur',
                'total_cases': 0,
                'total_deaths': 0,
                'total_recovered_cases': 0
            }
        ],
        'total_cases': 5,
        'total_deaths': 4,
        'total_recovered_cases': 2
    }
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_response_district_report_of_specific_day(report)

    # Arrange
    assert response == expected_response