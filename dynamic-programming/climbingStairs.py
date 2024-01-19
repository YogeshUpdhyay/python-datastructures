# def climbStairs(n):
#     dp = [0]*(n+1)
#     dp[0] = 1

#     for i in range(1,n+1):
#         dp[i] = (dp[i-1] if i-1 >= 0 else 0) + (dp[i-2] if i-2 >= 0 else 0)
    
#     return dp[n]


# recursive approach
def noOfWays(n, dp):
        if n == 0:
            return 1

        result = 0

        for i in [1, 2]:
            if n - i >= 0:
                if dp[n-i] != -1:
                    result += dp[n-i]
                else:
                    result += noOfWays(n - i, dp)

        dp[n] = result

        return result

def climbStairs( n: int) -> int:
    dp = [-1] * (n+1)
    
    return noOfWays(n ,dp)


print(climbStairs(4))