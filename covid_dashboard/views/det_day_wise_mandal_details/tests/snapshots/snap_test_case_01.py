# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01DetDayWiseMandalDetailsAPITestCase::test_case status'] = 404

snapshots['TestCase01DetDayWiseMandalDetailsAPITestCase::test_case body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'

snapshots['TestCase01DetDayWiseMandalDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '77',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html'
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
