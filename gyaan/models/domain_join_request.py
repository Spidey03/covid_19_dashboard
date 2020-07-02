from datetime import datetime

from django.db import models

from gyaan.models import User, Domain
from gyaan.constants.enums import JoinStatus


class DomainJoinRequest(models.Model):
    user = models.ForeignKey(User,
        on_delete = models.CASCADE,
        related_name='requested_user'
    )
    domain = models.ForeignKey(Domain,
        on_delete = models.CASCADE,
        related_name='requests'
    )
    StatusChoice = (
        (JoinStatus.APPROVED.value, JoinStatus.APPROVED.value),
        (JoinStatus.REJECTED.value, JoinStatus.REJECTED.value),
        (JoinStatus.REQUESTED.value, JoinStatus.REQUESTED.value)
    )
    status = models.CharField(max_length=10, choices=StatusChoice,
                              default=JoinStatus.REQUESTED.value)
    acted_by = models.ForeignKey(User,
        on_delete = models.CASCADE,
        null=True,
        related_name='requests'
    )
    acted_at = models.DateTimeField(auto_now = True)
