# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01StateGetCumulativeReportAPITestCase::test_case status'] = 400

snapshots['TestCase01StateGetCumulativeReportAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_STATE_ID',
    'response': 'invalid state id'
}

snapshots['TestCase01StateGetCumulativeReportAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '91',
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
