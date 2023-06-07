import socket
import json
import sys
from gb_chat.log.server_log_config import logger, log


@log
def create_response(message):
    response = {
        'response': 200,
        'message': 'OK',
        'data': message
    }
    return response


def send_response(sock, response):
    json_response = json.dumps(response)
    data = json_response.encode('utf-8')
    sock.send(data)


def receive_message(sock):
    data = sock.recv(1024)
    json_message = data.decode('utf-8')
    message = json.loads(json_message)
    return message


def parse_message(message):
    if 'action' in message and message['action'] == 'presence':
        logger.info('Received presence message from user: %s', message['user']['account_name'])
        return 'Presence message received'
    else:
        return 'Invalid message'


def main():
    server_port = int(sys.argv[1]) if len(sys.argv) > 1 else 7777
    server_address = sys.argv[2] if len(sys.argv) > 2 else ''

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((server_address, server_port))
        sock.listen(1)
        logger.info('Server started')

        while True:
            logger.info('Waiting for a connection...')
            client_sock, client_address = sock.accept()
            logger.info('Accepted connection from %s', client_address)

            message = receive_message(client_sock)
            result = parse_message(message)

            response = create_response(result)
            send_response(client_sock, response)

            client_sock.close()
            logger.info('Connection closed')

    except OSError as e:
        logger.error('Error: %s', e)

    finally:
        sock.close()


if __name__ == '__main__':
    main()
