```python
import random

class ReversalGame:
    def __init__(self):
        self.game_list = list(range(1, 10))
        while self.is_sorted():
            random.shuffle(self.game_list)

    def play(self):
        move_count = 0
        while True:
            print(self.game_list)
            i = int(input("Please enter an index to reverse from 2 to 9. Enter 99 to quit: "))
            if i == 99:
                break
            if i < 2 or i > 9:
                print("Invalid input")
            else:
                move_count += 1
                self.reverse(i)
                if self.is_sorted():
                    print(f"Congratulations you solved this in {move_count} moves!")
                    break

    def reverse(self, position):
        self.game_list[:position] = self.game_list[:position][::-1]

    def is_sorted(self):
        return all(self.game_list[i] <= self.game_list[i + 1] for i in range(len(self.game_list) - 1))

if __name__ == "__main__":
    game = ReversalGame()
    game.play()
```