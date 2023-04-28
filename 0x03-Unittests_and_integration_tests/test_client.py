#!/usr/bin/env python3
"""test_client module that tests client module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that tests GithubOrgClient class
    """
    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch('client.get_json')
    def test_org(self,org_name: str,
                 mock_get_json: unittest.mock.Mock) -> None:
        """test_org function that tests org method
        """
        pass
