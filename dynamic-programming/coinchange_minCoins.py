import sys

def minCoins(n, arr, dp):
	if n == 0:
		return 0

	ans = sys.maxsize

	for i in arr:
		if n-i >= 0:
			if dp[n-i] != -1:
				subans = dp[n-i]
			else:
				subans = minCoins(n-i, arr, dp)
			if (subans != sys.maxsize and subans+1 < ans):
				ans = subans + 1
	dp[n] = ans
	return ans


if __name__ == '__main__':
	n = int(input().strip())

	arr = list(map(int, input().split()))

	dp = [-1]*(n+1)
	dp[0] = 0

	result = minCoins(n, arr, dp)
	
	print(result)

