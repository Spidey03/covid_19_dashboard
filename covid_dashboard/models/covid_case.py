import datetime
from django.db import models
from covid_dashboard.models import Mandal
from covid_dashboard.constants.enums import Status

# class Case(models.Model):
#     mandal = models.ForeignKey(
#         Mandal, models.SET_NULL, null=True
#     ),
#     confirmed = models.BooleanField(default=True)
#     status = models.CharField(max_length=100,
#         choices=[(status, status.value) for status in Status]
#     )

# CONFIRMED 

# RECOVERED
# ACTIVE
# DEAD


class Stats(models.Model):
    mandal = models.ForeignKey(Mandal, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())
    total_confirmed = models.IntegerField(default=0)
    total_deaths=models.IntegerField(default=0)
    total_recovered=models.IntegerField(default=0)