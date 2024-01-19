import sys

# def minCoins(n, arr, dp):
# 	if n == 0:
# 		return 0

# 	ans = sys.maxsize

# 	for i in arr:
# 		if n-i >= 0:
# 			if dp[n-i] != -1:
# 				subans = dp[n-i]
# 			else:
# 				subans = minCoins(n-i, arr, dp)
# 			if (subans != sys.maxsize and subans+1 < ans):
# 				ans = subans + 1
# 	dp[n] = ans
# 	return ans

# testing out the dp method
def minCoins(n, arr, dp):
	if n == 0:
		return 0
	
	result = sys.maxsize
	
	for i in arr:
		if n - i >= 0:
			if dp[n-i] != 0:
				sub_ans = dp[n-i]
			else:
				sub_ans = minCoins(n - i, arr, dp)
			if sub_ans != -1:
				result = min(1 + sub_ans, result)
	
	if result == sys.maxsize:
		result = -1

	dp[n] = result
		
	return result

# testing out the recursion method first
# def minCoins(n, arr, dp=None):
#     if n == 0:
#         return 0
	
#     result = sys.maxsize
	
#     for i in arr:
#         if n - i >= 0:
#             sub_ans = minCoins(n - i, arr)
#             if sub_ans != -1:
#                 result = min(1 + sub_ans, result)
	
#     if result == sys.maxsize:
#         result = -1
		
#     return result



if __name__ == '__main__':
	n = int(input().strip())

	arr = list(map(int, input().split()))

	dp = [0]*(n+1)
	dp[0] = 0

	result = minCoins(n, arr, dp)
	
	print(result)
	print(dp)

