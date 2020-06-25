import pytest
import datetime
from covid_dashboard.interactors.storages.dtos import *


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

@pytest.fixture
def district_report_dtos():
    district_report_dtos = [
        DistrictReportDto(
            district_id=1,
            total_confirmed=10,
            total_recovered=1,
            total_deaths=3,
        ),
        DistrictReportDto(
            district_id=2,
            total_confirmed=0,
            total_recovered=0,
            total_deaths=0,
        )
    ]
    return district_report_dtos

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


@pytest.fixture
def state_cumulative_report_response():
    expected_output = {
        "state_name": "Andrapradesh",
        "districts": [
            {
                "district_name": 1,
                "total_cases": 10,
                "total_deaths": 3,
                "total_recovered_cases": 1,
                "active_cases": 6
            },
            {
                "district_name": 2,
                "total_cases": 0,
                "total_deaths": 0,
                "total_recovered_cases": 0,
                "active_cases": 0
            }
        ],
        "total_cases": 10,
        "total_deaths": 3,
        "total_recovered_cases": 1,
        "active_cases": 6
    }
    return expected_output


@pytest.fixture()
def state_daily_report_dtos():
    daily_report_dtos = [
        DayReportDto(
            date=datetime.date(year=2020, month=5, day=2),
            total_confirmed=10,
            total_recovered=5,
            total_deaths=1
        ),
        DayReportDto(
            date=datetime.date(year=2020, month=5, day=4),
            total_confirmed=5,
            total_recovered=3,
            total_deaths=1
        ),
        DayReportDto(
            date=datetime.date(year=2020, month=5, day=5),
            total_confirmed=2,
            total_recovered=1,
            total_deaths=0
        )
    ]
    return daily_report_dtos

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

@pytest.fixture()
def state_day_wise_report_response():

    expected_output = {
        "daily_cumulative":[
            {
                "date":"2020-05-02",
                "total_cases": 10,
                "total_deaths": 5,
                "total_recovered_cases": 1,
                "active_cases": 4
            },
            {
                "date":"2020-05-03",
                "total_cases": 10,
                "total_deaths": 5,
                "total_recovered_cases": 1,
                "active_cases": 4
            },
            {
                "date":"2020-05-04",
                "total_cases": 5,
                "total_deaths": 3,
                "total_recovered_cases": 1,
                "active_cases": 1
            },
            {
                "date":"2020-05-05",
                "total_cases": 2,
                "total_deaths": 1,
                "total_recovered_cases": 0,
                "active_cases": 1
            }
        ]
    }
    return expected_output