import pytest
from covid_dashboard.models import *

@pytest.fixture
def user():
    username = "Loki"
    password = "Asgardian84"
    user = User.objects.create(
        username=username,
    )
    user.set_password(password)
    user.save()
    return user