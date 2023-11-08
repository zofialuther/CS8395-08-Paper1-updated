def combs(item, capacity):
    if not item:
        return [(0, [])]
    else:
        return combs(item[1:], capacity) + \
               ([] if item[0][1] > capacity else \
               [(item[0][2] + x[0], [item[0]] + x[1]) for x in combs(item[1:], capacity - item[0][1])])

def main():
    print("Total value: ")
    print(value)
    for item in items:
        print(item)
    
    value, items = max(combs(inv, 400))
    print(value, items)