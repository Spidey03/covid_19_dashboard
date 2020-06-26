# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02LogInAPITestCase::test_case status'] = 200

snapshots['TestCase02LogInAPITestCase::test_case body'] = {
    'access_token': 'AEwOWuPMO04fchQqV8wga4ZtNpqzNI',
    'expires_in': '2020-09-14T17:46:40Z',
    'refresh_token': 'JlD2MYwFIidPL1mjJTIOjgISkot4Qc',
    'user_id': 1
}

snapshots['TestCase02LogInAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '153',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
