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
        model = models.State

    name = factory.Sequence(lambda id: f'district{id}')
    state = factory.Iterator(models.State.objects.all())

class MandalFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Mandal

    name = factory.Sequence(lambda id: f'mandal{id}')
    district = factory.Iterator(models.District.objects.all())

class StatsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Stats

    date = factory.LazyFunction(datetime.date)
    total_confirmed = 5
    total_recovered = 3
    total_deaths = 1
