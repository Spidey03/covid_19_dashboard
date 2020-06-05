import datetime
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.tests.storages.conftest\
    import daily_cumulative_report_dto
from covid_dashboard.interactors.storages.dtos\
    import DailyCumulativeReport, CumulativeReportOnSpecificDay


def test_get_daily_cumulative_report_for_district():
    # Arrange
    presenter = PresenterImplementation()
    reports = DailyCumulativeReport(
        report = [
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 22),
                total_cases=6,
                total_deaths=3,
                total_recovered_cases=5,
                active_cases=-2
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 23),
                total_cases=28,
                total_deaths=8,
                total_recovered_cases=13,
                active_cases=7
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 24),
                total_cases=57,
                total_deaths=27,
                total_recovered_cases=17,
                active_cases=13
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(2020, 5, 25),
                total_cases=87,
                total_deaths=32,
                total_recovered_cases=27,
                active_cases=28
            )
        ]
    )
    expected_response ={
        'daily_cumulative':[
            {
                'date': datetime.date(2020, 5, 22),
                'total_cases': 6,
                'total_deaths': 3,
                'total_recovered_cases': 5,
                'active_cases': -2
            },
            {
                'date': datetime.date(2020, 5, 23),
                'total_cases': 28,
                'total_deaths': 8,
                'total_recovered_cases': 13,
                'active_cases': 7
            },
            {
                'date': datetime.date(2020, 5, 24),
                'total_cases': 57,
                'total_deaths': 27,
                'total_recovered_cases': 17,
                'active_cases': 13
            },
            {
                'date': datetime.date(2020, 5, 25),
                'total_cases': 87,
                'total_deaths': 32,
                'total_recovered_cases': 27,
                'active_cases': 28
            }
        ]
    }
    
    # Act
    response = presenter.get_response_for_daily_cumulative_report_for_district(
        reports)

    # Assert
    assert response == expected_response