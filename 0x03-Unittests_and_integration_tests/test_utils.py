#!/usr/bin/env python3
"""test_utils module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map function

        Args:
            nested_map (dict): nested map
            path (tuple): path to access value
            expected (any): expected return value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """test_get_json function

        Args:
            url (string): url to get json
            test_payload (dict): test payload
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url), test_payload)


if __name__ == '__main__':
    unittest.main()
