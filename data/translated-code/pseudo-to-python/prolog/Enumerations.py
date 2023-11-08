fruit = {
    "apple": 1,
    "banana": 2,
    "cherry": 4
}

def write_fruit_name(N):
    for name, value in fruit.items():
        if value == N:
            print(f"It is a {name}")

write_fruit_name(1)
write_fruit_name(2)
write_fruit_name(4)