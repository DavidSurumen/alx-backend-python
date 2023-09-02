#!/usr/bin/env python3
"""
Test module for github organisations client
"""
from client import (
    GithubOrgClient,
    get_json,
)
from unittest.mock import (
    patch,
    Mock,
)
from parameterized import parameterized
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for GithubOrgClient class
    """
    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, test_org, test_payload, mock_get_json):
        """
        Test that org method returns dictionary of organisations.
        """
        object = GithubOrgClient(test_org)
        mock_get_json.return_value = test_payload
        self.assertTrue(isinstance(mock_get_json, Mock))

        result = object.org

        self.assertEqual(result, test_payload)

        org_url = object.ORG_URL.format(org=test_org)
        mock_get_json.assert_called_once_with(org_url)
