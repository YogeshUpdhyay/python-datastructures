def climbStairs(n):
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1,n+1):
        dp[i] = (dp[i-1] if i-1 >= 0 else 0) + (dp[i-2] if i-2 >= 0 else 0)
    
    return dp[n]


print(climbStairs(3))