def pivotIndex(nums):
    totalSum = sum(nums)
    currSum = 0
    for index, value in enumerate(nums):
        totalSum -= value
        if totalSum == currSum:
            return index
        currSum += value
    return -1

print(pivotIndex([1,7,3,6,5,6]))