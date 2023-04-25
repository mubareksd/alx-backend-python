#!/usr/bin/env python3
"""test_utils module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map function that,
        tests access_nested_map function

        Args:
            nested_map (dict): nested map to test
            path (tuple): path of keys to access in nested map
            expected (any): expected return value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test_access_nested_map_exception function that,
        tests access_nested_map function with exception

        Args:
            nested_map (dict): nested map to test
            path (tuple): path of keys to access in nested map
            expected (any): expected return value

        Raises:
            expected: expected exception
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """test_get_json function that tests get_json function

        Args:
            url (str): url to test
            tet_payload (dict): expected return value
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url), test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class that inherits from unittest.TestCase
    """
    def test_memoize(self):
        """Test that when calling a_property twice, the correct result
        """
        class TestClass:
            """TestClass class
            """
            def a_method(self):
                """a_method method that returns an int

                Returns:
                    int: 42
                """
                return 42

            @memoize
            def a_property(self):
                """a_property method that returns a memoized value

                Returns:
                    method: a_method return value
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
