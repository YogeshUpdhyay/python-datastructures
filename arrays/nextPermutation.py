
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

# Input: nums = [1,2,3]
# Output: [1,3,2]

# Solution:
# 1. Traverse the array from the ned until a elment nusm[i] < nums[i+1] -> this will be the breakpoint the array.
# 2. Then traverse aagain from the end till the ith position found earlier such that a[j] > a[i] -> j will represent
# the index of the number which when swapped with the breakpoint will provide the next permutation. 
# 3. Swap i and j th poisition elements 
# 4. Reverse the array ahead of the ith position in scending order

def nextPermutation(nums):
    n = len(nums)
        
    i = n-2
    
    while i>= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    if i >= 0:
        j = n-1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    nums[i+1:] = sorted(nums[i+1:])

nums = [1,1,5]
nextPermutation(nums)
print(*nums, sep=" ")