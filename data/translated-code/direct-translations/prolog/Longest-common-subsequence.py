import time

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [["" for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + s1[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
    
    return dp[m][n]

start_time = time.time()
result = lcs("beginning-middle-ending", "beginning-diddle-dum-ending")
end_time = time.time()

print(result)
print("Time taken: ", end_time - start_time)