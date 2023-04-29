import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from server_for_tests import create_response_to_client


class TestClass(unittest.TestCase):
    def test_empty_message(self):
        self.assertEqual(create_response_to_client('empty_message')['response'], 400)
    
    def test_get_name(self):
        self.assertEqual(create_response_to_client({'action': 'presence', 'time': 'any', 'user': {'account_name': 'Vadim'}})['message'],
                          'Hello from server, Vadim')
    
    def test_guest(self):
        self.assertEqual(create_response_to_client({'action': 'presence', 'time': 'any', 'user': {}})['message'],
                          'Dear Guest, welcome to the server!')
    
    def type_error(self):
        self.assertRaises(TypeError, create_response_to_client)


if __name__ == '__main__':
    unittest.main()