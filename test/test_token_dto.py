# coding: utf-8

"""
    Sematext Cloud API

    API Explorer provides access and documentation for Sematext REST API. The REST API requires the API Key to be sent as part of `Authorization` header. E.g.: `Authorization : apiKey e5f18450-205a-48eb-8589-7d49edaea813`.  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import stcloud
from stcloud.models.token_dto import TokenDto  # noqa: E501
from stcloud.rest import ApiException


class TestTokenDto(unittest.TestCase):
    """TokenDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTokenDto(self):
        """Test TokenDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = stcloud.models.token_dto.TokenDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
