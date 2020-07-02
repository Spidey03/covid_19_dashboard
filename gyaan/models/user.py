from django.contrib.auth.models import AbstractUser
from django.db import models

from gyaan.constants.enums import Role

# Create your models here.

class User(AbstractUser) :
    name = models.CharField(max_length = 100)
    profile_pic = models.CharField(max_length = 200, null=True)
    description = models.CharField(max_length=500, null=True)

    RoleChoice = (
        (Role.DESIGNER.value, Role.DESIGNER),
        (Role.DEVELOPER.value, Role.DEVELOPER)
    )
    role = models.CharField(max_length=50, choices=RoleChoice,
                            default=None, null=True)
