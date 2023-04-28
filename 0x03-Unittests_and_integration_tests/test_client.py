#!/usr/bin/env python3
"""test_client module that tests client module
"""
import unittest
from unittest.mock import PropertyMock, patch
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

    def test_public_repos_url(self):
        """test_public_repos_url function that tests _public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            org = {"repos_url": "world"}
            mock_org.return_value = org
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, org["repos_url"])