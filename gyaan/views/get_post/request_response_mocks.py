


RESPONSE_200_JSON = """
{
    "post_id": 1,
    "posted_by": {
        "user_id": 1,
        "name": "string",
        "profile_pic": "string"
    },
    "title": "string",
    "description": "string",
    "posted_at": "string",
    "tags": [
        {
            "id": 1,
            "name": "string"
        }
    ],
    "comments_count": 1,
    "reactions_count": 1,
    "domain": {
        "domain_id": 1,
        "name": "string",
        "picture": "string"
    },
    "is_reacted": true,
    "approved_answer": {
        "comment_id": 1,
        "commented_at": "string",
        "content": "string",
        "commented_by": {
            "user_id": 1,
            "name": "string",
            "profile_pic": "string"
        },
        "reactions_count": 1,
        "is_reacted": true,
        "replies_count": 1,
        "replies": [
            {
                "comment_id": 1,
                "commented_at": "string",
                "content": "string",
                "commented_by": {
                    "user_id": 1,
                    "name": "string",
                    "profile_pic": "string"
                },
                "reactions_count": 1,
                "is_reacted": true
            }
        ],
        "approved_by": {
            "user_id": 1,
            "name": "string",
            "profile_pic": "string"
        }
    },
    "latest_comments": [
        {
            "comment_id": 1,
            "commented_at": "string",
            "content": "string",
            "commented_by": {
                "user_id": 1,
                "name": "string",
                "profile_pic": "string"
            },
            "reactions_count": 1,
            "is_reacted": true,
            "replies_count": 1,
            "replies": [
                {
                    "comment_id": 1,
                    "commented_at": "string",
                    "content": "string",
                    "commented_by": {
                        "user_id": 1,
                        "name": "string",
                        "profile_pic": "string"
                    },
                    "reactions_count": 1,
                    "is_reacted": true
                }
            ]
        }
    ]
}
"""

