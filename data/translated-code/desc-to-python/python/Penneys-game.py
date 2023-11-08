import random
import time

players = ["Player 1", "Player 2"]
starting_player = random.choice(players)

print(f"{starting_player} will go first.")

user_input = input("Enter a sequence of three heads or tails (e.g. HHT): ")

while True:
    coin_sequence = ''.join(random.choice(['H', 'T']) for _ in range(3))
    print(coin_sequence)
    time.sleep(1)

    if coin_sequence == user_input:
        print(f"{starting_player} wins!")
        break
    else:
        starting_player = players[1] if starting_player == players[0] else players[0]