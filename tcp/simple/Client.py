import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = b'Hello, world'
        print('Sending', repr(message), "\n")
        s.sendall(message)
        data = s.recv(1024)
        print('Received', repr(data))
