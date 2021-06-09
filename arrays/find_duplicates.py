from typing import List

# negative pointer approach 
# to be used when the array containe elements in range(1, n) only *****
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