#!/usr/bin/env python3
"""test_client module that tests client module
"""
import unittest
from unittest.mock import patch
from typing import Dict
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that tests GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"message": "Not Found"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected: Dict,
                 mock_get_json: unittest.mock.Mock) -> None:
        """test_org function that tests org method

        Args:
            org_name (str): org name
            expected (Dict): expected return value
            mock_get_json (unittest.mock.Mock): mock get_json
        """
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once()
