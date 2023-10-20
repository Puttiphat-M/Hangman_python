import socket
import threading
from handleClient import handle_client


def setup_server(port):
        # enter your ip address here
        host = "192.168.68.50"
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the specified host and port
        server_socket.bind((host, port))

        # Start listening for incoming client connections
        server_socket.listen(1) # Only accept 1 connection at a time

        print("Waiting for client connection")
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
