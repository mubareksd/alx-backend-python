#!/usr/bin/env python3
import unittest


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    def test_org(self):
        pass