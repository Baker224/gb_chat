import unittest
from gb_chat.client import create_presence_message, parse_response


class ClientTestCase(unittest.TestCase):

    def test_create_presence_message(self):
        expected_message = '{"action": "presence", "user": {"account_name": "user1"}}'
        message = create_presence_message()
        self.assertEqual(message, expected_message)

    def test_parse_response(self):
        response = '{"response": 200, "alert": "OK"}'
        parsed_response = parse_response(response)
        expected_response = {'response': 200, 'alert': 'OK'}
        self.assertEqual(parsed_response, expected_response)


if __name__ == '__main__':
    unittest.main()
