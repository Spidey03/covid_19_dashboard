import pytest
import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.interactors.storages.dtos\
    import DistrictReportDto, MandalReportDto

def test_get_district_cumulative_report_presenter():
    # Arrange
    report = DistrictReportDto(
        # district_id=2,
        district_name='Nellore',
        mandals=[
            MandalReportDto(
                mandal_id=4,
                mandal_name='Kota',
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0,
                active_cases=0
            ),
            MandalReportDto(
                mandal_id=5,
                mandal_name='Kavali',
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0,
                active_cases=0
            ),
            MandalReportDto(
                mandal_id=6,
                mandal_name='Kovuru',
                total_cases=40,
                total_deaths=0,
                total_recovered_cases=20,
                active_cases=20
            )
        ],
        total_cases=40,
        total_deaths=0,
        total_recovered_cases=20,
        active_cases=20
    )

    presenter = PresenterImplementation()
    expected_result =  {
        # 'district_id': 2,
        'district_name': 'Nellore',
        'mandals': [
            {
                'mandal_id': 4,
                'mandal_name': 'Kota',
                'total_cases': 0,
                'total_recovered_cases': 0,
                'total_deaths': 0,
                'active_cases': 0
            },
            {
                'mandal_id': 5,
                'mandal_name': 'Kavali',
                'total_cases': 0,
                'total_recovered_cases': 0,
                'total_deaths': 0,
                'active_cases': 0
            },
            {
                'mandal_id': 6,
                'mandal_name': 'Kovuru',
                'total_cases': 40,
                'total_recovered_cases': 20,
                'total_deaths': 0,
                'active_cases': 20
            }
        ],
        'total_cases': 40,
        'total_recovered_cases': 20,
        'total_deaths': 0,
        'active_cases': 20
    }


    # Act
    result = presenter.get_response_for_district_cumulative_report(report)

    # Assert
    assert result == expected_result