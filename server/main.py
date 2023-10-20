import argparse
from setUpServer import setup_server

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hangman Server")
    parser.add_argument("port", type=int, help="Port number to listen on")

    args = parser.parse_args()

    server_socket = setup_server(args.port)