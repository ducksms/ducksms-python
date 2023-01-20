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
from ducksms_api.models.preview_sms_send import PreviewSmsSend  # noqa: E501
from ducksms_api.rest import ApiException

class TestPreviewSmsSend(unittest.TestCase):
    """PreviewSmsSend unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PreviewSmsSend
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ducksms_api.models.preview_sms_send.PreviewSmsSend()  # noqa: E501
        if include_optional :
            return PreviewSmsSend(
                status = 200, 
                message = 'Preview data return successfully', 
                data = {"scheduled_at":false,"sender_id":{"name":"DUCKSMS"},"mobile_number":[{"number":60131234567},{"number":60131234562}],"credit":{"charge_per_sms":1,"charge_per_number":1,"charge":1,"balance":986762,"after":986761},"message":{"type":"ascii","total":1,"length":31,"message":"RM0 DUCKSMS: Hello World, Good morning!"},"callback_url":"https://webhook.site/2a88e4b4-56f7-46ee-b3a4-2f05d8b8456e","contains_special_characters":false}
            )
        else :
            return PreviewSmsSend(
        )

    def testPreviewSmsSend(self):
        """Test PreviewSmsSend"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()