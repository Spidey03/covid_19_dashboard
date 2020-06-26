import factory
import datetime
from covid_dashboard import models


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.User

    name = factory.Sequence(lambda id: f'user{id}')
    username = factory.Sequence(lambda id: f'username{id}')
    

class StateFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.State

    name = factory.Sequence(lambda id: f'state{id}')

class DistrictFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.District

    name = factory.Sequence(lambda id: f'district{id}')
    state = factory.SubFactory(StateFactory)

class MandalFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Mandal

    name = factory.Sequence(lambda id: f'mandal{id}')
    district = factory.SubFactory(DistrictFactory)

class StatsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Stats

    total_confirmed = 5
    total_recovered = 3
    total_deaths = 1
    date = factory.LazyFunction(datetime.date)
    mandal_id = factory.SubFactory(MandalFactory)
