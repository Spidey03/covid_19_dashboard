import pytest
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_district_cumulative_report_interactor\
    import GetDistrictCumulativeReport
from covid_dashboard.tests.interactors.conftest import *
from covid_dashboard.interactors.storages.dtos\
    import MandalReportDto, DistrictReportDto


def test_get_district_cumulative_report_interator():
    import datetime
    district_id = 1
    till_date = datetime.date(year=2020, month=2, day=25)
    report = DistrictReportDto(
                district_name="Kurnool",
                mandals=[
                    MandalReportDto(
                        mandal_id=1,
                        mandal_name="Kallur",
                        total_cases=10,
                        total_deaths=5,
                        total_recovered_cases=3,
                        active_cases=2
                    )
                ],
                total_cases=10,
                total_deaths=5,
                total_recovered_cases=3,
                active_cases=2
            )
    expected_result = {
            "district_id":1,
            "district_name":"Kallur",
            "mandals":[
                {
                    "mandal_id":1,
                    "mandal_name":"Kallur",
                    "total_cases":10,
                    "total_deaths":5,
                    "total_recovered_cases":3,
                    "active_cases":2
                }
            ],
            "total_cases":10,
            "total_deaths":5,
            "total_recovered_cases":3,
            "active_cases":2
        }
    storage = create_autospec(DistrictStorageInterface)
    storage.get_district_cumulative_report.return_value = report

    presenter = create_autospec(PresenterInterface)
    presenter.get_response_for_district_cumulative_report.return_value = \
        expected_result
    interactor = GetDistrictCumulativeReport(storage=storage,
        presenter=presenter)
    # Act
    result = interactor.get_district_cumulative_report(
        till_date=till_date, district_id=district_id
    )
    # Assert
    assert result == expected_result
    presenter.get_response_for_district_cumulative_report\
             .assert_called_once_with(report)