#!/usr/bin/env python3
"""test_client module that tests client module
"""
import unittest
from unittest.mock import patch, MagicMock
from typing import Dict
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that tests GithubOrgClient class
    """
    @parameterized.expand([
        ('google', {'login': 'google'})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, ret: Dict, mock_get_json: MagicMock):
        """test_org method that tests org method

        Args:
            org_name (str): org name
            ret (Dict): return value
            mock_get_json (MagicMock): mock get_json
        """
        mock_get_json.return_value = ret
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, ret)
        mock_get_json.assert_called_once()
