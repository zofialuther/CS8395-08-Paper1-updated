def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight, value, quantity = items[i-1]
            for q in range(min(quantity, w // weight) + 1):
                dp[i][w] = max(dp[i][w], dp[i-1][w - q*weight] + q*value)
    
    return dp[n][capacity]

def main():
    items = [(10, 60, 3), (20, 100, 2), (30, 120, 1)]
    capacity = 400
    optimal_value = knapsack(items, capacity)
    print(optimal_value)

if __name__ == "__main__":
    main()