from datetime import datetime

from django.db import models

from gyaan.models import User, Post, Tags
from gyaan.constants.enums import PostStatus

class PostVersion(models.Model):

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    StatusChoice = (
        (PostStatus.APPROVED.value, PostStatus.APPROVED.value),
        (PostStatus.REJECTED.value, PostStatus.REJECTED.value),
        (PostStatus.PENDING.value, PostStatus.PENDING.value)
    )
    status = models.CharField(max_length=10, choices=StatusChoice,
                              default=PostStatus.PENDING.value)
    approved_by = models.ForeignKey(User,
            on_delete=models.CASCADE,
            null=True, default=None
    )
    approved_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post,
        on_delete=models.CASCADE,
        null=True
    )
    tags = models.ManyToManyField(Tags,
        through="PostTags",
        related_name='post_version'
    )

    def __str__(self):
        return self.title
