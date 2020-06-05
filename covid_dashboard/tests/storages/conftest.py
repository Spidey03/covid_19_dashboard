import pytest
import datetime
from covid_dashboard.models import User, State, District, Mandal, Stats
from covid_dashboard.interactors.storages.dtos import \
    (CumulativeReportOnSpecificDay, DailyCumulativeReport,
     DistrictStatDto, StateDto, DistrictCumulativeReportOnSpecificDay,
     CumulativeReportOnSpecificDay, ListDistrictDailyCumulativeReport
    )

@pytest.fixture
def useraccount():
    username = "user1"
    password = "password1"
    user = User.objects.create(
        username=username,
    )
    user.set_password(password)
    user.save()
    return user

@pytest.fixture
def states():
    states = State.objects.bulk_create(
        [State(name="Andrapradhesh")]
    )
    return states


@pytest.fixture
def districts():
    districts = District.objects.bulk_create(
        [District(name="Kurnool", state_id=1),
         District(name="Nellore", state_id=1)
        ]
    )
    return districts

@pytest.fixture
def districts2():
    districts = District.objects.bulk_create(
        [District(name="Kurnool", state_id=1),
         District(name="Nellore", state_id=1),
         District(name="Kadapa", state_id=1)
        ]
    )
    return districts


@pytest.fixture
def mandals():
    mandals = Mandal.objects.bulk_create(
        [Mandal(name="Kalluru", district_id=1),
         Mandal(name="Kota", district_id=2),
         
        ]
    )
    return mandals

@pytest.fixture
def mandals2():
    mandals = Mandal.objects.bulk_create(
        [Mandal(name="Kalluru", district_id=1),
         Mandal(name="Kota", district_id=2),
         Mandal(name="VemCity", district_id=3)
        ]
    )
    return mandals

@pytest.fixture
def stats():
    stats = Stats.objects.bulk_create(
        [
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=28),
                total_confirmed=10, total_recovered=10, total_deaths=0
            ),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=28),
                total_confirmed=10, total_recovered=10, total_deaths=0
            )
        ]
    )
    return stats

@pytest.fixture
def stats2():
    stats = Stats.objects.bulk_create(
        [
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=28),
                total_confirmed=10, total_recovered=10, total_deaths=0
            ),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=28),
                total_confirmed=10, total_recovered=10, total_deaths=0
            ),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=28),
                total_confirmed=0, total_recovered=0, total_deaths=0
            )
        ]
    )
    return stats


# test_get_daily_cumulative_report_storage
cumulate_report_on_specific_day = CumulativeReportOnSpecificDay(
        date=datetime.date(year=2020, month=5, day=28),
        total_cases=20,
        total_deaths=0,
        total_recovered_cases=20,
        active_cases=0
    )

daily_cumulative_report_dto = DailyCumulativeReport(
        report=[cumulate_report_on_specific_day]
    )
    

cumulate_report_on_specific_day_kurnool = DistrictStatDto(
        district_id=1,
        district_name='Kurnool',
        date=datetime.date(year=2020, month=5, day=28),
        total_cases=10,
        total_deaths=0,
        total_recovered_cases=10,
        active_cases=0
    )
cumulate_report_on_specific_day_nellore = DistrictStatDto(
        district_id=2,
        district_name='Nellore',
        date=datetime.date(year=2020, month=5, day=28),
        total_cases=10,
        total_deaths=0,
        total_recovered_cases=10,
        active_cases=0
    )

dist_daily_cumulative_report_dto_kurnool = DistrictCumulativeReportOnSpecificDay(
    district_id=1,
    district_name='Kurnool',
    report=[cumulate_report_on_specific_day_kurnool]
)
dist_daily_cumulative_report_dto_nellore = DistrictCumulativeReportOnSpecificDay(
    district_id=1,
    district_name='Nellore',
    report=[cumulate_report_on_specific_day_nellore]
)
list_dist_stat = [cumulate_report_on_specific_day_kurnool,
                  cumulate_report_on_specific_day_nellore]
                 
list_dist_daily_cumulative = ListDistrictDailyCumulativeReport(
    state_name="Andhrapradesh",
    districts=[dist_daily_cumulative_report_dto_kurnool,
            dist_daily_cumulative_report_dto_nellore]
)
# test_get_state_wise_report_storage
till_date = datetime.date(year=2020, month=5, day=28)
districts_cumulative_report = DistrictStatDto(
        district_id=1,
        district_name='Kurnool',
        date=till_date,
        total_cases=10,
	    total_deaths=10,
        total_recovered_cases=10,
	    active_cases=10
    )

