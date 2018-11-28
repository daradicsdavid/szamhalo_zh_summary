import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
UDP_PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def start_udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, UDP_PORT))
        s.settimeout(1)
        while True:
            try:
                data, address = s.recvfrom(1024)
                print('Client connected by', address, '\n')
                s.sendto(data, address)
            except socket.timeout:
                break