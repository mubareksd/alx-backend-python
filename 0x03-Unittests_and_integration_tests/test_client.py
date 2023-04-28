#!/usr/bin/env python3
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    def test_org(self):
        pass