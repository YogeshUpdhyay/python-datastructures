from typing import List

# negative pointer approach
def findDuplicate(nums: List[int]) -> int:
    for n in nums:
        m=abs(n)
        if nums[m-1]<0:
            return m
        else:
            nums[m-1]*=-1

if __name__ == '__main__':
    nums = list(map(int, input().split(" ")))
    print(findDuplicate(nums))