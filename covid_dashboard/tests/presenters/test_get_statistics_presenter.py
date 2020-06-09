import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.storages.conftest\
    import *
from covid_dashboard.interactors.storages.dtos import *


def test_get_statistics_presenter():
    # Arrange
    import datetime
    presenter = PresenterImplementation()
    mandal_report = MandalStatistics(
        mandal_id=1,
        mandal_name='Kallur',
        reports=[
            Statistics(
                date=datetime.date(2020, 5, 22),
                total_cases=5,
                total_deaths=1,
                total_recovered_cases=2
            ),
            Statistics(
                date=datetime.date(2020, 5, 23),
                total_cases=6,
                total_deaths=1,
                total_recovered_cases=2
            ),
            Statistics(
                date=datetime.date(2020, 5, 24),
                total_cases=5,
                total_deaths=4,
                total_recovered_cases=2
            )
        ]
    )
    expected_response = {
        'mandal_id': 1,
        'mandal_name': 'Kallur',
        'reports': [
            {
                'date': str(datetime.date(2020, 5, 22).strftime('%d-%b-%Y')),
                'total_cases': 5,
                'total_deaths': 1,
                'total_recovered_cases': 2
            },
            {
                'date': str(datetime.date(2020, 5, 23).strftime('%d-%b-%Y')),
                'total_cases': 6,
                'total_deaths': 1,
                'total_recovered_cases': 2
            },
            {
                'date': str(datetime.date(2020, 5, 24).strftime('%d-%b-%Y')),
                'total_cases': 5,
                'total_deaths': 4,
                'total_recovered_cases': 2
            }
        ]
    }

    # Act
    response = presenter.get_response_for_get_statistics(mandal_report)

    # Assert
    assert response == expected_response