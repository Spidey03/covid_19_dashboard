import datetime
import factory

from gyaan.models import Comment, User, Post

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
