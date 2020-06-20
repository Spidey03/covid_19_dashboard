import pytest
import datetime
from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *

@pytest.fixture()
def user():
    username = "Loki"
    password = "Asgardian84"
    user = User.objects.create(
        username=username,
    )
    user.set_password(password)
    user.save()
    return user


@pytest.fixture()
def states():
    states = State.objects.bulk_create([
        State(name="Andrapradesh"),
        State(name="Telangana")
    ])
    return states

@pytest.fixture()
def state_dto():
    state_dto = StateDto(
        state_id=1,
        state_name="Andrapradesh"
    )
    return state_dto

@pytest.fixture()
def districts():
    districts = District.objects.bulk_create([
        District(state_id=1, name="Kurnool"),
        District(state_id=1, name="Nellore"),
        District(state_id=1, name="Kadapa"),
        District(state_id=1, name="E.Godavari")
    ])
    return districts

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
        ),
        DistrictDto(
            district_id=3,
            district_name="Kadapa"
        ),
        DistrictDto(
            district_id=4,
            district_name="E.Godavari"
        )
    ]
    return district_dtos

@pytest.fixture()
def mandals():
    mandals = Mandal.objects.bulk_create([
        Mandal(name="Peddakadabur", district_id=1),
        Mandal(name="Kallur", district_id=1),
        Mandal(name="Adoni", district_id=1),

        Mandal(name="Kota", district_id=2),
        Mandal(name="Kavali", district_id=2),
        Mandal(name="Gudur", district_id=2),

        Mandal(name="VemCity", district_id=3),
        Mandal(name="Pulivendula", district_id=3),
        Mandal(name="Aathreyapuram", district_id=3),
        Mandal(name="Ravulapalem", district_id=3),
        
    ])

@pytest.fixture()
def stats():
    stats = Stats.objects.bulk_create([
        Stats(mandal_id=1, total_confirmed=10, total_recovered=5,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=25)),
        Stats(mandal_id=1, total_confirmed=5, total_recovered=1,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        Stats(mandal_id=1, total_confirmed=5, total_recovered=1,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=27)),
        Stats(mandal_id=2, total_confirmed=4, total_recovered=2,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=25)),
        Stats(mandal_id=2, total_confirmed=5, total_recovered=1,
            total_deaths=2, date=datetime.date(year=2020, month=5, day=26)),
        Stats(mandal_id=2, total_confirmed=5, total_recovered=1,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=27)),

        Stats(mandal_id=4, total_confirmed=0, total_recovered=0,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=25)),
        Stats(mandal_id=4, total_confirmed=5, total_recovered=3,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        Stats(mandal_id=4, total_confirmed=5, total_recovered=1,
            total_deaths=3, date=datetime.date(year=2020, month=5, day=27)),
        Stats(mandal_id=5, total_confirmed=10, total_recovered=0,
            total_deaths=3, date=datetime.date(year=2020, month=5, day=25)),
        Stats(mandal_id=5, total_confirmed=1, total_recovered=0,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        Stats(mandal_id=5, total_confirmed=3, total_recovered=1,
            total_deaths=1, date=datetime.date(year=2020, month=5, day=27)),
        Stats(mandal_id=6, total_confirmed=10, total_recovered=0,
            total_deaths=3, date=datetime.date(year=2020, month=5, day=25)),
        Stats(mandal_id=6, total_confirmed=1, total_recovered=0,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        Stats(mandal_id=6, total_confirmed=3, total_recovered=1,
            total_deaths=1, date=datetime.date(year=2020, month=5, day=27)),

        Stats(mandal_id=7, total_confirmed=1, total_recovered=0,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        Stats(mandal_id=7, total_confirmed=3, total_recovered=1,
            total_deaths=1, date=datetime.date(year=2020, month=5, day=27)),
    ])
    return stats