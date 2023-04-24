#!/usr/bin/env python3
"""test_client module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch

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

        Args:
            org_name (String): organization name
            mock_get_json ([type]): [description]
        """
        mock_get_json.return_value = {'login': org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, mock_get_json.return_value)
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()