from datetime import datetime

from django.db import models

from gyaan.models import User, Post

class Comment(models.Model):
    content = models.CharField(max_length = 1000)
    commented_at = models.DateTimeField(auto_now=True)
    commented_by = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(Post,
        on_delete=models.CASCADE,
        null=True,
        related_name='comments'
    )
    is_approved_by = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='comment_approved_by'
    )
    is_answer = models.BooleanField(default=False)
    parent_comment = models.ForeignKey('self',
        on_delete=models.CASCADE,
        null=True, default=None,
        related_name='comments'
    )
