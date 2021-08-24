def twosum(nums, target):
    pairs = []
    for index, value in enumerate(nums):
        pairs.append((value, index))
    pairs.sort()

    left, right = 0, len(nums)-1

    while(left < right):
        if pairs[right][0] > target - pairs[left][0]:
            right -= 1
        elif pairs[right][0] < target - pairs[left][0]:
            left += 1
        else:
            return [pairs[left][1], pairs[right][1]]

print(*twosum([3,2,3], 6), sep=" ")