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
from ducksms_api.api.credit_api import CreditApi  # noqa: E501
from ducksms_api.rest import ApiException


class TestCreditApi(unittest.TestCase):
    """CreditApi unit test stubs"""

    def setUp(self):
        self.api = ducksms_api.api.credit_api.CreditApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_credit_balance(self):
        """Test case for credit_balance

        Credit Balance  # noqa: E501
        """
        pass

    def test_credit_history(self):
        """Test case for credit_history

        Credit History  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()