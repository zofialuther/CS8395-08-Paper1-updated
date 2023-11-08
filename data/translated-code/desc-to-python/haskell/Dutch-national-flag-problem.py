```python
import random

class Color:
    RED = 'red'
    WHITE = 'white'
    BLUE = 'blue'

def sort_colors(colors):
    return sorted(colors, key=lambda x: (x != Color.RED, x != Color.WHITE))

def is_sorted_dutch_flag(colors):
    return all(colors[i] <= colors[i+1] for i in range(len(colors)-1))

def main():
    colors = [random.choice([Color.RED, Color.WHITE, Color.BLUE]) for _ in range(10)]
    print("Original sequence:", colors)
    
    if not is_sorted_dutch_flag(colors):
        sorted_colors = sort_colors(colors)
        print("Sorted sequence:", sorted_colors)
    else:
        print("Sequence is already sorted according to Dutch national flag colors.")

if __name__ == "__main__":
    main()
```