#!/usr/bin/env python3
"""
Unit tests module for the access_nested_map function
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
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
