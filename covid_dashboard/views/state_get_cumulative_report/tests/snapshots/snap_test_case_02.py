# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02StateGetCumulativeReportAPITestCase::test_case status'] = 200

snapshots['TestCase02StateGetCumulativeReportAPITestCase::test_case body'] = {
    'active_cases': 45,
    'districts': [
        {
            'active_cases': 21,
            'district_name': 'district0',
            'total_cases': 34,
            'total_deaths': 2,
            'total_recovered_cases': 11
        },
        {
            'active_cases': 12,
            'district_name': 'district1',
            'total_cases': 24,
            'total_deaths': 7,
            'total_recovered_cases': 5
        },
        {
            'active_cases': 12,
            'district_name': 'district2',
            'total_cases': 21,
            'total_deaths': 6,
            'total_recovered_cases': 3
        },
        {
            'active_cases': 0,
            'district_name': 'district3',
            'total_cases': 0,
            'total_deaths': 0,
            'total_recovered_cases': 0
        }
    ],
    'state_name': 'state0',
    'total_cases': 79,
    'total_deaths': 15,
    'total_recovered_cases': 19
}

snapshots['TestCase02StateGetCumulativeReportAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '598',
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
