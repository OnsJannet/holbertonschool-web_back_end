#!/usr/bin/env python3
'''Testing
'''
import unittest
from unittest import mock
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import PropertyMock, Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    '''
    a test class that inherits from unittest.TestCase
    '''
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, url, payload, get_patch):
        '''
        test that GithubOrgClient.org returns the correct value.
        '''
        get_patch.return_value = payload
        github_client = GithubOrgClient(url)
        response = github_client.org
        self.assertEqual(response, payload)
        get_patch.assert_called_once()

    def test_public_repos_url(self):
        '''
        Test that the result of _public_repos_url
        is the expected one based on the mocked payload.
        '''
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock) as mock_o:
            test_json = {"url": "facebook",
                         "repos_url": "http://taylorswift.com"}
            mock_o.return_value = test_json
            github_client = GithubOrgClient(test_json.get("url"))
            response = github_client._public_repos_url
            mock_o.assert_called_once()
            self.assertEqual(response, test_json.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, get_patch):
        '''
        Test that the list of repos is what you expect from the chosen payload.
        '''
        get_patch.return_value = [{"name": "google"},
                                  {"name": "abc"}]
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_o:
            mock_o.return_value = "http://taylorswift.com"
            github_client = GithubOrgClient("facebook")
            response = github_client.public_repos()
            self.assertEqual(response, ["google", "abc"])
            get_patch.assert_called_once()
            mock_o.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        '''
        Testing for test_has_license
        '''
        github_client = GithubOrgClient("facebook")
        response = (github_client.has_license(repo, license))
        self.assertEqual(response, expected)


if __name__ == '__main__':
    unittest.main()
