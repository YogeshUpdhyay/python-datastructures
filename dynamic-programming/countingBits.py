def countBits(n):
    ans = [-1]*(n+1)
    ans[0] = 0
    for i in range(1, n+1):
        ans[i] = ans[i//2] + i%2
    return ans

print(countBits(3))