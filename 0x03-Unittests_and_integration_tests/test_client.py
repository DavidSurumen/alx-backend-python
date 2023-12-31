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
    PropertyMock,
)
from parameterized import (
    parameterized,
    parameterized_class,
)
import unittest
from fixtures import TEST_PAYLOAD
from requests import HTTPError


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

    @parameterized.expand([
        ('this_org1', {'repos_url': "public-repo-url"}),
    ])
    def test_public_repos_url(self, this_org1, test_payload):
        """
        doc
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock)\
                as mock_org:
            mock_org.return_value = test_payload
            self.assertTrue(isinstance(mock_org, Mock))

            result = GithubOrgClient(this_org1)._public_repos_url

        self.assertEqual(result, "public-repo-url")
        mock_org.assert_called_once_with()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos method returns a list of repositories
        """
        test_payload = {
                'repos_url': "some url",
                'repos': [
                    {
                        "name": "repo 1"
                    },
                    {
                        "name": "repo 2"
                    }
                ]
        }
        mock_get_json.return_value = test_payload["repos"]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = test_payload["repos_url"]
            object = GithubOrgClient('test')
            result = object.public_repos()

            self.assertEqual(result, [
                "repo 1",
                "repo 2"
                ])
            mock_repo_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "my_license"}}, "my_license", True),
        ({'license': {'key': "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, test_repo, test_license_key, expected):
        """
        Test that has_license method returns boolean whether or not a
        given repository has the passed license key.
        """
        client = GithubOrgClient('google')
        bool = client.has_license(test_repo, test_license_key)

        self.assertEqual(bool, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
      TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient.public_repos method
    """
    @classmethod
    def setUpClass(cls):
        """
        sets up class fixtures
        """
        route_payload = {
                'https://api.github.com/orgs/google': cls.org_payload,
                'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """
        Test public_repos method against the fixtures
        """
        obj = GithubOrgClient('google')
        public_repos = obj.public_repos()

        self.assertEqual(public_repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the public_repos method with license, against the fixtures
        """
        license = "apache-2.0"
        obj = GithubOrgClient('google')
        public_repos = obj.public_repos(license)

        self.assertEqual(public_repos, self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """
        removes the class fixtures
        """
        cls.get_patcher.stop()
