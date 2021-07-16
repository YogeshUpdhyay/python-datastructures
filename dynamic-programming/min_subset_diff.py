import sys

def min_subset_diff(arr):
    n = sum(arr)

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
    
    diff = sys.maxsize
    for i, val in enumerate(dp[-1][0:(n//2)+1]):
        if val:
            diff = min(diff, n-(2*i))
    return diff

if __name__ == '__main__':
    arr = list(map(int, input().strip().split(" ")))
    print(min_subset_diff(arr))