#!/usr/bin/env python3
""" Module test clients"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from typing import Any


class TestGithubOrgClient(unittest.TestCase):
    """ Tests github_org_client """

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
        """ Test public_repos """
        mock_get.return_value = [{'name': 'Google'}]

        mock_obj = 'client.GithubOrgClient._public_repos_url'
        mock_value = "Google"

        with patch(mock_obj,
                   new_callable=PropertyMock,
                   return_value=mock_value) as mock_public_repos:
            result = GithubOrgClient("Google").public_repos()
            self.assertEqual(result, ['Google'])
            mock_get.assert_called_once()
            mock_public_repos.assert_called_once()
