def knapsack_solver(items, max_weight):
    memo = {}

    def solve(i, weight):
        if i < 0:
            return 0, []
        if (i, weight) in memo:
            return memo[(i, weight)]

        if items[i][1] > weight:
            result = solve(i - 1, weight)
        else:
            r1 = solve(i - 1, weight)
            r2 = solve(i - 1, weight - items[i][1])
            r2 = (r2[0] + items[i][0], r2[1] + [items[i]])

            result = r1 if r1[0] > r2[0] else r2

        memo[(i, weight)] = result
        return result

    result = solve(len(items) - 1, max_weight)
    total_value, selected_items = result

    print("Selected items:", selected_items)
    print("Total value:", total_value)
    print("Total weight:", sum(item[1] for item in selected_items))