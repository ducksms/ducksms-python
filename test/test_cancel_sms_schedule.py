# coding: utf-8

"""
    Ducksms

    The version of the OpenAPI document: 1.0.0
    Contact: support@ducksms.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ducksms_api
from ducksms_api.models.cancel_sms_schedule import CancelSmsSchedule  # noqa: E501
from ducksms_api.rest import ApiException

class TestCancelSmsSchedule(unittest.TestCase):
    """CancelSmsSchedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CancelSmsSchedule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ducksms_api.models.cancel_sms_schedule.CancelSmsSchedule()  # noqa: E501
        if include_optional :
            return CancelSmsSchedule(
                status = 200, 
                message = 'Schedule successfully cancelled', 
                data = []
            )
        else :
            return CancelSmsSchedule(
        )

    def testCancelSmsSchedule(self):
        """Test CancelSmsSchedule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
