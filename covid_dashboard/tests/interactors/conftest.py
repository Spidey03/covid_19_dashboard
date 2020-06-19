import pytest
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
        ),
    ]
    return district_report_dtos

@pytest.fixture
def state_cumulative_report_dto(state_dto, district_report_dtos):
    state_cumulative_report_dto = StateCumulativeReportDto(
        state=state_dto,
        districts=[1,2],
        reports=district_report_dtos
    )
    return state_cumulative_report_dto


@pytest.fixture
def state_cumulative_report_response():
    expected_output = {
        "state_name": "Andrapradesh",
        "districts": [
            {
                "district_id": 1,
                "total_cases": 10,
                "total_deaths": 3,
                "total_recovered_cases": 1,
                "active_cases": 6
            },
            {
                "district_id": 2,
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