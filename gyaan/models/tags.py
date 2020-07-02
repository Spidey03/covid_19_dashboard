from django.db import models

from gyaan.models import Domain


class Tags(models.Model):

    domain = models.ForeignKey(Domain,
        on_delete=models.CASCADE,
        related_name='tags',
        null=True
    )
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name