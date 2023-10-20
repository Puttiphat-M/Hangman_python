import argparse
import socket

def main(port):
    host = "192.168.68.54"
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("Client side:")
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        print(data, end="")
        guess = input("Your next guess: ")
        client.send(guess.encode())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hangman Server")
    parser.add_argument("port", type=int, help="Port number to listen on")

    args = parser.parse_args()

    server_socket = main(args.port)