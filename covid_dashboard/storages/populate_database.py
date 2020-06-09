import datetime
from covid_dashboard.models  import *


states = State.objects.bulk_create(
    [
        State(name="Andrapradesh"),
        State(name='Telangana')
    ]
)

districts=District.objects.bulk_create(
    [
        District(state_id=1, name='Kurnool'),
        District(state_id=1, name='Nellore'),
        District(state_id=1, name='Ananthapuram')
    ]
)

mandals = Mandal.objects.bulk_create(
    [
        Mandal(district_id=1, name='Kallur'),
        Mandal(district_id=1, name='Adoni'),
        Mandal(district_id=1, name='Kodumur'),
        Mandal(district_id=2, name='Kota'),
        Mandal(district_id=2, name='Kavali'),
        Mandal(district_id=2, name='Kovuru'),
        Mandal(district_id=3, name='Kadiri'),
        Mandal(district_id=3, name='Hindupur'),
        Mandal(district_id=3, name='Parigi')
    ]
)

stats = Stats.objects.bulk_create(
        [
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=5, total_deaths=1, total_recovered=2),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=5, total_deaths=2, total_recovered=0),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=8, total_deaths=1, total_recovered=3),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=26),
                  total_confirmed=10, total_deaths=0, total_recovered=5),
            Stats(mandal_id=1, date=datetime.date(year=2020, month=5, day=28),
                  total_confirmed=1, total_deaths=0, total_recovered=0),

            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=0, total_deaths=0, total_recovered=0),
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=5, total_deaths=2, total_recovered=0),
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=8, total_deaths=1, total_recovered=0),
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=26),
                  total_confirmed=10, total_deaths=0, total_recovered=5),
            Stats(mandal_id=2, date=datetime.date(year=2020, month=5, day=28),
                  total_confirmed=1, total_deaths=0, total_recovered=0),

            Stats(mandal_id=4, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=10, total_deaths=4, total_recovered=1),
            Stats(mandal_id=4, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=3, total_deaths=2, total_recovered=0),
            Stats(mandal_id=4, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=8, total_deaths=1, total_recovered=3),
            Stats(mandal_id=4, date=datetime.date(year=2020, month=5, day=25),
                  total_confirmed=5, total_deaths=0, total_recovered=5),
            Stats(mandal_id=4, date=datetime.date(year=2020, month=5, day=26),
                  total_confirmed=1, total_deaths=0, total_recovered=0),

            Stats(mandal_id=5, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=15, total_deaths=1, total_recovered=7),
            Stats(mandal_id=5, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=10, total_deaths=2, total_recovered=0),
            Stats(mandal_id=5, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=0, total_deaths=0, total_recovered=0),
            Stats(mandal_id=5, date=datetime.date(year=2020, month=5, day=25),
                  total_confirmed=10, total_deaths=5, total_recovered=1),
            Stats(mandal_id=5, date=datetime.date(year=2020, month=5, day=28),
                  total_confirmed=1, total_deaths=0, total_recovered=0),

            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=15, total_deaths=1, total_recovered=7),
            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=20, total_deaths=2, total_recovered=5),
            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=1, total_deaths=0, total_recovered=0),
            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=25),
                  total_confirmed=10, total_deaths=4, total_recovered=1),
            Stats(mandal_id=6, date=datetime.date(year=2020, month=5, day=28),
                  total_confirmed=1, total_deaths=0, total_recovered=0),

            Stats(mandal_id=8, date=datetime.date(year=2020, month=5, day=22),
                  total_confirmed=1, total_deaths=1, total_recovered=0),
            Stats(mandal_id=8, date=datetime.date(year=2020, month=5, day=23),
                  total_confirmed=10, total_deaths=2, total_recovered=3),
            Stats(mandal_id=8, date=datetime.date(year=2020, month=5, day=24),
                  total_confirmed=3, total_deaths=1, total_recovered=2),
            Stats(mandal_id=8, date=datetime.date(year=2020, month=5, day=26),
                  total_confirmed=4, total_deaths=0, total_recovered=0),
            Stats(mandal_id=8, date=datetime.date(year=2020, month=5, day=30),
                  total_confirmed=3, total_deaths=0, total_recovered=2),
        ]
)