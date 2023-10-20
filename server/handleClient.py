import random
import threading
import socket

lock = threading.Lock()

word_list = ["glasses", "elephant", "programming", "hangman", "bottle"]

def play_game(client_socket):
    chosen_word = random.choice(word_list)
    max_guesses = 10
    guessed_word = ["-" for _ in chosen_word]

    try:
        while max_guesses > 0:
            client_socket.send(f"{''.join(guessed_word)} you have {max_guesses} Guess left\n".encode())
            guess = client_socket.recv(len(chosen_word)).decode()
            with lock:
                if guess in chosen_word:
                    for i in range(len(chosen_word)):
                        if chosen_word[i] == guess:
                            guessed_word[i] = guess
                else:
                    max_guesses -= 1

            if ''.join(guessed_word) == chosen_word:
                client_socket.send(f"You won\nthe word was {chosen_word} you have {max_guesses} Guess left\n".encode())
                break
            elif max_guesses == 0:
                client_socket.send(f"You lost, the word was {chosen_word}\n".encode())
                break
    except:
        pass
    client_socket.close()
    
def handle_client(client_socket):
    play_game(client_socket)
