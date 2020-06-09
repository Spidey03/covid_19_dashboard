# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetStateWiseCumulativeReportOfCasesAPITestCase::test_case status'] = 200

snapshots['TestCase01GetStateWiseCumulativeReportOfCasesAPITestCase::test_case body'] = {
    'active_cases': 0,
    'districts': [
    ],
    'state_name': 'Andhrapradesh',
    'total_cases': 0,
    'total_deaths': 0,
    'total_recovered_cases': 0
}

snapshots['TestCase01GetStateWiseCumulativeReportOfCasesAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '132',
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
