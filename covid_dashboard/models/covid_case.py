import datetime
from django.db import models
from django.core.exceptions import ValidationError
from covid_dashboard.models import Mandal
from covid_dashboard.constants.enums import Status

class ValidateNumbers:
    
    def validate_total_confirmed(self, total_confirmed):
        if total_confirmed<0:
            raise ValidationError(
                'total_confirmed value must be non-negative number')

    def validate_total_deaths(self, total_deaths):
        if total_deaths<0:
            raise ValidationError(
                'total_deaths value must be non-negative number')

    def validate_total_recovered(self, total_recovered):
        if total_recovered<0:
            raise ValidationError(
                'total_recovered value must be non-negative number')

class Stats(models.Model):
    mandal = models.ForeignKey(Mandal, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())
    total_confirmed = models.IntegerField(default=0,
        validators=[ValidateNumbers.validate_total_confirmed])
    total_deaths=models.IntegerField(default=0,
        validators=[ValidateNumbers.validate_total_deaths])
    total_recovered=models.IntegerField(default=0,
        validators=[ValidateNumbers.validate_total_recovered])