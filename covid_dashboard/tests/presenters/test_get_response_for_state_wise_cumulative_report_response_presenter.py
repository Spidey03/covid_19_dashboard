import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.storages.conftest\
    import *


def test_get_response_for_state_wise_cumulative_report():
    # Arrange
    presenter = PresenterImplementation()
    expected_result = {
      "state_name": "Andhrapradesh",
      # "state_id":1,
    #   "date":datetime.date(year=2020, month=5, day=28),
      "districts": [
        {
          "district_id": 1,
          "district_name": "Kurnool",
          "total_cases": 10,
          "total_deaths": 0,
          "total_recovered_cases": 10,
          "active_cases": 0
        },
        {
          "district_id": 2,
          "district_name": "Nellore",
          "total_cases": 10,
          "total_deaths": 0,
          "total_recovered_cases": 10,
          "active_cases": 0
        }
      ],
      "total_cases": 20,
      "total_deaths": 0,
      "total_recovered_cases": 20,
      "active_cases": 0
    }
    

    # Act
    result = presenter.get_response_for_state_wise_cumulative_report(cumulative_state_report_dto)

    # Assert
    assert result == expected_result
