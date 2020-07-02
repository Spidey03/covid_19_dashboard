from gyaan.models import *

def create_users():
    users = [
        {
            "username": "user1",
            "name": "user1",
            "profile_pic": "user1@abc.com",
            "password": "user1"
        },
        {
            "username": "user2",
            "name": "user2",
            "profile_pic": "user2@abc.com",
            "password": "user2"
        },
        {
            "username": "user3",
            "name": "user3",
            "profile_pic": "user3@abc.com",
            "password": "user3"
        },
        {
            "username": "user4",
            "name": "user4",
            "profile_pic": "user4@abc.com",
            "password": "user4"
        }
    ]

    for user in users:
        user_obj = User.objects.create(
            username=user["username"],
            name=user["name"],
            profile_pic=user["profile_pic"],
        )
        user_obj.set_password(user["password"])
        user_obj.save()



def populate_database():

    create_domains = [{
        "name": "Django",
        "description": "django",
        "picture": "dkfajh"
    },
    {
        "name": "ORM",
        "description": "ORM",
        "picture": "dkfajh"
    },
    {
        "name": "Flask",
        "description": "Flask",
        "picture": "dkfajh"
    },
    {
        "name": "SQL",
        "description": "SQL",
        "picture": "dkfajh"
    }]
    for domain in create_domains:
        Domain.objects.create(
            name=domain["name"],
            description=domain["description"],
            picture=domain["picture"]
        )

    create_posts = [{
        "is_approved": True,
        "posted_by_id": 1,
        "domain_id": 1
    },
    {
        "is_approved": False,
        "posted_by_id": 1,
        "domain_id": 2
    },
    {
        "is_approved": False,
        "posted_by_id": 2,
        "domain_id": 1
    },
    {
        "is_approved": True,
        "posted_by_id": 3,
        "domain_id": 3
    }
    ]
    for post in create_posts:
        Post.objects.create(
            is_approved=post["is_approved"],
            posted_by_id=post["posted_by_id"],
            domain_id=post["domain_id"]
        )

    create_version_posts = [{
        "title": "Django Post",
        "description": "first",
        "status": "APPROVED",
        "approved_by_id": 1,
        "post_id": 1
    },
    {
        "title": "Django post",
        "description": "updated",
        "status": "PENDING",
        "approved_by_id": 1,
        "post_id": 1
    },
    {
        "title": "ORM post",
        "description": "first",
        "status": "PENDING",
        "approved_by_id": None,
        "post_id": 2
    },
    {
        "title": "Flask post",
        "description": "first",
        "status": "PENDING",
        "approved_by_id": None,
        "post_id": 3
    },
    {
        "title": "SQL post",
        "description": "first",
        "status": "APPROVED",
        "approved_by_id": 1,
        "post_id": 4
    }]

    for post in create_version_posts:
        PostVersion.objects.create(
            title=post["title"],
            description=post["description"],
            status=post["status"],
            approved_by_id=post['approved_by_id'],
            post_id=post["post_id"]
        )

    create_comments = [{
        "content": "comment to post1",
        "commented_by_id": 1,
        "post_id": 1,
        "is_answer": True,
        "parent_comment_id": None
    },
    {
        "content": "reply to comment1",
        "commented_by_id": 2,
        "post_id": 1,
        "is_answer": False,
        "parent_comment_id": 1
    },
    {
        "content": "comment to post2",
        "commented_by_id": 2,
        "post_id": 2,
        "is_answer": False,
        "parent_comment_id": None
    }]
    for comment in create_comments:
        Comment.objects.create(
            content=comment["content"],
            commented_by_id=comment["commented_by_id"],
            post_id=comment["post_id"],
            is_answer=comment["is_answer"],
            parent_comment_id=comment["parent_comment_id"]
        )



def create_reactions():
    create_reactions = [{
        "comment_id": 1,
        "post_id": None,
        "user_id": 1
    },
    {
        "comment_id": None,
        "post_id": 1,
        "user_id": 1
    }]
    for reaction in create_reactions:
        Reaction.objects.create(
            comment_id=reaction["comment_id"],
            post_id=reaction["post_id"],
            user_id=reaction["user_id"]
            )

def populate_tags():
    create_tags = [{
        "domain_id": 1,
        "name": "ORM"
    },
    {
        "domain_id": 1,
        "name": "MODEL"
    },
    {
        "domain_id": 1,
        "name": "SHELL"
    }]

    for tag in create_tags:
        Tags.objects.create(
            domain_id=tag["domain_id"],
            name=tag["name"]
        )


def create_post_tags():
    create_post_tags = [
        {
            "post_id": 1,
            "tag_id": 1
        },
        {
            "post_id": 1,
            "tag_id": 2
        }
    ]
    for tag in create_post_tags:
        PostTags.objects.create(
            post_id=tag["post_id"],
            tag_id=tag["tag_id"]
        )


def populate_domain_request():
    create_domain_requests = [{
        "user_id": 4,
        "domain_id": 1,
        "status": "REQUESTED"
    }]
    for request in create_domain_requests:
        DomainJoinRequest.objects.create(
            user_id=request["user_id"],
            domain_id=request["domain_id"],
            status=request["status"]
        )

def populate_domain_experts():
    create_domain_experts = [{
        "expert_id": 1,
        "domain_id": 1
    },
    {
        "expert_id": 2,
        "domain_id": 1
    },
    {
        "expert_id": 1,
        "domain_id": 2
    },
    ]
    for expert in create_domain_experts:
        DomainExpert.objects.create(
            expert_id=expert["expert_id"],
            domain_id=expert['domain_id']
        )

def populate_domain_members():
    create_domain_members = [{
        "member_id": 1,
        "domain_id": 1
    },
    {
        "member_id": 2,
        "domain_id": 1
    },
    {
        "member_id": 1,
        "domain_id": 2
    },
    ]
    for expert in create_domain_members:
        DomainMembers.objects.create(
            member_id=expert["member_id"],
            domain_id=expert['domain_id']
        )


# queryset = DomainExpert.objects.filter(domain_id=1).annotate(experts_count=Count('id'))
# Domain.objects.prefetch_related(
#     Prefetch('domains', queryset=queryset, to_attr='domain_experts')
# )






    create_posts = [{
        "is_approved": True,
        "posted_by_id": 1,
        "domain_id": 1
    },
    {
        "is_approved": False,
        "posted_by_id": 1,
        "domain_id": 2
    },
    {
        "is_approved": True,
        "posted_by_id": 1,
        "domain_id": 3
    },
    {
        "is_approved": True,
        "posted_by_id": 1,
        "domain_id": 4
    },
    {
        "is_approved": False,
        "posted_by_id": 1,
        "domain_id": 5
    },
    {
        "is_approved": False,
        "posted_by_id": 1,
        "domain_id": 1
    },
    {
        "is_approved": True,
        "posted_by_id": 2,
        "domain_id": 1
    },{
        "is_approved": True,
        "posted_by_id": 2,
        "domain_id": 2
    },
    {
        "is_approved": False,
        "posted_by_id": 2,
        "domain_id": 3
    },
    {
        "is_approved": True,
        "posted_by_id": 2,
        "domain_id": 4
    },
    {
        "is_approved": True,
        "posted_by_id": 3,
        "domain_id": 1
    },
    {
        "is_approved": False,
        "posted_by_id": 3,
        "domain_id": 2
    }
    ]



