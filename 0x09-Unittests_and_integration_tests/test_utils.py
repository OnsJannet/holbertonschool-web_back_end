#!/usr/bin/env python3
'''Testing
'''

import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch



class TestAccessNestedMap(unittest.TestCase):
    '''
    a test class that inherits from unittest.TestCase
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, returned):
        '''
        tests that the method returns what it is supposed to.
        '''
        self.assertEqual(access_nested_map(nested_map, path), returned)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, ret_error):
        '''
        tests that a KeyError is raised for the following inputs.
        '''
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(ret_error, str(error.exception))


class TestGetJson(unittest.TestCase):
    '''
    a test class that inherits from unittest.TestCase
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        '''
        tests that utils.get_json returns the expected result.
        '''
        response = mock.Mock()
        response.json.return_value = payload

        with mock.patch('requests.get', return_value=response):
            request = get_json(url)
            self.assertEqual(request, payload)
            response.json.assert_called_once()


class TestMemoize(TestCase):
    '''
    a test class that inherits from unittest.TestCase
    '''

    def test_memoize(self):
        ''' Test that when calling a_property twice,
        the correct result is returned but a_method is only
        called once using assert_called_once.
        '''

        class TestClass:
            ''' Test class
            '''

            def a_method(self):
                ''' returns 42
                '''
                return 42

            @memoize
            def a_property(self):
                ''' Returns memoized property
                '''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            returned = test_class.a_property
            returned = test_class.a_property

            self.assertEqual(returned, 42)
            patched.assert_called_once()


if __name__ == '__main__':
    unittest.main()
