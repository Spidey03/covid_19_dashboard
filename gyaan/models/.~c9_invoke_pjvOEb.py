from datetime import datetime

from django.db import models

from gyaan.models import User

class Domain:
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    picture = models.CharField(max_length=120)
    expert = models.ManyToManyField(User,
        through = "DomainExpert"
    )
