import datetime
import factory
import random

from gyaan.models import *
from gyaan.constants.enums import PostStatus

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: "user%03d" % n)
    profile_pic = factory.LazyAttribute(
        lambda obj: "%s@example.com" % obj.name
    )
    username = factory.Sequence(lambda n: "user%03d" % n)


class DomainFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Domain

    name = factory.Sequence(lambda n: "Domain%03d" % n)
    picture = factory.LazyAttribute(
        lambda obj: "%s@example.com" % obj.name
    )
    description = "This a valid Domain"


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    is_approved = False
    posted_at = factory.LazyFunction(datetime.datetime.now)
    posted_by = factory.Iterator(User.objects.all())
    domain = factory.Iterator(Domain.objects.all())

class TagsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tags

    domain = factory.Iterator(Domain.objects.all())
    name = factory.Sequence(lambda n: "tag%03d" % n)

class PostVersionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostVersion

    title = factory.Sequence(lambda n: "Post Title %02d" % n)
    description = factory.LazyAttribute(
        lambda obj: "%s description" % obj.title
    )
    status = PostStatus.PENDING.value
    post = factory.Iterator(Post.objects.all())


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Sequence(lambda n: "Hii! Welcome %02d" % n)
    commented_by = factory.Iterator(User.objects.all())
    commented_at = factory.LazyFunction(datetime.datetime.now)
    post = factory.Iterator(Post.objects.all())


class ReplyCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Sequence(lambda n: "Hii! Welcome Reply Comment %02d" % n)
    commented_by = factory.Iterator(User.objects.all())
    commented_at = factory.LazyFunction(datetime.datetime.now)
    parent_comment = factory.Iterator(Comment.objects.all())


class PostReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    reacted_by = factory.Iterator(User.objects.all())
    post = factory.Iterator(Post.objects.all())
    reacted_at = factory.LazyFunction(datetime.datetime.now)


class CommentReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    reacted_by = factory.Iterator(User.objects.all())
    comment = factory.Iterator(Comment.objects.all())
    reacted_at = factory.LazyFunction(datetime.datetime.now)
