# coding: utf-8

"""
    Ducksms

    The version of the OpenAPI document: 1.0.0
    Contact: support@ducksms.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ducksms_api
from ducksms_api.api.sms_api import SmsApi  # noqa: E501
from ducksms_api.rest import ApiException


class TestSmsApi(unittest.TestCase):
    """SmsApi unit test stubs"""

    def setUp(self):
        self.api = ducksms_api.api.sms_api.SmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sms_send(self):
        """Test case for sms_send

        Send Sms  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
