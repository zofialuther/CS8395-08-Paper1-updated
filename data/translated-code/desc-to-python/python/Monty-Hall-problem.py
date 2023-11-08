```python
import random

def monty_hall_simulator(iterations):
    switch_wins = 0
    stay_wins = 0

    for i in range(iterations):
        prize_door = random.randint(1, 3)
        selected_door = random.randint(1, 3)

        revealed_door = random.choice([door for door in range(1, 4) if door != prize_door and door != selected_door])

        if selected_door != prize_door:
            switch_wins += 1
        else:
            stay_wins += 1

    print(f"Switching doors wins {switch_wins} out of {iterations} times")
    print(f"Not switching doors wins {stay_wins} out of {iterations} times")

    print("For more information on the Monty Hall problem, visit: https://en.wikipedia.org/wiki/Monty_Hall_problem")
```