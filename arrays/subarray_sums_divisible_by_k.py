class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        res = 0
        prefixRemainders = {0: 1}
        currSum = 0
        for n in nums:
            currSum += n
            remainder = currSum % k                
            res += prefixRemainders.get(remainder, 0)

            # add the current remainder to the prefix remainders
            prefixRemainders[remainder] = 1 + prefixRemainders.get(remainder, 0)

        return res
            
            
sol = Solution()
print(sol.subarraysDivByK([5], 9))