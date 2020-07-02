


RESPONSE_200_JSON = """
{
    "post_review_requests": {
        "total_posts": 1,
        "pending_for_review": [
            {
                "domain_id": 1,
                "name": "string",
                "picture": "string",
                "review_posts_count": 1
            }
        ]
    },
    "user_requests": [
        {
            "total_requests": 1,
            "requests": [
                {
                    "domain": {
                        "domain_id": 1,
                        "name": "string",
                        "picture": "string"
                    },
                    "requested_user": {
                        "user_id": 1,
                        "name": "string",
                        "profile_pic": "string",
                        "approved": true,
                        "rejected": true
                    }
                }
            ]
        }
    ]
}
"""

