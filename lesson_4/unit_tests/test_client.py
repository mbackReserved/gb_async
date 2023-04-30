import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from client_for_tests import resp_from_server

class TestClass(unittest.TestCase):
    def test_status_code_200(self):
        self.assertEqual(resp_from_server({'response': 200, 'message': 'Test Message'}), 200)

    def test_status_code_400(self):
        self.assertEqual(resp_from_server({'response': 400, 'message': 'Test Message'}), 400)
    
    def test_key_error(self):
        self.assertEqual(resp_from_server({'response': 200}), 'Не получены необходимые данные от сервера')
    
    def test_type_error(self):
        self.assertRaises(TypeError, resp_from_server)


if __name__ == '__main__':
    unittest.main()