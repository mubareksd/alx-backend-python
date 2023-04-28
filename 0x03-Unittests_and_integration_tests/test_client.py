import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        mock_get_json.return_value = {'login': org_name}
        org = GithubOrgClient(org_name)
        assert org.org == mock_get_json.return_value