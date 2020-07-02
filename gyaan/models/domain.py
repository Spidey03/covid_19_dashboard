from datetime import datetime

from django.db import models

from gyaan.models import User

class Domain(models.Model):

    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    picture = models.CharField(max_length=220)

    experts = models.ManyToManyField(User,
        through = "DomainExpert",
        related_name='expert_domains'
    )

    members = models.ManyToManyField(User,
        through = "DomainMembers",
        related_name='members_domains'
    )

    def __str__(self):
        return self.name
