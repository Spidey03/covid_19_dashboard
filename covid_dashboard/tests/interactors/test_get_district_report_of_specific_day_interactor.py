import pytest
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_district_report_of_specific_day_interactor\
    import GetDistrictReportOfSpecificDay
from covid_dashboard.tests.interactors.conftest import *
from covid_dashboard.interactors.storages.dtos\
    import DistrictReportOfDay, MandalReportOfDay
from covid_dashboard.exceptions.exceptions import InvalidDate

def test_get_district_report_of_specific_day():
    # Arrange
    import datetime
    date = datetime.date(year=2020, month=5, day=3)
    district_id = 1
    report = DistrictReportOfDay(
            district_name="Kurnool",
            mandals=[
                MandalReportOfDay(
                    mandal_id=1,
                    mandal_name="Kallur",
                    total_cases=6,
                    total_recovered_cases=3,
                    total_deaths=0
                ),
                MandalReportOfDay(
                    mandal_id=2,
                    mandal_name="Adoni",
                    total_cases=1,
                    total_recovered_cases=0,
                    total_deaths=1
                )
            ],
            total_cases=7,
            total_recovered_cases=3,
            total_deaths=1
        )
    expected_result = {
        "district_id":"Kurnool",
        "mandals":[
            {
                "mandal_id":1,
                "mandal_name":"Kallur",
                "total_cases":6,
                "total_recovered_cases":3,
                "total_deaths":0
            },
            {
                "mandal_id":2,
                "mandal_name":"Adoni",
                "total_cases":1,
                "total_recovered_cases":0,
                "total_deaths":1
            }
        ],
        "total_case":7,
        "total_recovered_cases":3,
        "total_deaths":1
    }
    storage = create_autospec(DistrictStorageInterface)
    storage.get_district_report_of_specific_day.return_value = report
    
    presenter = create_autospec(PresenterInterface)
    presenter.get_response_district_report_of_specific_day.return_value = \
        expected_result
    interactor = GetDistrictReportOfSpecificDay(storage, presenter)

    # Act
    result = interactor.get_district_report_of_specific_day(
            date=date, district_id=district_id)

    # Assert
    assert result == expected_result


def test_get_district_report_of_specific_day_invalid_date():
    # Arrange
    import datetime
    date = datetime.date(year=3020, month=5, day=3)
    district_id = 1
    storage = create_autospec(DistrictStorageInterface)
    storage.check_is_date_valid.side_effect = InvalidDate
    
    presenter = create_autospec(PresenterInterface)
    presenter.raise_invalid_date.side_effect = \
        InvalidDate
    interactor = GetDistrictReportOfSpecificDay(storage, presenter)

    # Act
    with pytest.raises(InvalidDate):
        interactor.get_district_report_of_specific_day(
            date=date, district_id=district_id)