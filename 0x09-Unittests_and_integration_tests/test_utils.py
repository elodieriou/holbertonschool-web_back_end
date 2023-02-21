#!/usr/bin/env python3
""" Module test utils """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
from typing import Mapping, Sequence, Dict, Any


class TestAccessNestedMap(unittest.TestCase):
    """ Tests access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected_result: Any) -> None:
        """ Test expected result"""
        result = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence) -> None:
        """ Test exception """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)


class TestGetJson(unittest.TestCase):
    """ Test get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, expected_result: Any,
                      mock_get) -> None:
        """ Test expected result """
        mock_json = Mock(return_value=expected_result)
        mock_get.return_value = Mock(json=mock_json)

        result = get_json(url=test_url)
        self.assertEqual(result, expected_result)
        self.assertIsInstance(mock_get.return_value, Mock)


class TestMemoize(unittest.TestCase):
    """ Test memoized """

    def test_memoize(self):
        """ Test expected result """

        class TestClass:
            """ Test class """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        mock_obj = TestClass()
        with patch.object(mock_obj, 'a_method', return_value=42) \
                as mock_a_method:
            result = mock_obj.a_property
            self.assertEqual(result, mock_a_method.return_value)
            self.assertEqual(result, mock_a_method.return_value)
            mock_a_method.assert_called_once()
