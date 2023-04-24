#!/usr/bin/env python3
"""test_client module
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test_has_license function

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
    """TestIntegrationGithubOrgClient class
    """

    @classmethod
    def setUp(self) -> None:
        self.get_patcher = patch('requests.get', side_effect=[
            self.org_payload, self.repos_payload,
            self.org_payload, self.repos_payload
        ])
        self.mock_get = self.get_patcher.start()

    @classmethod
    def tearDown(self) -> None:
        self.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
