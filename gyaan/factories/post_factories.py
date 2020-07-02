import datetime
import factory

from gyaan.models import Post, PostVersion, User, Domain
from gyaan.constants.enums import PostStatus


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    is_approved = False
    posted_at = factory.LazyFunction(datetime.datetime.now)
    posted_by = factory.Iterator(User.objects.all())
    domain = factory.Iterator(Domain.objects.all())

class PostVersionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostVersion

    title = factory.Sequence(lambda n: "Post Title %02d" % n)
    description = factory.LazyAttribute(
        lambda obj: "%s description" % obj.title
    )
    status = PostStatus.PENDING.value
    post = factory.Iterator(Post.objects.all())
