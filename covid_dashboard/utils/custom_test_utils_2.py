import datetime
from freezegun import freeze_time
from django_swagger_utils.utils.test import CustomAPITestCase

from covid_dashboard.tests.factories \
    import UserFactory, StateFactory, DistrictFactory,\
        MandalFactory, StatsFactory

class CustomTestUtils(CustomAPITestCase):

    def reset_sequence(self):

        UserFactory.reset_sequence(0)
        StateFactory.reset_sequence(0)
        DistrictFactory.reset_sequence(0)
        MandalFactory.reset_sequence(0)
        StatsFactory.reset_sequence(0)

    def create_user(self):

        users = UserFactory.create()
        return users

    def create_state(self):

        states = StateFactory.create()
        return states

    def create_districts(self):

        districts = DistrictFactory.create_batch(size=4, state_id=1)
        return districts

    def create_mandals(self):

        mandals = MandalFactory.create_batch(size=3, district_id=1)
        mandals = MandalFactory.create_batch(size=2, district_id=2)
        mandals = MandalFactory.create_batch(size=7, district_id=3)

    def create_stats(self):

        StatsFactory.create(mandal_id=1, total_confirmed=10, total_recovered=5,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=25)),
        StatsFactory.create(mandal_id=1, total_confirmed=5, total_recovered=1,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        StatsFactory.create(mandal_id=1, total_confirmed=5, total_recovered=1,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=27)),
        StatsFactory.create(mandal_id=2, total_confirmed=4, total_recovered=2,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=25)),
        StatsFactory.create(mandal_id=2, total_confirmed=5, total_recovered=1,
            total_deaths=2, date=datetime.date(year=2020, month=5, day=26)),
        StatsFactory.create(mandal_id=2, total_confirmed=5, total_recovered=1,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=27)),

        StatsFactory.create(mandal_id=4, total_confirmed=0, total_recovered=0,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=25)),
        StatsFactory.create(mandal_id=4, total_confirmed=5, total_recovered=3,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        StatsFactory.create(mandal_id=4, total_confirmed=5, total_recovered=1,
            total_deaths=3, date=datetime.date(year=2020, month=5, day=27)),
        StatsFactory.create(mandal_id=5, total_confirmed=10, total_recovered=0,
            total_deaths=3, date=datetime.date(year=2020, month=5, day=25)),
        StatsFactory.create(mandal_id=5, total_confirmed=1, total_recovered=0,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        StatsFactory.create(mandal_id=5, total_confirmed=3, total_recovered=1,
            total_deaths=1, date=datetime.date(year=2020, month=5, day=27)),
        StatsFactory.create(mandal_id=6, total_confirmed=10, total_recovered=0,
            total_deaths=3, date=datetime.date(year=2020, month=5, day=25)),
        StatsFactory.create(mandal_id=6, total_confirmed=1, total_recovered=0,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        StatsFactory.create(mandal_id=6, total_confirmed=3, total_recovered=1,
            total_deaths=1, date=datetime.date(year=2020, month=5, day=27)),

        StatsFactory.create(mandal_id=7, total_confirmed=1, total_recovered=0,
            total_deaths=0, date=datetime.date(year=2020, month=5, day=26)),
        StatsFactory.create(mandal_id=7, total_confirmed=3, total_recovered=1,
            total_deaths=1, date=datetime.date(year=2020, month=5, day=27))
        StatsFactory.create(mandal_id=7, total_confirmed=3, total_recovered=1,
            total_deaths=1, date=datetime.date(year=2020, month=5, day=30))

    def create_database(self):
        self.reset_sequence()
        self.create_user()
        self.create_state()
        self.create_districts()
        self.create_mandals()
        self.create_stats()
