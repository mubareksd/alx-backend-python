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
    def test_org(self, org_name):
        """test_org function
        """
        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = {'payload': True}
            client = GithubOrgClient(org_name)
            self.assertEqual(client.org, mock_get_json.return_value)
