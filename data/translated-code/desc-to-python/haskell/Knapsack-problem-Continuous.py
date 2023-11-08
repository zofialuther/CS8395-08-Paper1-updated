items = [('item1', 10, 2), ('item2', 5, 3), ('item3', 15, 5), ('item4', 7, 7), ('item5', 6, 1)]

def sortBy(item):
    return item[1] / item[2]

def solution(capacity, items):
    items.sort(key=sortBy, reverse=True)
    knapsack = []
    total_value = 0
    total_weight = 0
    for item in items:
        if total_weight + item[2] <= capacity:
            knapsack.append(item[0])
            total_value += item[1]
            total_weight += item[2]
    return knapsack, total_value, total_weight

def main():
    knapsack_capacity = 15
    result = solution(knapsack_capacity, items)
    print(result)

main()