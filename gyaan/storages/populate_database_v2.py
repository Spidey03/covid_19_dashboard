from gyaan.models import *

def create_users():
    users = [
        {
            "username": "user1",
            "name": "Federico De Marco",
            "profile_pic": "user1@abc.com",
            "password": "user1"
        },
        {
            "username": "user2",
            "name": "RaccoonONRoids",
            "profile_pic": "user2@abc.com",
            "password": "user2"
        },
        {
            "username": "user3",
            "name": "Anoop K George",
            "profile_pic": "user3@abc.com",
            "password": "user3"
        },
        {
            "username": "user4",
            "name": "NublicPablo",
            "profile_pic": "user4@abc.com",
            "password": "user4"
        },
        {
            "username": "user5",
            "name": "John Lehmann",
            "profile_pic": "user4@abc.com",
            "password": "user5"
        },
        {
            "username": "user6",
            "name": "Mehmet Burak Ibis",
            "profile_pic": "user4@abc.com",
            "password": "user6"
        },
        {
            "username": "user7",
            "name": "Ahmed Wagdi",
            "profile_pic": "user4@abc.com",
            "password": "user7"
        }
    ]

    for user in users:
        user_obj = User.objects.create(
            username=user["username"],
            name=user["name"],
            profile_pic=user["profile_pic"],
        )
        user_obj.set_password(user["password"])
        user_obj.profile_pic = "https://2.gravatar.com/avatar/767fc9c115a1b989744c755db47feb60?s=132&d=wavatar"
        user_obj.save()

