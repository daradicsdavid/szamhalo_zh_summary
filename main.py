import threading

from udp.simple.UdpClient import start_udp_client
from udp.simple.UdpServer import start_udp_server
from util.Struct import structExample
from tcp.select.SelectClient import start_select_client
from tcp.select.SelectServer import start_select_server
from tcp.simple.Client import start_client
from tcp.simple.Server import start_server


def start_server_and_client():
    server_thread = threading.Thread(name='server', target=start_server)
    client_thread = threading.Thread(name='client', target=start_client)
    server_thread.setDaemon(1)
    client_thread.setDaemon(1)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()


def start_select_server_and_client():
    server_thread = threading.Thread(name='select_server', target=start_select_server)
    client_thread = threading.Thread(name='select_client', target=start_select_client)
    server_thread.setDaemon(1)
    client_thread.setDaemon(1)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()


def start_udp_server_and_client():
    server_thread = threading.Thread(name='server', target=start_udp_server)
    client_thread = threading.Thread(name='client', target=start_udp_client)
    server_thread.setDaemon(1)
    client_thread.setDaemon(1)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()


if __name__ == '__main__':
    # start_server_and_client()
    # start_select_server_and_client()
    # structExample()
    start_udp_server_and_client()