list_cumulative_districts = [
    DistrictStatDto(
        district_id=1,
        district_name='Kurnool',
        date=datetime.date(2020, 5, 28),
        total_cases=10,
        total_deaths=0,
        total_recovered_cases=10,
        active_cases=0
    ),
    DistrictStatDto(
        district_id=2,
        district_name='Nellore',
        date=datetime.date(2020, 5, 28),
        total_cases=10,
        total_deaths=0,
        total_recovered_cases=10,
        active_cases=0
    )
]

cumulative_state_report_dto = \
    StateDto(
        state_name='Andhrapradesh',
        state_id=1,
        stats=list_cumulative_districts
    )



till_date = datetime.date(year=1000, month=1, day=1)
districts_cumulative_report_no_cases = DistrictStatDto(
        district_id=1,
        district_name='Kurnool',
        date=till_date,
        total_cases=0,
	    total_deaths=0,
        total_recovered_cases=0,
	    active_cases=0
    )
cumulative_state_report_dto_no_cases = \
    StateDto(
        state_name='Andhrapradesh',
        state_id=1,
        stats=[
            DistrictStatDto(
                district_id=1,
                district_name='Kurnool',
                date=datetime.date(1000, 1, 1),
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0,
                active_cases=0
            ),
            DistrictStatDto(
                district_id=2,
                district_name='Nellore',
                date=datetime.date(1000, 1, 1),
                total_cases=0,
                total_deaths=0,
                total_recovered_cases=0,
                active_cases=0
            )
        ]
    )




@pytest.fixture
def districts3():
    districts = District.objects.bulk_create(
        [District(name="Kurnool", state_id=1),
         District(name="Nellore", state_id=1),
         District(name="Ananthapuram", state_id=1)
        ]
    )
    return districts


@pytest.fixture
def mandals3():
    mandals = Mandal.objects.bulk_create(
        [Mandal(name="Kalluru", district_id=1),
         Mandal(name="Adoni", district_id=1),
         Mandal(name="Kota", district_id=2),
         Mandal(name='Panyam', district_id=1),
         Mandal(name='Kadiri', district_id=3)
        ]
    )
    return mandals

@pytest.fixture
def stats3():
    stats = Stats.objects.bulk_create(
        [
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=28),
                total_confirmed=10, total_recovered=10, total_deaths=0
            ),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=28),
                total_confirmed=10, total_recovered=10, total_deaths=0
            ),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=28),
                total_confirmed=0, total_recovered=0, total_deaths=0
            ),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=27),
                total_confirmed=10, total_recovered=0, total_deaths=0
            ),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=26),
                total_confirmed=30, total_recovered=0, total_deaths=3
            )
        ]
    )
    return stats





# ------------------------ New TestCases ------------------------ #
@pytest.fixture
def all_states():
    states = State.objects.bulk_create(
        [
            State(name="Andrapradesh"),
            State(name='Telangana')
        ]
    )
    return states


@pytest.fixture
def all_districts():
    districts=District.objects.bulk_create(
        [
            District(state_id=1, name='Kurnool'),
            District(state_id=1, name='Nellore')
        ]
    )
    return districts


@pytest.fixture
def all_mandals():
    mandals = Mandal.objects.bulk_create(
        [
            Mandal(district_id=1, name='Kallur'),
            Mandal(district_id=1, name='Adoni'),
            Mandal(district_id=1, name='Kodumur'),
            Mandal(district_id=2, name='Kota'),
            Mandal(district_id=2, name='Kavali'),
            Mandal(district_id=2, name='Kovuru'),
        ]
    )
    return mandals


@pytest.fixture
def all_stats():
    stats = Stats.objects.bulk_create(
        [
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=5, total_deaths=1, total_recovered=2),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=6, total_deaths=1, total_recovered=2),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=5, total_deaths=4, total_recovered=2),
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=1, total_deaths=2, total_recovered=3),
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=6, total_deaths=1, total_recovered=4),
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=7, total_deaths=0, total_recovered=0),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=10, total_deaths=3, total_recovered=2),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=17, total_deaths=15, total_recovered=2),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=25),
                  total_confirmed=30, total_deaths=5, total_recovered=10),
            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=20),
                  total_confirmed=5, total_deaths=0, total_recovered=5),
            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=21),
                  total_confirmed=20, total_deaths=0, total_recovered=10),
            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=10, total_deaths=0, total_recovered=5),
            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=5, total_deaths=0, total_recovered=0),
        ]
    )


@pytest.fixture
def all_stats2():
    stats = Stats.objects.bulk_create(
        [
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=5, total_deaths=1, total_recovered=2),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=5, total_deaths=4, total_recovered=2),
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=7, total_deaths=0, total_recovered=0),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=10, total_deaths=3, total_recovered=2),
            Stats(mandal_id=3, date=datetime.date(year=2020, month=5, day=30),
                  total_confirmed=17, total_deaths=15, total_recovered=2),
        ]
    )