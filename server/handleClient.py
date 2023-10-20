
import random
import threading

word_list = ["glasses", "elephant", "programming", "hangman", "bottle"]

chosen_word = random.choice(word_list)

guessed_word = ["-" for _ in chosen_word]

max_guesses = 10

lock = threading.Lock()
def handle_client(client_socket):
    global max_guesses
    global chosen_word
    global guessed_word
    try:
        while max_guesses > 0:
            if type(chosen_word) == str:
                client_socket.send(f"{''.join(guessed_word)} you have {max_guesses} Guess left\n".encode())
                guess = client_socket.recv(1).decode()

                with lock:
                    if guess in chosen_word:
                        for i in range(len(chosen_word)):
                            if chosen_word[i] == guess:
                                guessed_word[i] = guess
                    else:
                        max_guesses -= 1

                if ''.join(guessed_word) == chosen_word:
                    client_socket.send("You won\n".encode())
                    break

                elif max_guesses == 0:
                        client_socket.send(f"You lost, the word was {chosen_word}\n".encode())
                        break
            else:
                client_socket.send("The word is not a string\n".encode())

        client_socket.send(f"The word is {chosen_word}, you have {max_guesses} Guess left\n".encode())
    except:
        pass

    client_socket.close()