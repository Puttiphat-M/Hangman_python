import argparse
import socket
import time

def main(port):
    host = "192.168.68.54"
    status = False
    while not status:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            status = True
        except:
            print("Server is not up yet, trying again in 5 seconds")
            time.sleep(5)
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        print(data, end="")
        
        if "You won" in data:
            break
        elif "You lost" in data:
            break
        else:
            guess = input("Your next Guess: ")
            while len(guess) != 1 or not guess.isalpha():
                guess = input("Please enter a single letter: ")
            #check server is still up
            try:
                client.send(guess.encode())
            except:
                break

    client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hangman Server")
    parser.add_argument("port", type=int, help="Port number to listen on")

    args = parser.parse_args()

    server_socket = main(args.port)
