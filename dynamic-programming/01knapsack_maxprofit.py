
def maxProfit(c, n, w, p, dp):
    for i in range(1, n+1):
        for j in range(1,c+1):
            if j >= w[i-1]:
                curr_max = (p[i-1]+dp[i-1][j-w[i-1]])

                if (curr_max >= dp[i-1][j]):
                    dp[i][j] =  curr_max
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[i][j]

    return 0
if __name__ == '__main__':
    c = int(input().strip())

    w = list(map(int, input().split(" ")))

    p = list(map(int, input().split(" ")))

    n = len(w)
    #  filling base conditions
    dp = [[-1]*(c+1) for _ in range(n+2)]
    for i in dp:
        i[0] = 0
    dp[0] = [0]*(c+1)

    result = maxProfit(c, n, w, p, dp)

    print(result)
