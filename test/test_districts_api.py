# coding: utf-8

"""
    Clever Data API

    Serves the Clever Data API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import clever_client
from clever_client.api.districts_api import DistrictsApi  # noqa: E501
from clever_client.rest import ApiException


class TestDistrictsApi(unittest.TestCase):
    """DistrictsApi unit test stubs"""

    def setUp(self):
        self.api = clever_client.api.districts_api.DistrictsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_district(self):
        """Test case for get_district

        """
        pass

    def test_get_districts(self):
        """Test case for get_districts

        """
        pass


if __name__ == '__main__':
    unittest.main()
