from django.db import models

from gyaan.models import User, Post, Comment

class Reaction(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                default=None, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None,
                             null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'post'], ['user', 'comment']]