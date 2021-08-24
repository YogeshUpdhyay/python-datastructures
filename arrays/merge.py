def merge(nums1, m, nums2, n):
    if n == 0:
        return nums1
    i, j = 0, 0
    while i < m:
        if nums1[i] > nums2[j]:
            nums1[i], nums2[j] = nums2[j], nums1[i]
            nums2.sort()
        i += 1
    while i < m+n and j < n:
        nums1[i] = nums2[j]
        i += 1
        j += 1
    return nums1
print(*merge([1], 1, [], 0), sep=" ")