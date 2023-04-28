#!/usr/bin/env python3
"""test_client module
"""
import unittest
from unittest.mock import MagicMock, patch, PropertyMock
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: MagicMock):
        """test_org function that tests org function

        Args:
            org_name (String): organization name to test
            mock_get_json (MagicMock): mock get_json function from client
        """
        mock_get_json.return_value = {'payload': True}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, mock_get_json.return_value)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """test_public_repos_url function that tests public_repos_url function
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'google'}
            client = GithubOrgClient('google')
            self.assertEqual(client.public_repos,
                             mock_org.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test_public_repos function that tests public_repos function

        Args:
            mock_get_json ([type]): [description]
        """
        mock_get_json.return_value = [
            {'name': 'truth'},
            {'name': 'ruby-openid-apps-discovery'}
            ]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'google/repos'
            client = GithubOrgClient('google')
            self.assertEqual(client.public_repos(),
                             ["truth", "ruby-openid-apps-discovery"])
            mock_get_json.assert_called_once()
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test_has_license function that tests has_license function

        Args:
            repo ([type]): [description]
            license_key ([type]): [description]
            expected ([type]): [description]
        """
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected)


@parameterized_class([
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class that,
    inherits from unittest.TestCase
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.get_patcher = patch('requests.get', new=MagicMock())
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
