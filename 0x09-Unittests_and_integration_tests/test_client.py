#!/usr/bin/env python3
""" Module test clients"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock
from typing import Any


class TestGithubOrgClient(unittest.TestCase):
    """ Tests github_org_client """

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": True})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected_result: Any, mock_get) -> None:
        """ Test org method"""
        mock_json = Mock(return_value=expected_result)
        mock_get.return_value = Mock(json=mock_json)

        result = GithubOrgClient(org_name=org_name).org
        self.assertEqual(result, mock_get.return_value)
        mock_get.assert_called_once()
