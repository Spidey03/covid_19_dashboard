from django.db import models

from gyaan.models import User, Domain

class DomainMembers(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='domain_members')
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE,
                               related_name='domain_members')

    class Meta:
        unique_together = [['member', 'domain']]