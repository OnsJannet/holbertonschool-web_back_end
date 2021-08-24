#!/usr/bin/env python3
'''Testing
'''

import unittest
from utils import access_nested_map
from parameterized import parameterized


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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path, ret_error):
        '''
        tests that a KeyError is raised for the following inputs.
        '''
        with self.assertRaises(TypeError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(ret_error, error.exception)
