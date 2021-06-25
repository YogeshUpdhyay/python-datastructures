def word_wrap(nums, k):
    res = 0
    capacity = k
    for i in nums:
        if capacity > i:
            if capacity < k:
                capacity -= i
                capacity -= 1
            else:
                capacity -= i
        else:
            res += capacity
            capacity = k - i
    return res

if __name__ == '__main__':
    nums = list(map(int, input().strip().split(" ")))
    k = int(input().strip())
    print(word_wrap(nums, k))