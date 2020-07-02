from django.db import models

from gyaan.models import User, Domain

class DomainExpert(models.Model):
    expert = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='domain_experts')
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE,
                               related_name='domains')

    class Meta:
        unique_together = [['expert', 'domain']]
