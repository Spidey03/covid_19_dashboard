# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01StateGetDayWiseReportAPITestCase::test_case status'] = 200

snapshots['TestCase01StateGetDayWiseReportAPITestCase::test_case body'] = {
    'daily_cumulative': [
        {
            'active_cases': 21,
            'date': '25-May-2020',
            'total_cases': 34,
            'total_deaths': 6,
            'total_recovered_cases': 7
        },
        {
            'active_cases': 32,
            'date': '26-May-2020',
            'total_cases': 52,
            'total_deaths': 8,
            'total_recovered_cases': 12
        },
        {
            'active_cases': 44,
            'date': '27-May-2020',
            'total_cases': 76,
            'total_deaths': 14,
            'total_recovered_cases': 18
        },
        {
            'active_cases': 44,
            'date': '28-May-2020',
            'total_cases': 76,
            'total_deaths': 14,
            'total_recovered_cases': 18
        },
        {
            'active_cases': 44,
            'date': '29-May-2020',
            'total_cases': 76,
            'total_deaths': 14,
            'total_recovered_cases': 18
        },
        {
            'active_cases': 45,
            'date': '30-May-2020',
            'total_cases': 79,
            'total_deaths': 15,
            'total_recovered_cases': 19
        }
    ]
}

snapshots['TestCase01StateGetDayWiseReportAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '697',
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
