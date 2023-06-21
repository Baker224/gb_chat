import unittest
from unittest.mock import patch
from gb_chat.server import create_response, send_response, receive_message, parse_message


class ServerTestCase(unittest.TestCase):

    def test_create_response(self):
        message = 'Test message'
        expected_response = {
            'response': 200,
            'message': 'OK',
            'data': message
        }
        response = create_response(message)
        self.assertEqual(response, expected_response)

    def test_send_response(self):
        mock_socket = MockSocket()
        response = {
            'response': 200,
            'message': 'OK',
            'data': 'Test response'
        }
        expected_json_response = '{"response": 200, "message": "OK", "data": "Test response"}'
        send_response(mock_socket, response)
        self.assertEqual(mock_socket.sent_data, expected_json_response)

    def test_receive_message(self):
        mock_socket = MockSocket()
        json_message = '{"action": "test", "data": "Hello"}'
        expected_message = {
            'action': 'test',
            'data': 'Hello'
        }
        mock_socket.recv_data = json_message.encode('utf-8')
        message = receive_message(mock_socket)
        self.assertEqual(message, expected_message)

    @patch('builtins.print')
    def test_parse_message_valid_presence(self, mock_print):
        message = {
            'action': 'presence',
            'user': {
                'account_name': 'user1'
            }
        }
        result = parse_message(message)
        self.assertEqual(result, 'Presence message received')
        mock_print.assert_called_with('Received presence message from user:', 'user1')

    def test_parse_message_invalid_message(self):
        message = {
            'action': 'test',
            'data': 'Hello'
        }
        result = parse_message(message)
        self.assertEqual(result, 'Invalid message')


class MockSocket:
    def __init__(self):
        self.sent_data = None
        self.recv_data = None

    def send(self, data):
        self.sent_data = data.decode('utf-8')

    def recv(self, size):
        return self.recv_data


if __name__ == '__main__':
    unittest.main()
