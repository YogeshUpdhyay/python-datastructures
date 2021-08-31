def maxArea(height):
    maxArea = 0
    l = 0
    r = len(height)-1
    while (l < r):
        maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
        if (height[l] < height[r]):
            l+=1
        else:
            r-=1
    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))