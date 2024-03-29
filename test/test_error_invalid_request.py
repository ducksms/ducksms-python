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
from ducksms_api.models.error_invalid_request import ErrorInvalidRequest  # noqa: E501
from ducksms_api.rest import ApiException

class TestErrorInvalidRequest(unittest.TestCase):
    """ErrorInvalidRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ErrorInvalidRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ducksms_api.models.error_invalid_request.ErrorInvalidRequest()  # noqa: E501
        if include_optional :
            return ErrorInvalidRequest(
                status = 400, 
                message = 'Invalid request'
            )
        else :
            return ErrorInvalidRequest(
        )

    def testErrorInvalidRequest(self):
        """Test ErrorInvalidRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
