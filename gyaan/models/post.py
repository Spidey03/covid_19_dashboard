from datetime import datetime

from django.db import models

from gyaan.models import User
from gyaan.models.domain import Domain

class Post(models.Model):
    is_approved = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User,
        on_delete = models.CASCADE,
        related_name='posts'
    )
    domain = models.ForeignKey(Domain,
        on_delete=models.CASCADE,
        related_name='posts'
    )
