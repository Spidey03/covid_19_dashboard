import pytest
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.\
    get_daily_cumulative_report_for_district_interactor\
        import GetDailyCumulativeReportForDistrict
from covid_dashboard.tests.interactors.conftest import *


def get_daily_cumulative_report_for_district_interactor():
    # Arrange
    district_id = 1
    storage = create_autospec(DistrictStorageInterface)
    storage.get_daily_cumulative_report_for_district.return_value = \
        daily_cumulative_report_dto
    
    presenter = create_autospec(PresenterInterface)
    presenter.get_response_for_daily_cumulative_report_for_district.\
        return_value = daily_cumulative_report
    
    interactor = GetDailyCumulativeReportForDistrict(
        storage=storage, presenter=presenter)
    # Act
    result = interactor.get_daily_cumulative_report_for_district(
        district_id)

    # Assert
    storage.get_daily_cumulative_report_for_district\
           .assert_called_once(district_id)
    presenter.get_response_for_daily_cumulative_report_for_district\
             .assert_called_once_with(daily_cumulative_report_dto)
    assert result == daily_cumulative_report
