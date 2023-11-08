```python
import random

def play(switch):
    doors = [0, 0, 1]  # 0 represents no prize, 1 represents a prize
    choice = random.randint(0, 2)
    reveal = random.choice([i for i in range(3) if i != choice and doors[i] == 0])
    if switch:
        choice = [i for i in range(3) if i != choice and i != reveal][0]
    return doors[choice]

def win_count(switch):
    wins = 0
    for _ in range(1000):
        if play(switch) == 1:
            wins += 1
    return wins

def main():
    switch_wins = win_count(True)
    stay_wins = win_count(False)
    print("Switching wins:", switch_wins)
    print("Staying wins:", stay_wins)

main()
```