
def isSubset(n, arr):
    dp = [[False]*(n+1) for _ in range(len(arr)+1)]
    for i in dp:
        i[0] = True

    i = 1
    while i < len(arr)+1:
        j = 1
        while j < n+1:
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                if dp[i-1][j] or dp[i-1][j-arr[i-1]]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            j += 1
        i += 1
    
    return dp[i-1][j-1]

    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(" ")))
    print(isSubset(n, arr))