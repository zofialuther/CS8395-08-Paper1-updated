```python
import random

def do_it(N):
    Cards, Sets = card_sets(N)
    print('Cards: ')
    for card in Cards:
        print_card(card)
    print('Sets: ')
    for s in Sets:
        print_set(s)

def print_card(Card):
    print(f'  {Card[0]} {Card[1]} {Card[2]} {Card[3]}')

def print_set(Set):
    for card in Set:
        print_card(card)
    print()

def n(N, L):
    return N, L

def card_sets(N):
    Cards = random_deal(N)
    Sets = [set for set in get_all_sets(Cards)]
    return Cards, Sets

def random_card():
    colors = ['red', 'green', 'purple']
    shapes = ['oval', 'squiggle', 'diamond']
    numbers = ['one', 'two', 'three']
    shading = ['solid', 'open', 'striped']
    return [random.choice(colors), random.choice(shapes), random.choice(numbers), random.choice(shading)]

def random_deal(N):
    return [random_card() for _ in range(N)]

def is_card_set(Cards):
    for c1 in Cards:
        for c2 in Cards:
            for c3 in Cards:
                if c1 != c2 and c2 != c3 and c1 != c3:
                    if match(c1, c2, c3):
                        yield {c1, c2, c3}

def match(c1, c2, c3):
    for i in range(4):
        if c1[i] == c2[i] == c3[i] or c1[i] != c2[i] != c3[i] and c1[i] != c3[i]:
            continue
        else:
            return False
    return True
```