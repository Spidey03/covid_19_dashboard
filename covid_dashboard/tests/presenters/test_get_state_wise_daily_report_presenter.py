import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.storages.conftest\
    import *
from covid_dashboard.interactors.storages.dtos import Report


def test_get_response_for_get_state_wise_daily_report_presenter():
    # Arrange
    presenter = PresenterImplementation()
    report = [
        Report(
            date=datetime.date(2020, 5, 20),
            total_cases=5,
            total_recovered_cases=5,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 21),
            total_cases=20,
            total_recovered_cases=10,
            total_deaths=0,
            active_cases=10
        ),
        Report(
            date=datetime.date(2020, 5, 22),
            total_cases=16,
            total_recovered_cases=10,
            total_deaths=3,
            active_cases=3
        ),
        Report(
            date=datetime.date(2020, 5, 23),
            total_cases=27,
            total_recovered_cases=8,
            total_deaths=5,
            active_cases=14
        ),
        Report(
            date=datetime.date(2020, 5, 24),
            total_cases=29,
            total_recovered_cases=4,
            total_deaths=19,
            active_cases=6
        )
    ]
    expected_response =  [
        {
            'active_cases': 0,
            'date': datetime.date(2020, 5, 20),
            'total_cases': 5,
            'total_deaths': 0,
            'total_recovered_cases': 5
        },
        {
            'active_cases': 10,
            'date': datetime.date(2020, 5, 21),
            'total_cases': 20,
            'total_deaths': 0,
            'total_recovered_cases': 10
        },
        {
            'active_cases': 3,
            'date': datetime.date(2020, 5, 22),
            'total_cases': 16,
            'total_deaths': 3,
            'total_recovered_cases': 10
        },
        {
            'active_cases': 14,
            'date': datetime.date(2020, 5, 23),
            'total_cases': 27,
            'total_deaths': 5,
            'total_recovered_cases': 8
        },
        {
            'active_cases': 6,
            'date': datetime.date(2020, 5, 24),
            'total_cases': 29,
            'total_deaths': 19,
            'total_recovered_cases': 4
        }
    ]


    # Act
    response = presenter.get_response_for_state_wise_daily_cases_report(
        report)

    # Assert
    assert response == expected_response


def test_get_response_for_get_state_wise_daily_report_presenter_when_no_report_for_a_day():
    # Arrange
    presenter = PresenterImplementation()
    report = [
        Report(
            date=datetime.date(2020, 5, 22),
            total_cases=5,
            total_recovered_cases=2,
            total_deaths=1,
            active_cases=2
        ),
        Report(
            date=datetime.date(2020, 5, 23),
            total_cases=10,
            total_recovered_cases=2,
            total_deaths=3,
            active_cases=5
        ),
        Report(
            date=datetime.date(2020, 5, 24),
            total_cases=12,
            total_recovered_cases=2,
            total_deaths=4,
            active_cases=6
        ),
        Report(
            date=datetime.date(2020, 5, 25),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 26),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 27),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 28),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        ),
        Report(
            date=datetime.date(2020, 5, 29),
            total_cases=0,
            total_recovered_cases=0,
            total_deaths=0,
            active_cases=0
        )
    ]
    expected_response = [
        {
            'date': datetime.date(2020, 5, 22),
             'total_cases': 5,
             'total_deaths': 1,
             'total_recovered_cases': 2,
             'active_cases': 2
        },
        {
            'date': datetime.date(2020, 5, 23),
             'total_cases': 10,
             'total_deaths': 3,
             'total_recovered_cases': 2,
             'active_cases': 5
        },
        {
            'date': datetime.date(2020, 5, 24),
             'total_cases': 12,
             'total_deaths': 4,
             'total_recovered_cases': 2,
             'active_cases': 6
        },
        {
            'date': datetime.date(2020, 5, 25),
             'total_cases': 0,
             'total_deaths': 0,
             'total_recovered_cases': 0,
             'active_cases': 0
        },
        {
            'date': datetime.date(2020, 5, 26),
             'total_cases': 0,
             'total_deaths': 0,
             'total_recovered_cases': 0,
             'active_cases': 0
        },
        {
            'date': datetime.date(2020, 5, 27),
             'total_cases': 0,
             'total_deaths': 0,
             'total_recovered_cases': 0,
             'active_cases': 0
        },
        {
            'date': datetime.date(2020, 5, 28),
             'total_cases': 0,
             'total_deaths': 0,
             'total_recovered_cases': 0,
             'active_cases': 0
        },
        {
            'date': datetime.date(2020, 5, 29),
             'total_cases': 0,
             'total_deaths': 0,
             'total_recovered_cases': 0,
             'active_cases': 0
        }
    ]
    
    # Act
    response = presenter.get_response_for_state_wise_daily_cases_report(
        report)

    # Assert
    assert response == expected_response