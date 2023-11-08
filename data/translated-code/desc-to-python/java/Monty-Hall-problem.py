import random

def monty_hall_simulation():
    switch_wins = 0
    stay_wins = 0
    
    for i in range(32768):
        prize_door = random.randint(1, 3)
        player_choice = random.randint(1, 3)
        
        revealed_door = random.choice([door for door in [1, 2, 3] if door != player_choice and door != prize_door])
        
        if player_choice == prize_door:
            stay_wins += 1
        else:
            switch_wins += 1
    
    print("Wins when staying with original choice:", stay_wins)
    print("Wins when switching doors:", switch_wins)

monty_hall_simulation()