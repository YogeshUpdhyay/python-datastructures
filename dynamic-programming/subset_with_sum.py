def countSubsets(n, arr):
    
    dp = [[0]*(n+1) for _ in range(len(arr)+1)]
    for i in dp:
        i[0] = 1

    i = 1
    while i < len(arr)+1:
        j = 1
        while j < n+1:
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
            j+=1
        i+=1
    
    return dp[i-1][j-1]

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(" ")))
    print(countSubsets(n, arr))