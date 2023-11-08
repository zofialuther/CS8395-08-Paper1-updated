```python
class CountTheCoins:
    def countChanges(self, coins, amount):
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]

def main():
    ctc = CountTheCoins()
    coins1 = [1, 2, 5]
    amount1 = 5
    print(ctc.countChanges(coins1, amount1))  # Output: 4
    
    coins2 = [2, 3, 6]
    amount2 = 10
    print(ctc.countChanges(coins2, amount2))  # Output: 5

if __name__ == "__main__":
    main()
```