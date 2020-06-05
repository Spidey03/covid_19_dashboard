import pytest
from datetime import datetime
from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *


@pytest.fixture
def useraccount():
    username = "user1"
    password = "password1"
    user = User.objects.create(
        username=username,
        password=password
    )
    return user


@pytest.fixture
def daily_cumulative_report():
    report = {
        "daily_cumulative": [
            {
                "date":datetime.now().date(),
                "total_cases":10,
                "total_deaths":1,
                "total_recovered_cases":5,
                "active_cases":4
            }
        ]
    }
    return report

@pytest.fixture
def mandals():
    mandals=Mandal.objects.create(name='Kalluru', district_id=1)
    return mandals

@pytest.fixture
def district():
    districts = District.objects.create(name="Kurnool", state_id=1)
    return districts

@pytest.fixture
def districts():
    districts = District.objects.bulk_create(
        District(name="Kurnool", state_id=1),
        District(name="Kadapa", state_id=1)
    )
    return districts

@pytest.fixture
def states():
    states = State.objects.create(name="Andrapradesh")
    return states

@pytest.fixture
def stats():
    stats=Stats.objects.create(total_confirmed=10, total_deaths=1, total_recovered=5, mandal_id=1)
# kallur_mandal_dto = MandalDto(
#     mandal_id=1,
#     mandal_name="Kalluru"
#     )

# pkbr_mandal_dto = MandalDto(
#     mandal_id=2,
#     mandal_name="Peddakadaburu"
#     )

# kurnool = DistrictDto(
#     district_id=1,
#     district_name="Kurnool"
# )

# ap = StateDto(
#     state_id=1,
#     state_name="Andrapradesh"
# )

# covid1 = CovidCase(
#     case_id=1,
#     mandal_id=1,
#     district_id=1,
#     state_id=1,
#     created_on=datetime.now().date()
# )

# covid2 = CovidCase(
#     case_id=2,
#     mandal_id=1,
#     district_id=1,
#     state_id=1,
#     created_on=datetime.now().date()
# )

# daily_state_report_dto = DailyStateReportDto(
#         state = ap,
#         districts = [kurnool],
#         cases = [covid1, covid2]
#     )


cumulative_state_report_dto = CumulativeReportOnSpecificDay(
    date=datetime.now().date(),
    total_cases=10,
    total_deaths=1,
    total_recovered_cases=5,
    active_cases=4
)

daily_cumulative_report_dto = DailyCumulativeReport(
    report=[cumulative_state_report_dto]
)


#state_wise_cumulative_report
districtstatdto = DistrictStatDto(
    district_id=1,
    district_name="Kadapa",
    date=datetime.now().date(),
	total_cases=10,
	total_deaths=0,
	total_recovered_cases=10,
	active_cases=0
)

statedto = StateDto(
    state_id=1,
    state_name='Andrapradesh',
    stats=[districtstatdto]
)

state_dto_with_metrics = StateStatsDtoWithMetrics(
        state_id=1,
        state_name='Andrapradesh',
        stats=[districtstatdto],
        total_cases=10,
    	total_deaths=0,
    	total_recovered_cases=10,
    	active_cases=0
    )

state_stats_with_metrics = {
  "state_name": "Andrapradesh",
  "districts": [
    {
      "district_id": 1,
      "district_name": "Kadapa",
      "total_cases": 10,
      "total_deaths": 0,
      "total_recovered_cases": 10,
      "active_cases": 0
    }
  ],
  "total_cases": 10,
  "total_deaths": 0,
  "total_recovered_cases": 10,
  "active_cases": 0
}



# district daily cumulative report
dist_daily_cumulative_report_dto = DistrictCumulativeReportOnSpecificDay(
    district_id=1,
    district_name='Kadapa',
    report=[cumulative_state_report_dto]
)

list_district_daily_cumulative_report_dto = \
    ListDistrictDailyCumulativeReport(
        state_name="Andrapradesh",
        districts=[dist_daily_cumulative_report_dto]
    )

list_district_daily_cumulative_report = {
    "state_name":"Andrapradesh",
    "districts":[
        {
            "district_id":1,
            "district_name":"Kadapa",
            "daily_cumulative":{
                "total_cases":10,
                "total_deaths":1,
                "total_recovered_cases":5,
                "active_cases":4
            }
        }
    ]
}

district_id = 1
districts_df = defaultdict(list)
district_statistics = defaultdict(int)
district_statistics['date'] = datetime.now().date()
district_statistics['total_cases'] = 10
district_statistics['total_deaths'] = 1
district_statistics['total_recovered_cases'] = 5
district_statistics['active_cases'] = 4
districts_df[district_id].append(district_statistics)
district_statistics = defaultdict(int)
district_statistics['date'] = datetime.now().date()
district_statistics['total_cases'] = 9
district_statistics['total_deaths'] = 5
district_statistics['total_recovered_cases'] = 4
district_statistics['active_cases'] = 0
districts_df[district_id].append(district_statistics)



district_daily_report = DailyCumulativeDistrictWise(
    state_name="Andhrapradesh",
    districts={
            1: {
                'district_id': 1,
                'district_name': 'Kurnool'
            }
        },
    reports=districts_df
)

district_daily_report_reponse = {
    "state_name":"Andhrapradesh",
    "districts":[
        {
            "district_id":1,
            "district_name":"Kurnool",
            "daily_cumulative":
                [
                    {
                        "date":datetime.now().date(),
                        "total_cases":10,
                        "total_deaths":1,
                        "total_recovered_cases":5,
                        "active_cases":4
                    },
                    {
                        "date":datetime.now().date(),
                        "total_cases":9,
                        "total_deaths":5,
                        "total_recovered_cases":4,
                        "active_cases":0
                    }
                ]
        }
    ]
}




# ---- get_report of state for a date

state_report_for_date = StateReportForADate(
	state_name="Andrapradesh",
	districts=[
	    DistrictReportForADate(
            district_id=1,
        	district_name="Kurnool",
        	total_cases=15,
        	total_recovered_cases=5,
        	total_deaths=0,
        ),
        DistrictReportForADate(
            district_id=2,
        	district_name="Kadapa",
        	total_cases=20,
        	total_recovered_cases=8,
        	total_deaths=0,
        ),
        DistrictReportForADate(
            district_id=3,
        	district_name="Nellore",
        	total_cases=0,
        	total_recovered_cases=0,
        	total_deaths=0,
        )
	],
	total_cases=35,
	total_recovered_cases=13,
	total_deaths=0
)