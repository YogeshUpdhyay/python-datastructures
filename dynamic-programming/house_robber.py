class Solution:
    def rob(self, nums) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i - 2 >= 0:
                dp[i] = max(nums[i] + dp[i - 2], dp[i-1])
            else:
                dp[i] = max(nums[i], nums[i-1])

        return dp[-1]
    
sol = Solution()
print(sol.rob([1,2,3,1]))
