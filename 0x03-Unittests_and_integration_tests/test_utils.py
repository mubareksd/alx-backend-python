#!/usr/bin/env python3
"""test_utils module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch

from utils import access_nested_map, get_json, memoize


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


class TestMemoize(unittest.TestCase):
    """TestMemoize class
    """
    def test_memoize(self):
        class TestClass:
            """TestClass class
            """

            def a_method(self):
                """a_method function

                Returns:
                    int: 42
                """
                return 42

            @memoize
            def a_property(self):
                """a_property function

                Returns:
                    method: a_method
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
