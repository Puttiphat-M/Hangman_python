import socket
import threading
from handleClient import handle_client


def setup_server(port):
        # enter your ip address here
        host = "192.168.68.54"
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the specified host and port
        server_socket.bind((host, port))

        # Start listening for incoming client connections
        server_socket.listen(1) 

        print("Waiting for client connection")
        while True:
            client_socket, addr = server_socket.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
