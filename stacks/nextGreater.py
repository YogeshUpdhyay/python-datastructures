def nextGreaterElement(nums1, nums2):
    ansMap = {}
    mstack = []
    for i in nums2:
        if len(mstack) == 0:
            mstack.append(i)
            continue
        
        if mstack[-1] <= i:
            while len(mstack) != 0 and mstack[-1] <= i:
                ansMap[mstack[-1]] = i
                mstack.pop()
            mstack.append(i)
        else:
            mstack.append(i)
    
    return [ansMap.get(x, -1) for x in nums1 ]

print(*nextGreaterElement([4,1,2], [1,3,4,2]), sep=" ")