import datetime
import factory

from gyaan.models import (
    User, Domain, DomainMembers, DomainExpert,
    DomainJoinRequest
)
from gyaan.constants.enums import JoinStatus

class DomainFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Domain

    name = factory.Sequence(lambda n: "Domain%03d" % n)
    picture = factory.LazyAttribute(
        lambda obj: "%s@example.com" % obj.name
    )
    description = "This a valid Domain"


class DomainMembersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DomainMembers

    member = factory.Iterator(User.objects.all())
    domain = factory.Iterator(Domain.objects.all())


class DomainExpertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DomainExpert

    expert = factory.Iterator(User.objects.all())
    domain = factory.Iterator(Domain.objects.all())


class DomainJoinRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DomainJoinRequest

    user = factory.Iterator(User.objects.all())
    domain = factory.Iterator(Domain.objects.all())
    status = JoinStatus.REQUESTED.value
