import datetime
import factory

from gyaan.models import Tags, PostTags, PostVersion, Domain

class TagsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tags

    domain = factory.Iterator(Domain.objects.all())
    name = factory.Sequence(lambda n: "tag%03d" % n)


class PostTagsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostTags

    post = factory.Iterator(PostVersion.objects.all())
    tag = factory.Iterator(Tags.objects.all())