```python
import random

def main():
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    moves = 0
    
    while numbers != sorted(numbers):
        print("Current list:", numbers)
        index = int(input("Enter the index of the number to reverse: "))
        numbers[:index] = numbers[:index][::-1]
        moves += 1
        
    print("Congratulations! You sorted the list in", moves, "moves.")

if __name__ == "__main__":
    main()
```