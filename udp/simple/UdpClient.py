import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
UDP_PORT = 65432  # The port used by the server


def start_udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = b'Hello, world'
        print('Sending', repr(message), "\n")
        s.sendto(message, (HOST, UDP_PORT))
        data, address = s.recvfrom(1024)
        print('Received', repr(data), 'from:', address)
