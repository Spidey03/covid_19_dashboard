from django.db import models

from gyaan.models import PostVersion, Tags

class PostTags(models.Model):
    post = models.ForeignKey(PostVersion, on_delete=models.CASCADE,
                               related_name='post_tags')
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE,
                               related_name='post_tags')

    class Meta:
        unique_together = [['post', 'tag']]
