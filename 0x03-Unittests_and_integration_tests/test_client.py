#!/usr/bin/env python3
"""test_client module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock

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

    def test_public_repos_url(self):
        """test_public_repos_url function
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'google'}
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url,
                             mock_org.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test_public_repos function
        """
        mock_get_json.return_value = [{'name': 'google'}, {'name': 'abc'}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'google'
            client = GithubOrgClient('google')
            self.assertEqual(client.public_repos(), ['google', 'abc'])
            mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
