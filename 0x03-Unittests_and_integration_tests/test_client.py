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
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 mock_get_json: unittest.mock.Mock) -> None:
        """test_org function that tests org method

        Args:
            org_name (str): org name
            expected (Dict): expected return value
            mock_get_json (unittest.mock.Mock): mock get_json
        """
        org = {"payload": True}
        mock_get_json.return_value = org
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, org)
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool) -> None:
        """test_has_license function that tests _has_license method

        Args:
            repo (Dict): repo dict
            license_key (str): license key
        """
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)
