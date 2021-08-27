
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# Input: nums = [1,1,1], k = 2
# Output: 2

# Solution

# 1. Create a map whose keys are sum values and the count of their appearance in the array as value 
# 2. iterate over the loop -> check if the currSum is equal to target if yes increment count by 1
# 3. If it is not equal to target subtract the target from the value and check if the diff is in the map or not 
# Note: On every iteration update the current sum and update the sum map

def subarraySum(nums, k: int) -> int:
    dic = {}
    ans = 0
    sums = 0
    for i in nums:
        if sums + i == k:
            ans += 1
        if ((sums + i) - k) in dic:
            ans += dic[(sums + i) - k]
        sums += i
        dic[sums] = dic.get(sums,0) + 1

    return ans

print(subarraySum([1,-1,0], 0))