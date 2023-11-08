def total_characters(strings):
    total = 0
    for s in strings:
        total += len(s)
    return total

print(total_characters(["apple", "orange"]))