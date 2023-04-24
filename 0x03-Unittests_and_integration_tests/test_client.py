#!/usr/bin/env python3
"""test_client module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org function
        """
        mock_get_json.return_value = {'payload': True}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, mock_get_json.return_value)
