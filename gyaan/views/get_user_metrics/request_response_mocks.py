


RESPONSE_200_JSON = """
{
    "user": {
        "user_id": 1,
        "name": "string",
        "profile_pic": "string"
    },
    "following_domains": [
        {
            "domain_id": 1,
            "name": "string",
            "picture": "string"
        }
    ],
    "suggested_domains": [
        {
            "domain_id": 1,
            "name": "string",
            "picture": "string",
            "follow_request": true
        }
    ],
    "user_post_metrics": {
        "total_posts": 1,
        "posts_in_each_domain": [
            {
                "domain_id": 1,
                "name": "string",
                "picture": "string",
                "posts_count": 1
            }
        ]
    },
    "pending_post_metrics": {
        "total_review_posts": 1,
        "pending_for_review": [
            {
                "domain_id": 1,
                "name": "string",
                "picture": "string",
                "review_posts_count": 1
            }
        ]
    }
}
"""

