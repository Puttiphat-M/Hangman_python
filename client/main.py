import socket
import json

def setup_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    return client_socket

def request_new_game(client_socket):
    game_state = json.loads(client_socket.recv(1024).decode())
    return game_state

def guess_letter(client_socket, letter):
    client_socket.send(letter.encode())
    game_state = json.loads(client_socket.recv(1024).decode())
    return game_state

def is_game_over(game_state):
    if game_state["attempts_remaining"] <= 0:
        return True
    if '_' not in game_state["guessed_word"]:
        return True
    return False

def display_game_state(game_state):
    word_display = ' '.join(game_state["guessed_word"])
    attempts_remaining = game_state["attempts_remaining"]
    print(f"{word_display} you have {attempts_remaining} guess left")

def run_client():
    client_socket = setup_client()
    used_letters = set()

    while True:
        game_state = request_new_game(client_socket)
        display_game_state(game_state)

        if is_game_over(game_state):
            if '_' not in game_state["guessed_word"]:
                print(f'You won\nThe word is {game_state["word"]}, you have {game_state["attempts_remaining"]} guesses left')
            else:
                print(f'You lose\nThe word was: {game_state["word"]}')
            break

        guess = input('Your next guess: ').strip().lower()
        if guess and guess not in used_letters:
            used_letters.add(guess)

            # After sending the guess to the server
            client_socket.send(guess.encode())

            # Wait for the server's response
            client_socket.recv(1024).decode()

            game_state = guess_letter(client_socket, guess)
            display_game_state(game_state)
        elif guess in used_letters:
            print(f"You've already guessed '{guess}'. Please choose a different letter.")
        else:
            print("Invalid input. Please enter a single alphabetic character.")

if __name__ == '__main__':
    run_client()
