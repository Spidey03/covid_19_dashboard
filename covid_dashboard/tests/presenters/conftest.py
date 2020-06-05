from collections import defaultdict
from covid_dashboard.interactors.storages.dtos import *
import datetime




districts = [
    DistrictCumulativeReportOnSpecificDay(
        district_id=1,
        district_name='Kurnool',
        report=[
            CumulativeReportOnSpecificDay(
                date=datetime.date(year=2020, month=5, day=26),
                total_cases=40,
                total_deaths=3,
                total_recovered_cases=37,
                active_cases=0
            ),
        ]
    ),
    DistrictCumulativeReportOnSpecificDay(
        district_id=2,
        district_name='Nellore',
        report=[
            CumulativeReportOnSpecificDay(
                date=datetime.date(year=2020, month=5, day=26),
                total_cases=30,
                total_deaths=3,
                total_recovered_cases=27,
                active_cases=0
            ),
            CumulativeReportOnSpecificDay(
                date=datetime.date(year=2020, month=5, day=27),
                total_cases=40,
                total_deaths=3,
                total_recovered_cases=37,
                active_cases=0
            )
        ]
    ),
]

list_district_daily_cumulative = ListDistrictDailyCumulativeReport(
    state_name="Andhrapradesh",
    districts=districts
)