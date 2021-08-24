def moveZeroes(nums):
    count, i = 0, 0
    while i < len(nums) - count:
        if nums[i] == 0:
            count += 1
            j = i
            while j < len(nums)-1:
                nums[j] = nums[j+1]
                j += 1
            nums[j] = 0
        else:
            i += 1
    
    

nums = [0,1,0,3,12]
moveZeroes(nums)
print(*nums, sep=" ")