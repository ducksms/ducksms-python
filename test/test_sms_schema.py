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
from ducksms_api.models.sms_schema import SmsSchema  # noqa: E501
from ducksms_api.rest import ApiException

class TestSmsSchema(unittest.TestCase):
    """SmsSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmsSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ducksms_api.models.sms_schema.SmsSchema()  # noqa: E501
        if include_optional :
            return SmsSchema(
                preview = 'yes', 
                mobile_numbers = ["60121234567","60131234567","60141234567","60151234567","60161234567","60171234567","60181234567"], 
                message = 'Hello world', 
                sender_id = 'DUCKSMS', 
                scheduled_at = '2022-12-06T15:19', 
                callback_url = 'https://webhook.site/2a88e4b4-56f7-46ee-b3a4-2f05d8b8456e'
            )
        else :
            return SmsSchema(
        )

    def testSmsSchema(self):
        """Test SmsSchema"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
