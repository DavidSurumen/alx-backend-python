#!/usr/bin/env python3
"""
Unit tests module for the access_nested_map function
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
import json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test whether the access_nested_map function correctly accesses values
        from a nested dictionary using a given path.

        Parameters:
            nested_map (Mapping): the nested dictionary to be accessed
            path (Sequence): the list of keys forming the path to the desired
                             value

        Returns:
            None: This test does not return anything.

        Assertions:
            - The result of access_nested_map(nested_map, path) must match
              the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError, "'a'"),
        ({"a": 1}, ["a", "b"], KeyError, "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_excep, expected_msg):
        """
        Test whether the access_nested_map function raises the right
        exceptions on bad input and the exception message matches.

        Parameters:
            nested_map (Mapping): the nested dictionary
            path (Sequence): list of keys forming path to the desired value
            expected_excep: the expected exception type to be raised
            expected_msg: the expected exception message.

        Returns:
            None: this test does not return anything.
        """
        with self.assertRaises(expected_excep) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_msg)


class TestGetJson(unittest.TestCase):
    """
    Test suite for the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function using parameterized tests and mocking
        requests.get.

        Parameters:
            test_url (str): the test URL
            test_payload (dict): the required response from requesting the url
            mock_get (Mock): the mocked requests.get object
        """
        self.assertTrue(isinstance(mock_get, Mock))

        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)

        self.assertEqual(result, test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test suite for the memoize function
    """
    def test_memoize(self):
        """
        Test the memoize function

        Parameters:
            None
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=20)\
                as mock_method:
            object = TestClass()

            result1 = object.a_property
            result2 = object.a_property

        self.assertEqual(result1, 20)
        self.assertEqual(result2, 20)

        mock_method.assert_called_once_with()
