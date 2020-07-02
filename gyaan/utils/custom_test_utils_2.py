from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time

from gyaan.models import *
from gyaan.factories import *


class CustomTestUtils(CustomAPITestCase):

    def create_users(self):
        users = UserFactory.create_batch(5)
        return users

    def create_domains(self):
        DomainFactory.create_batch(3)

    def create_tags(self):
        TagsFactory.create_batch(3)

    def create_posts(self):
        PostFactory.create_batch(3)

    def create_post_versions(self):
        PostVersionFactory.create_batch(3)

    def create_post_tags(self):
        PostTagsFactory.create_batch(size=3)

    def create_comments(self):
        CommentFactory.create_batch(9)

    def create_post_reactions(self):
        post_reactions = PostReactionFactory.create_batch(3)
        return post_reactions

    def create_comment_reactions(self):
        CommentReactionFactory.create_batch(3)

    def get_post(self):
        self.create_users()
        self.create_domains()
        self.create_tags()
        self.create_posts()
        self.create_post_versions()
        self.create_post_tags()
        self.create_comments()
        # self.create_post_reactions()
        # self.create_comment_reactions()

    def get_home_feed(self):
        self.create_users()
        self.create_domains()
        self.create_tags()
        self.create_posts()
        self.create_post_versions()
        self.create_post_tags()
        self.create_comments()
        self.create_post_reactions()
        self.create_comment_reactions()


    def get_user_metrics(self):
        users = UserFactory.create_batch(10)



















"""
    POSTS = [
        {
            "user_id": 1,
            "post_content": "NEW POST",
        },
        {
            "user_id": 1,
            "post_content": "NEW POST",
        },
        {
            "user_id": 1,
            "post_content": "NEW POST",
        }
    ]

    USERS = [
        {
            'username': 'user1',
            "name": "lakshmi",
            "profile_pic": "abcd"
        }
    ]

    REACTIONS = [
        {
            "post_id": 1,
            "user_id": 1,
            "reaction_type": "LIKE",
            "comment_id": None
        }
    ]
    COMMENTS = [
        {
            "user_id": 1,
            "post_id": 1,
            "comment_content": "nice post",
            "parent_comment_id": None
        },
        {
            "user_id": 1,
            "post_id": 1,
            "comment_content": "great",
            "parent_comment_id": None
        },
        {
            "user_id": 1,
            "post_id": 1,
            "comment_content": "nice",
            "parent_comment_id": None
        }
    ]

    COMMENTS_REACTIONS = [
        {
            "comment_id": 1,
            "post_id": None,
            "user_id": 1,
            "reaction_type": "SAD"
        }
    ]

    COMMENT_REPLIES = [
        {
            "user_id": 1,
            "post_id": None,
            "comment_content": "nice post",
            "parent_comment_id": 2
        }
    ]
    REPLY_REACTIONS = [
        {
            "comment_id": 2,
            "post_id": None,
            "user_id": 1,
            "reaction_type": "WOW"
        }
    ]

    def create_posts(self):
        for post in self.POSTS:
            with freeze_time("09-11-2019"):
                Post.objects.create(
                    user_id=post['user_id'],
                    post_content=post['post_content']
                )

    def create_user(self):
        for user in self.USERS:
            User.objects.create(
                username=user['username'],
                name=user['name'],
                profile_pic=user['profile_pic']
            )

    def create_post_reactions(self):
        for reaction in self.REACTIONS:
            Reactions.objects.create(post_id=reaction['post_id'],
                                     user_id=reaction['user_id'],
                                     reaction_type=reaction['reaction_type'])

    def create_comments(self):
        for comment in self.COMMENTS:
            with freeze_time("18-12-2019"):
                Comment.objects.create(user_id=comment['user_id'],
                                       post_id=comment['post_id'],
                                       comment_text=comment['comment_content']
                                       )

    def create_comment_reactions(self):
        for reaction in self.COMMENTS_REACTIONS:
            Reactions.objects.create(comment_id=reaction['comment_id'],
                                     user_id=reaction['user_id'],
                                     reaction_type=reaction[
                                         'reaction_type'])

    def create_replies_for_comment(self):
        for reply in self.COMMENT_REPLIES:
            with freeze_time("18-12-2019"):
                Comment.objects.create(user_id=reply['user_id'],
                                       comment_text=reply['comment_content'],
                                       parent_comment_id=reply[
                                           'parent_comment_id'])

    def create_reply_reactions(self):
        for reaction in self.REPLY_REACTIONS:
            Reactions.objects.create(comment_id=reaction['comment_id'],
                                     user_id=reaction['user_id'],
                                     reaction_type=reaction['reaction_type'])
"""
