from gyaan.models.user import User
from gyaan.models.post import Post
from gyaan.models.domain import Domain
from gyaan.models.comment import Comment
from gyaan.models.tags import Tags
from gyaan.models.postversion import PostVersion
from gyaan.models.reaction import Reaction
from gyaan.models.domain_expert import DomainExpert
from gyaan.models.domain_join_request import DomainJoinRequest
from gyaan.models.domain_members import DomainMembers
from gyaan.models.post_tags import PostTags

__all__ = [
    "User",
    "Post",
    "Domain",
    "Comment",
    "PostVersion",
    "Reaction",
    "DomainExpert",
    "DomainJoinRequest",
    "DomainMembers",
    "Tags",
    "PostTags"
    ]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
