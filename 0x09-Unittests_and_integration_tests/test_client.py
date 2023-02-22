#!/usr/bin/env python3
""" Module test clients"""
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from typing import Dict
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Unittest github_org_client """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get) -> None:
        """ Test org method"""
        mock_get.return_value = {}

        result = GithubOrgClient(org_name=org_name).org
        self.assertEqual(result, mock_get.return_value)
        mock_get.assert_called_once()

    def test_public_repos_url(self) -> None:
        """ Test _public_repos_url method """
        mock_obj = 'client.GithubOrgClient.org'
        mock_value = {'repos_url': 'https://api.github.com/orgs/google'}

        with patch(mock_obj,
                   new_callable=PropertyMock,
                   return_value=mock_value) as mock_repos_url:
            result = GithubOrgClient("Google").org
            self.assertEqual(result, mock_repos_url.return_value)

    @patch('client.get_json')
    def test_public_repos(self, mock_get) -> None:
        """ Test public_repos method """
        mock_get.return_value = [{'name': 'Google'}]

        mock_obj = 'client.GithubOrgClient._public_repos_url'
        mock_value = "https://api.github.com/orgs/google"

        with patch(mock_obj,
                   new_callable=PropertyMock,
                   return_value=mock_value) as mock_public_repos:
            result = GithubOrgClient("Google").public_repos()
            self.assertEqual(result, ['Google'])
            mock_get.assert_called_once()
            mock_public_repos.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected_value) -> None:
        """ Test has_license method """
        result = GithubOrgClient.has_license(repo=repo,
                                             license_key=license_key)
        self.assertEqual(result, expected_value)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test github_org_client """

    @classmethod
    def setUpClass(cls):
        """ Class call before tests and Start a patcher """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        mock_org = Mock(return_value=cls.org_payload)
        mock_org.json = mock_org

        mock_repos = Mock(return_value=cls.repos_payload)
        mock_repos.json = mock_repos

        my_side_effect = [mock_org, mock_repos, mock_org, mock_repos]
        cls.mock_get.side_effect = my_side_effect

    @classmethod
    def tearDownClass(cls):
        """ Class call after tests and Close the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """ Test public_repos method """
        result = GithubOrgClient("Google").public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """ Test has_license """
        result = GithubOrgClient("Google").public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)
