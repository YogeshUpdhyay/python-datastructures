from typing import List

def majorityElement(nums: List[int]) -> int:
    nums.sort()
    majorNum = -1
    maxCount=0
    count = 0
    currentNum = nums[0]
    for i in nums:
        if i == currentNum:
            count += 1 
        else:
            if count > maxCount:
                maxCount = count
                majorNum = currentNum
            count = 1
            currentNum = i
    if count > maxCount:
        majorNum = currentNum
    return majorNum

print(majorityElement([3,2,3]))