def populate_database():

    users = [
        {
            "username": "user1",
            "name": "Federico De Marco",
            "profile_pic": "user1@abc.com",
            "password": "user1"
        },
        {
            "username": "user2",
            "name": "RaccoonONRoids",
            "profile_pic": "user2@abc.com",
            "password": "user2"
        },
        {
            "username": "user3",
            "name": "Anoop K George",
            "profile_pic": "user3@abc.com",
            "password": "user3"
        },
        {
            "username": "user4",
            "name": "NublicPablo",
            "profile_pic": "user4@abc.com",
            "password": "user4"
        },
        {
            "username": "user5",
            "name": "John Lehmann",
            "profile_pic": "user4@abc.com",
            "password": "user5"
        },
        {
            "username": "user6",
            "name": "Mehmet Burak Ibis",
            "profile_pic": "user4@abc.com",
            "password": "user6"
        },
        {
            "username": "user7",
            "name": "Ahmed Wagdi",
            "profile_pic": "user4@abc.com",
            "password": "user7"
        }
    ]

    for user in users:
        user_obj = User.objects.create(
            username=user["username"],
            name=user["name"],
            profile_pic=user["profile_pic"],
        )
        user_obj.set_password(user["password"])
        user_obj.profile_pic = "https://2.gravatar.com/avatar/767fc9c115a1b989744c755db47feb60?s=132&d=wavatar"
        user_obj.save()


    create_domains = [{
        "name": "Django",
        "description": "Django is an open-source server-side web application framework, written in Python. It is designed to reduce the effort required to create complex data-driven websites and web applications, with a special focus on less code, no-redundancy and being more explicit than implicit.",
        "picture": "dkfajh"
    },
    {
        "name": "Python",
        "description": "Python is a multi-paradigm, dynamically typed, multipurpose programming language. It is designed to be quick to learn, understand, and use, and enforce a clean and uniform syntax. Please note that Python 2 is officially out of support as of 01-01-2020. Still, for version-specific Python questions, add the [python-2.7] or [python-3.x] tag. When using a Python variant or library (e.g. Jython, PyPy, Pandas, Numpy), please include it in the tags.",
        "picture": "dkfajh"
    },
    {
        "name": "Flask",
        "description": "Flask is a lightweight framework for developing web applications using Python.",
        "picture": "dkfajh"
    },
    {
        "name": "SQL",
        "description": "Structured Query Language (SQL) is a language for querying databases. Questions should include code examples, table structure, sample data, and a tag for the DBMS implementation (e.g. MySQL, PostgreSQL, Oracle, MS SQL Server, IBM DB2, etc.) being used. If your question relates solely to a specific DBMS (uses specific extensions/features), use that DBMS's tag instead. Answers to questions tagged with SQL should use ISO/IEC standard SQL.",
        "picture": "dkfajh"
    },
    {
        "name": "javascript",
        "description": "For questions regarding programming in ECMAScript (JavaScript/JS) and its various dialects/implementations (excluding ActionScript). This tag is rarely used alone but is most often associated with the tags [node.js], [json], and [html].",
        "picture": "dkfajh"
    },
    {
        "name": "android",
        "description": "Android is Google's mobile operating system, used for programming or developing digital devices (Smartphones, Tablets, Automobiles, TVs, Wear, Glass, IoT). For topics related to Android, use Android-specific tags such as android-intent, android-activity, android-adapter, etc. For questions other than development or programming, but related to the Android framework, use this link: https://android.stackexchange.com.",
        "picture": "dkfajh"
    },
    {
        "name": "html",
        "description": "HTML (HyperText Markup Language) is the main markup language for creating web pages and other information to be displayed in a web browser. Questions regarding HTML should include a minimal reproducible example and some idea of what you're trying to achieve. This tag is rarely used alone and is often paired with [CSS] and [javascript].",
        "picture": "dkfajh"
    }
    ]
    domain_objs = []
    for domain in create_domains:
        domain_objs.append(Domain(
            name=domain["name"],
            description=domain["description"],
            picture=domain["picture"]
        ))
    Domain.objects.bulk_create(domain_objs)


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
    post_objs = []
    for post in create_posts:
        post_objs.append(Post(
            is_approved=post["is_approved"],
            posted_by_id=post["posted_by_id"],
            domain_id=post["domain_id"]
        ))
    Post.objects.bulk_create(post_objs)


    create_version_posts = [{
        "title": "How to use serialize to serialize only some field?",
        "description": "Suppose I have a serializer class ProductSerializer(serializers.ModelSerializer): product_brand = serializers.StringRelatedField() product_type = serializers.StringRelatedField() class ...",
        "status": "APPROVED",
        "approved_by_id": 1,
        "post_id": 1
    },
    {
        "title": "How to transfer Django's messages to Angular app",
        "description": "I am building Django 2.2 +Node + Angular 8 app. Django is used to run a couple of simple scrapers when user clicks on Search btn. I want to make user notified that the scraping process started ..",
        "status": "PENDING",
        "approved_by_id": None,
        "post_id": 2
    },
    {
        "title": "Frontend application displaing progress from API",
        "description": "I've got a case where I have got 3 docker containers: - frontend in Angular - backend in Django - processing API in python. The use-case is that user sends a file to backend volume (using frontend ...",
        "status": "APPROVED",
        "approved_by_id": 3,
        "post_id": 3
    },
    {
        "title": "ExtendedRequestsLibrary from robot framework has depreciation to_json error",
        "description": "I just downloaded the ExtendedRequestsLibrary, and I cannot seem to even import it. The code crashes before any code execution when I import using Library ExtendedRequestsLibrary I am ...",
        "status": "APPROVED",
        "approved_by_id": 4,
        "post_id": 4
    },
    {
        "title": "I got error “ZeroDivisionError: division by zero” because modulo make number small",
        "description": "I have a problem with my code, in the code below the purpose is to change the value in the index of range 4 to n+1. by the flow just put answer[index] = round((answer[i-1]**2)/answer[index-2]) and I ...",
        "status": "PENDING",
        "approved_by_id": None,
        "post_id": 5
    },
    {
        "title": "Repeating numbers random Android studio java random array problem",
        "description": "i have a problen with random in arrays. It is like a quiz and i have arrays with questions,choises and answers. When i start my quiz , qustions are repeating Know about shuffle but do not know how to ...",
        "status": "PENDING",
        "approved_by_id": None,
        "post_id": 6
    },
    {
        "title": "AppRTC: iOS to Android Call is not working",
        "description": "We are developing an app using AppRTC. Audio and Video call from iOS-iOS and Android-Android are working fine but whenever we try to call from android to iOS or iOS to android, nothing happens after ...",
        "status": "APPROVED",
        "approved_by_id": 1,
        "post_id": 6
    },
    {
        "title": "How should I design the RDS database schema for creating a hierarchical relationship of each entry with itself?",
        "description": "I am creating a categories table. I can have many categories which are a parent to one category. For eg: Electronics -> Consumer Electronics -> Televisions -> Smart TVs etc. One way was to have ...",
        "status": "APPROVED",
        "approved_by_id": 2,
        "post_id": 7
    },
    {
        "title": "Flask SQLAlchemy Order by Field",
        "description": "I have successfully ran a select statement in mysql as follows: SELECT * FROM servers ORDER BY FIELD (onlinecheck, 0, NULL, last_reboot) DESC, last_reboot DESC; How do I run this same statement ...",
        "status": "PENDING",
        "approved_by_id": None,
        "post_id": 8
    },
    {
        "title": "Database changes are not showing in php/browser output on my VM server",
        "description": "I'm using a vagrant/VM with sequel pro and php to develop a site. I have a strange situation where I cannot update a table in the DB using php/sql update code (the code works on apache). ...",
        "status": "APPROVED",
        "approved_by_id": 4,
        "post_id": 9
    },
    {
        "title": "Is there any way to determine what codec AVPlayer is using?",
        "description": "I have looked through all the header docs for AVPlayer, AVPlayerItem, AVAsset, etc and haven't found anything that could be used to gather information about the current codec being used by AVPlayer. ...",
        "status": "APPROVED",
        "approved_by_id": 1,
        "post_id": 10
    },
    {
        "title": "“No internet connection” message appears while using sign in by Apple",
        "description": "I recently implemented Sign In with Apple feature in my iOS application, I tested the feature on many devices including an iPad and iPhone on Wi-Fi and cellular network on iOS 13.5.1 and it worked ...",
        "status": "PENDING",
        "approved_by_id": None,
        "post_id": 11
    }
    ]
    version = []
    for post in create_version_posts:
        version.append(PostVersion(
            title=post["title"],
            description=post["description"],
            status=post["status"],
            approved_by_id=post['approved_by_id'],
            post_id=post["post_id"]
        ))
    PostVersion.objects.bulk_create(version)


    create_comments = [{
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 1,
        "post_id": 1,
        "is_answer": True,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 2,
        "post_id": 1,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 3,
        "post_id": 1,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 4,
        "post_id": 1,
        "is_answer": False,
        "parent_comment_id": 1
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 2,
        "post_id": 2,
        "is_answer": True,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 3,
        "post_id": 2,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 4,
        "post_id": 2,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 3,
        "post_id": 3,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 4,
        "post_id": 3,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 5,
        "post_id": 3,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 4,
        "post_id": 4,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 5,
        "post_id": 4,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 6,
        "post_id": 4,
        "is_answer": False,
        "parent_comment_id": None
    },
    {
        "content": "That is pretty strange since I did the exact same thing yesterday and got the same version 1.8.4 which did resolve the problem. And is also what bower themselves recommend. Perhaps something else is a problem in your setup so you're not running the bower that you think you are ",
        "commented_by_id": 7,
        "post_id": 7,
        "is_answer": False,
        "parent_comment_id": None
    }
    ]
    comment_objs = []
    for comment in create_comments:
        comment_objs.append(Comment(
            content=comment["content"],
            commented_by_id=comment["commented_by_id"],
            post_id=comment["post_id"],
            is_answer=comment["is_answer"],
            parent_comment_id=comment["parent_comment_id"]
        ))
    Comment.objects.bulk_create(comment_objs)


    create_reactions = [{
        "comment_id": 1,
        "post_id": None,
        "user_id": 1
    },
    {
        "comment_id": None,
        "post_id": 1,
        "user_id": 1
    },
    {
        "comment_id": 2,
        "post_id": None,
        "user_id": 2
    },
    {
        "comment_id": None,
        "post_id": 2,
        "user_id": 2
    },
    {
        "comment_id": 3,
        "post_id": None,
        "user_id": 3
    },
    {
        "comment_id": None,
        "post_id": 3,
        "user_id": 3
    },
    {
        "comment_id": 4,
        "post_id": None,
        "user_id": 4
    },
    {
        "comment_id": None,
        "post_id": 4,
        "user_id": 4
    },
    {
        "comment_id": 5,
        "post_id": None,
        "user_id": 5
    },
    {
        "comment_id": None,
        "post_id": 5,
        "user_id": 5
    },
    {
        "comment_id": 6,
        "post_id": None,
        "user_id": 6
    },
    {
        "comment_id": None,
        "post_id": 6,
        "user_id": 6
    },
    {
        "comment_id": 1,
        "post_id": None,
        "user_id": 2
    },
    {
        "comment_id": None,
        "post_id": 1,
        "user_id": 2
    },
    {
        "comment_id": 1,
        "post_id": None,
        "user_id": 3
    },
    {
        "comment_id": None,
        "post_id": 1,
        "user_id": 3
    },
    {
        "comment_id": 1,
        "post_id": None,
        "user_id": 4
    },
    {
        "comment_id": None,
        "post_id": 1,
        "user_id": 4
    }
    ]

    reaction_objs = []
    for reaction in create_reactions:
        reaction_objs.append(Reaction(
            comment_id=reaction["comment_id"],
            post_id=reaction["post_id"],
            user_id=reaction["user_id"]
            ))
    Reaction.objects.bulk_create(reaction_objs)

    create_tags = [{
        "domain_id": 1,
        "name": "ORM"
    },
    {
        "domain_id": 2,
        "name": "MODEL"
    },
    {
        "domain_id": 3,
        "name": "css"
    },
    {
        "domain_id": 4,
        "name": "python"
    },
    {
        "domain_id": 3,
        "name": "sql"
    },
    {
        "domain_id": 2,
        "name": "android"
    },
    {
        "domain_id": 1,
        "name": "ruby"
    }]

    tag_objs = []
    for tag in create_tags:
        tag_objs.append(Tags(
            domain_id=tag["domain_id"],
            name=tag["name"]
        ))
    Tags.objects.bulk_create(tag_objs)

    create_post_tags = [
        {
            "post_id": 1,
            "tag_id": 1
        },
        {
            "post_id": 1,
            "tag_id": 2
        },
        {
            "post_id": 2,
            "tag_id": 3
        },
        {
            "post_id": 2,
            "tag_id": 4
        },
        {
            "post_id": 3,
            "tag_id": 5
        },
        {
            "post_id": 4,
            "tag_id": 6
        },
        {
            "post_id": 3,
            "tag_id": 4
        },
        {
            "post_id": 4,
            "tag_id": 5
        },
        {
            "post_id": 5,
            "tag_id": 6
        }
    ]
    post_tags = []
    for tag in create_post_tags:
        post_tags.append(PostTags(
            post_id=tag["post_id"],
            tag_id=tag["tag_id"]
        ))
    PostTags.objects.bulk_create(post_tags)

    create_domain_requests = [{
        "user_id": 4,
        "domain_id": 1,
        "status": "REQUESTED"
    },
    {
        "user_id": 5,
        "domain_id": 1,
        "status": "REQUESTED"
    },
    {
        "user_id": 6,
        "domain_id": 1,
        "status": "REQUESTED"
    },
    {
        "user_id": 4,
        "domain_id": 2,
        "status": "REQUESTED"
    },
    {
        "user_id": 5,
        "domain_id": 2,
        "status": "REQUESTED"
    },
    {
        "user_id": 6,
        "domain_id": 2,
        "status": "REQUESTED"
    }
    ]
    join_requests = []
    for request in create_domain_requests:
        join_requests.append(DomainJoinRequest(
            user_id=request["user_id"],
            domain_id=request["domain_id"],
            status=request["status"]
        ))
    DomainJoinRequest.objects.bulk_create(join_requests)

    create_domain_experts = [{
        "expert_id": 1,
        "domain_id": 1
    },
    {
        "expert_id": 2,
        "domain_id": 2
    },
    {
        "expert_id": 3,
        "domain_id": 3
    },
    {
        "expert_id": 4,
        "domain_id": 4
    },
    {
        "expert_id": 5,
        "domain_id": 5
    },
    {
        "expert_id": 6,
        "domain_id": 6
    }
    ]
    expert_objs = []
    for expert in create_domain_experts:
        expert_objs.append(DomainExpert(
            expert_id=expert["expert_id"],
            domain_id=expert['domain_id']
        ))
    DomainExpert.objects.bulk_create(expert_objs)

    create_domain_members = [{
        "member_id": 1,
        "domain_id": 1
    },
    {
        "member_id": 2,
        "domain_id": 2
    },
    {
        "member_id": 3,
        "domain_id": 3
    },
    {
        "member_id": 4,
        "domain_id": 4
    },
    {
        "member_id": 5,
        "domain_id": 5
    },
    {
        "member_id": 6,
        "domain_id": 3
    },
    {
        "member_id": 2,
        "domain_id": 1
    },
    {
        "member_id": 1,
        "domain_id": 2
    },
    {
        "member_id": 6,
        "domain_id": 2
    },
    {
        "member_id": 3,
        "domain_id": 1
    },
    {
        "member_id": 3,
        "domain_id": 2
    },
    ]
    memeber_objs = []
    for expert in create_domain_members:
        memeber_objs.append(DomainMembers(
            member_id=expert["member_id"],
            domain_id=expert['domain_id']
        ))
    DomainMembers.objects.bulk_create(memeber_objs)
