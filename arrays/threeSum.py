from typing import List

# Three Sum 

# Ex input = [-1,0,1,2,-1,-4] -> nums
# output = [[-1,-1,2],[-1,0,1]]

# Conditions are
# nums[i] != nums[j] != nums[k]
# such that nums[i] + nums[j] + nums[k] == 0


# Solution 

# 1. Sort the array so that 2 pointer approach can be applied
# [-4,-1,-1,0,1,2]

# 2. Loop over the elements select the ith element and find two other elements between the i+1 th index 
# and the n-1 the index where n is the length of nums

# To do this run a while loop with two pointer approach where the two pointers are 
# s = i+1 -> start and e = n-1 -> end 

# Find nums where nums[e]+nums[s]=(-1*nums[i])
# This will find the elements -> append to the answers list when this happens

# Note there can be more than one occurence of a particular number in the nums list 
# to deal this we increment start and decrement end till we find the numbers that are not equal
# same for the ith element as well

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    n = len(nums)
    i = 0
    while i < n:
        t = -1*nums[i]
        s = i+1
        e = n-1

        while s < e:
            if nums[s] + nums[e] == -1*nums[i]:
                ans.append([nums[i], nums[s], nums[e]])
                while s<e and nums[s] == nums[s+1]:
                    s+=1
                while s<e and nums[e] == nums[e-1]:
                    e-=1
                s+=1
                e-=1
            elif nums[s] + nums[e] > -1*nums[i]:
                e-=1
            else:
                s+=1
        
        while i+1<n and nums[i] == nums[i+1]:
            i+=1

        i+=1
    
    return ans



print(threeSum([-1,0,1,2,-1,-4]))