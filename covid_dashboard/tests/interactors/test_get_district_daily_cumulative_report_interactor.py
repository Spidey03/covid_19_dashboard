import pytest
from unittest.mock import create_autospec
from covid_dashboard.interactors.storages.district_storage_interface\
    import DistrictStorageInterface
from covid_dashboard.interactors.presenters.presenter_interface\
    import PresenterInterface
from covid_dashboard.interactors.get_district_daily_cumulative_report_interactor\
    import GetDistrictDailyCumulativeReport
from covid_dashboard.tests.interactors.conftest import *


def get_district_daily_cumulative_report_interactor():
    # Arrange
    storage = create_autospec(DistrictStorageInterface)
    storage.get_district_daily_cumulative_report.return_value = \
        district_daily_report
    
    presenter = create_autospec(PresenterInterface)
    presenter.get_district_daily_cumulative_report_response.return_value = \
        district_daily_report_reponse
    
    interactor = GetDistrictDailyCumulativeReport(
        storage=storage, presenter=presenter)

    # Act
    result = interactor.get_district_daily_cumulative_report()

    # Assert
    storage.get_district_daily_cumulative_report.assert_called_once()
    presenter.get_district_daily_cumulative_report_response. \
        assert_called_once_with(list_district_daily_cumulative_report_dto)
    assert result == district_daily_report_reponse