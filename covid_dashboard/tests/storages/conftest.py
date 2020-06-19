import pytest
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