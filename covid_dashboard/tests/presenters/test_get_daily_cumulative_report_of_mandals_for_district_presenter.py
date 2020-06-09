import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.storages.conftest\
    import daily_cumulative_report_dto
from covid_dashboard.interactors.storages.dtos import *

def test_get_response_for_daily_cumulative_report_of_mandals_for_district():
    # Arrange
    import datetime
    mandals = [
        MandalCumulativeReportOnSpecificDayDto(
            mandal_id=1,
            mandal_name="Kallur",
            report=[
                CumulativeReportOnSpecificDay(
                    date=datetime.date(year=2020, month=5, day=26),
                    total_cases=5,
                    total_recovered_cases=3,
                    total_deaths=0,
                    active_cases=2
                ),
                CumulativeReportOnSpecificDay(
                    date=datetime.date(year=2020, month=5, day=27),
                    total_cases=10,
                    total_recovered_cases=5,
                    total_deaths=3,
                    active_cases=2
                )
            ]
        ),
        MandalCumulativeReportOnSpecificDayDto(
            mandal_id=2,
            mandal_name="Adoni",
            report=[
                CumulativeReportOnSpecificDay(
                    date=datetime.date(year=2020, month=5, day=30),
                    total_cases=0,
                    total_recovered_cases=0,
                    total_deaths=0,
                    active_cases=0
                ),
                CumulativeReportOnSpecificDay(
                    date=datetime.date(year=2020, month=5, day=31),
                    total_cases=5,
                    total_recovered_cases=1,
                    total_deaths=2,
                    active_cases=2
                )
            ]
        )
    ]
    report = ListMandalDailyCumulativeReportDto(
        district_name="Kurnool",
        mandals=mandals
        )
    expected_response = {
        'district_name': 'Kurnool',
        'mandals': [
            {
                'mandal_id': 1,
                'mandal_name':'Kallur',
                'daily_cumulative': [
                    {
                        'date': str(datetime.date(2020, 5, 26).strftime('%d-%b-%Y')),
                        'total_cases': 5,
                        'total_deaths': 0,
                        'total_recovered_cases': 3,
                        'active_cases': 2
                    },
                    {
                        'date': str(datetime.date(2020, 5, 27).strftime('%d-%b-%Y')),
                        'total_cases': 10,
                        'total_deaths': 3,
                        'total_recovered_cases': 5,
                        'active_cases': 2
                    }
                ]
            
            },
            {
                'mandal_id': 2,
                'mandal_name': 'Adoni',
                'daily_cumulative': [
                    {
                        'date': str(datetime.date(2020, 5, 30).strftime('%d-%b-%Y')),
                        'total_cases': 0,
                        'total_deaths': 0,
                        'total_recovered_cases': 0,
                        'active_cases': 0
                    },
                    {
                        'date': str(datetime.date(2020, 5, 31).strftime('%d-%b-%Y')),
                        'total_cases': 5,
                        'total_deaths': 2,
                        'total_recovered_cases': 1,
                        'active_cases': 2
                    }
                ]
            }
        ]
    }
    presenter = PresenterImplementation()

    # Act
    response = presenter.\
        get_response_for_daily_cumulative_report_of_mandals_for_district(report)

    # Assert
    assert response == expected_response