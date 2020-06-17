import pytest
from gyaan.interactors.storages.dtos import *

@pytest.fixture()
def domain_dto():
    domain_dto = DomainDto(
        domain_id=1,
        domain_name='CyberSecurity',
        description='CyberSecurity for white hat'
    )
    return domain_dto

@pytest.fixture()
def domain_stats():
    domain_stats = DomainStatDto(
        domain_id=1,
        followers_count=100,
        posts_count=50,
        bookmarked_count=25
    )
    return domain_stats

@pytest.fixture()
def experts():
    users = [
        UserDto(
            user_id=1,
            name="Naveen"
        ),
        UserDto(
            user_id=1,
            name="Codist"
        )
    ]
    return users

@pytest.fixture()
def domain_join_requests():
    domain_join_requests =  [
        DomainJoinRequestDto(
            request_id = 3,
            user_id = 1 
        )
    ]
    return domain_join_requests

@pytest.fixture()
def requested_users():
    requested_users = [
        UserDto(
            user_id=3,
            name="Gwen"
        )
    ]
    return requested_users

@pytest.fixture()
def response_get_domain_details():
    expected_output = {
            "domain_id":1,
            "domain_name":"CyberSecurity",
            "description":"CyberSecurity for white hat",
            "domain_stats":{
                "followers_count":100,
                "posts_count":50,
                "bookmarked_count":25
            },
            "domain_experts":[
                {
                    "user_id":1,
                    "name":"Naveen"
                },
                {
                    "user_id":2,
                    "name":"codist"
                }
            ],
            "requested_users":[
                {
                    "user_id":3,
                    "name":"Gwen"
                }
            ]
        }
    return expected_output