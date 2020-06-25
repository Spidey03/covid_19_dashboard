import datetime
import pytest
from common.dtos import UserAuthTokensDTO
from covid_dashboard.interactors.storages.dtos import *

@pytest.fixture
def user_auth_token_dto():
    user_auth_token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        refresh_token="DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        expires_in=datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    )
    return user_auth_token_dto

@pytest.fixture
def login_response():
    login_response = {
        "user_id":1,
        "access_token":"HiplEtNJKFIPRsyDSDqrH7GHkSHSzq",
        "refresh_token":"DIxY1vyGQRkN7zJKqE4MZaq73tpKDj3ee444444444444e",
        "expires_in":datetime.datetime(2020, 9, 21, 3, 45, 50, 163595)
    }
    return login_response

@pytest.fixture()
def state_dto():
    state_dto = StateDto(
        state_id=1,
        state_name="Andrapradesh"
    )
    return state_dto

@pytest.fixture()
def district_dtos():
    district_dtos = [
        DistrictDto(
            district_id=1,
            district_name="Kurnool"
        ),
        DistrictDto(
            district_id=2,
            district_name="Nellore"
        )
    ]
    return district_dtos


@pytest.fixture()
def district_total_report_dto():
    district_total_report_dto = [
        DistrictTotalReportDto(
            district_id=1,
            total_confirmed=10,
            total_recovered=1,
            total_deaths=3,
            active_cases=6
        ),
        DistrictTotalReportDto(
            district_id=2,
            total_confirmed=0,
            total_recovered=0,
            total_deaths=0,
            active_cases=0
        )
    ]
    return district_total_report_dto

@pytest.fixture()
def complete_state_cumulative_report_dto(state_dto, district_dtos, district_total_report_dto):
    complete_state_cumulative_report_dto = CompleteStateCumulativeReportDto(
        state=state_dto,
        districts=district_dtos,
        district_reports=district_total_report_dto,
        state_cumulative_report=TotalReportDto(
            total_confirmed=10,
            total_recovered=1,
            total_deaths=3,
            active_cases=6
        )
    )
    return complete_state_cumulative_report_dto


@pytest.fixture()
def state_day_wise_report_dtos():
    day_wise_report_dtos = [
        DayWiseReportDto(
            date=datetime.date(year=2020, month=5, day=2),
            total_confirmed=10,
            total_recovered=5,
            total_deaths=1,
            active_cases=4
        ),
        DayWiseReportDto(
            date=datetime.date(year=2020, month=5, day=3),
            total_confirmed=10,
            total_recovered=5,
            total_deaths=1,
            active_cases=4
        ),
        DayWiseReportDto(
            date=datetime.date(year=2020, month=5, day=4),
            total_confirmed=15,
            total_recovered=8,
            total_deaths=2,
            active_cases=5
        ),
        DayWiseReportDto(
            date=datetime.date(year=2020, month=5, day=5),
            total_confirmed=17,
            total_recovered=9,
            total_deaths=2,
            active_cases=6
        )
    ]
    return day_wise_report_dtos