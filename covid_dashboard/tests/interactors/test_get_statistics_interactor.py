import pytest
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.mandal_storage_interface\
    import MandalStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_statistics_interactor\
    import GetStatistics
from covid_dashboard.exceptions.exceptions\
    import InvalidMandalId
from covid_dashboard.tests.interactors.conftest import *
from covid_dashboard.interactors.storages.dtos import *

def test_get_statistics_for_mandal_invalid_mandal_id():
    # Arrange
    storage = create_autospec(MandalStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetStatistics(storage=storage, presenter=presenter)
    mandal_id = 10
    report = None
    result = None
    user = {'is_superuser':True}
    storage.is_valid_mandal_id.side_effect = InvalidMandalId
    presenter.raise_invalid_details_for_mandal_id.side_effect = InvalidMandalId

    # Act
    with pytest.raises(InvalidMandalId):
        interactor.get_statistics(mandal_id=mandal_id, user=user)


def test_get_statistics_for_mandal():
    # Arrange
    import datetime
    storage = create_autospec(MandalStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetStatistics(storage=storage, presenter=presenter)
    mandal_id = 10
    user = {'is_superuser':True}
    report = MandalStatistics(
            mandal_id=1,
            mandal_name='Kallur',
            reports=[
                Statistics(
                    date=datetime.date(year=2020, month=5, day=25),
                    total_cases=5,
                    total_deaths=0,
                    total_recovered_cases=3
                ),
                Statistics(
                    date=datetime.date(year=2020, month=5, day=26),
                    total_cases=3,
                    total_deaths=0,
                    total_recovered_cases=3
                )
            ]
        )
    expected_result = {
        "mandal_id":1,
        "mandal_name":"Kallur",
        "reports":[
            {
                "date":"2020-05-25",
                "total_cases":5,
                "total_deaths":0,
                "total_recovered_cases":3
            },
            {
                "date":"2020-05-26",
                "total_cases":3,
                "total_deaths":0,
                "total_recovered_cases":3
            }
        ]
    }
    
    storage.get_statistics.return_value = report
    presenter.get_response_for_get_statistics.return_value = expected_result

    # Act
    result = interactor.get_statistics(mandal_id=mandal_id, user=user)

    # Assert
    assert result == expected_result
    storage.get_statistics.assert_called_once_with(mandal_id=mandal_id)
    presenter.get_response_for_get_statistics.assert_called_once_with(report)
