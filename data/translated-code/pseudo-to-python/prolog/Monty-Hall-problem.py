import random

def main():
    random.seed()
    switch_total = win_count(1000, True, 0)
    print(f"Switching wins {switch_total} out of 1000.")
    stay_total = win_count(1000, False, 0)
    print(f"Staying wins {stay_total} out of 1000.")

def play(switch, won):
    p = random.randint(1, 3)
    c = random.randint(1, 3)
    
    while True:
        r = random.randint(1, 3)
        if r != p and r != c:
            break
    
    if switch:
        for f in range(1, 4):
            if f != c and f != r:
                break
    else:
        f = c
    
    if f == p:
        won = True
    else:
        won = False

def win_count(i, switch, total):
    if i == 0:
        return total
    else:
        i -= 1
        won = play(switch, total)
        if won:
            total += 1
        return win_count(i, switch, total)