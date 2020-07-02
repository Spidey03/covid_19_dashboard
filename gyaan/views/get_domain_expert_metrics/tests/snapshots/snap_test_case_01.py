# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDomainExpertMetricsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetDomainExpertMetricsAPITestCase::test_case body'] = {
    'post_review_requests': {
        'pending_for_review': [
            {
                'domain_id': 1,
                'name': 'string',
                'picture': 'string',
                'review_posts_count': 1
            }
        ],
        'total_posts': 1
    },
    'user_requests': [
        {
            'requests': [
                {
                    'domain': {
                        'domain_id': 1,
                        'name': 'string',
                        'picture': 'string'
                    },
                    'requested_user': {
                        'approved': True,
                        'name': 'string',
                        'profile_pic': 'string',
                        'rejected': True,
                        'user_id': 1
                    }
                }
            ],
            'total_requests': 1
        }
    ]
}

snapshots['TestCase01GetDomainExpertMetricsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '355',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
