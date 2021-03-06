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
from clever_client.api.resources_api import ResourcesApi  # noqa: E501
from clever_client.rest import ApiException


class TestResourcesApi(unittest.TestCase):
    """ResourcesApi unit test stubs"""

    def setUp(self):
        self.api = clever_client.api.resources_api.ResourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_courses_for_resource(self):
        """Test case for get_courses_for_resource

        """
        pass

    def test_get_resource(self):
        """Test case for get_resource

        """
        pass

    def test_get_resources(self):
        """Test case for get_resources

        """
        pass

    def test_get_sections_for_resource(self):
        """Test case for get_sections_for_resource

        """
        pass

    def test_get_users_for_resource(self):
        """Test case for get_users_for_resource

        """
        pass


if __name__ == '__main__':
    unittest.main()
