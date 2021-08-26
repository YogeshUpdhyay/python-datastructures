def removeDuplicates(nums) -> int:
    uniqueCount = len(nums)
    i = 1
    while i < uniqueCount:
        if nums[i] == nums[i-1]:
            del nums[i]
            nums.append("_")
            uniqueCount -= 1
        else:
            i += 1
    return uniqueCount

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))