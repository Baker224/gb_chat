import sys
import json
import socket

def create_presence_message():
    message = {
        'action': 'presence',
        'user': {
            'account_name': 'user1'
        }
    }
    return json.dumps(message)

def send_message(sock, message):
    sock.sendall(message.encode())

def receive_response(sock):
    response = sock.recv(1024)
    return response.decode()

def parse_response(response):
    return json.loads(response)

def main():
    if len(sys.argv) < 2:
        print("Usage: client.py <addr> [<port>]")
        return

    server_address = sys.argv[1]
    server_port = int(sys.argv[2]) if len(sys.argv) >= 3 else 7777

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_address, server_port))

    presence_message = create_presence_message()
    send_message(sock, presence_message)

    response = receive_response(sock)
    parsed_response = parse_response(response)
    print("Response:", parsed_response)

    sock.close()

if __name__ == '__main__':
    main()
