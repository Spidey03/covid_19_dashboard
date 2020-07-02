# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDomainPostsAPITestCase::test_case status'] = 500

snapshots['TestCase01GetDomainPostsAPITestCase::test_case body'] = {
    'replies': [
        {
            'non_field_errors': [
                'Invalid data. Expected a dictionary, but got CommentType.'
            ]
        }
    ]
}

snapshots['TestCase01GetDomainPostsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '96',
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
