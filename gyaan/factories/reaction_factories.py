import datetime
import factory

from gyaan.models import Comment, User, Post, Reaction

class PostReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    user = factory.Iterator(User.objects.all())
    post = factory.Iterator(Post.objects.all())
    # reacted_at = factory.LazyFunction(datetime.datetime.now)


class CommentReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    user = factory.Iterator(User.objects.all())
    comment = factory.Iterator(Comment.objects.all())
    # reacted_at = factory.LazyFunction(datetime.datetime.now)
