
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Solution 

# Create a prodLeft and prodRight pointer which indicates the left and right produts 
# for the curent value of i -> position of the iterator

# Loop once over the nums and updated left and right product or a particular value in the ans by multipling it 
# to the value present there hence in one loop the same index will be multiplied twice once with the left and once with right 
# thus updating the answers

def productExceptSelf(nums):
    n = len(nums)
    ans = [1]*n
    prodLeft = 1
    prodRight = 1

    for i in range(n):
        ans[i]*=prodLeft
        prodLeft*=nums[i]

        j = n-i-1
        ans[j]*=prodRight
        prodRight*=nums[j]
   
    return ans

print(*productExceptSelf([1,2,3,4]))