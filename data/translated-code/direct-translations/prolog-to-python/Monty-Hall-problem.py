import random

def play(switch):
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
    return f == p

def win_count(i, switch):
    total = 0
    for _ in range(i):
        if play(switch):
            total += 1
    return total

def main():
    random.seed()
    switch_total = win_count(1000, True)
    stay_total = win_count(1000, False)
    print(f"Switching wins {switch_total} out of 1000.")
    print(f"Staying wins {stay_total} out of 1000.")

if __name__ == "__main__":
    main()