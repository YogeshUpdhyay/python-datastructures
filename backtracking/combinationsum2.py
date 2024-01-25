from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = 0

    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        paths = []
        if sum(nums) < target:
            return []
        
        if target == 0:
            return [[]]
        
        for i in range(len(nums)):
            path = []
            if nums[i] <= target:
                # this line will let only the unique paths through
                if i - 1 >= 0 and nums[i] == nums[i-1]:
                    continue
                
                subTarget = target - nums[i]
                # adding this element to the path
                path.append(nums[i])
                
                sub_paths = self.combinationSum2(nums[i+1:], subTarget)
                for sp in sub_paths:
                    paths.append(path + sp)
                    
        return paths
    
    def allPathsToFormTarget(self, nums, target):
        res = 0
        paths = []
        if sum(nums) < target:
            return 0, []
        
        if target == 0:
            return 1, [[]]
        
        for i in range(len(nums)):
            path = []
            if nums[i] <= target:
                subTarget = target - nums[i]
                # adding this element to the path
                path.append(nums[i])
                
                no_of_ways_to_find_subtarget, sub_paths = self.allPathsToFormTarget(nums[i+1:], subTarget)
                if no_of_ways_to_find_subtarget:
                    res += no_of_ways_to_find_subtarget
                    for i in range(no_of_ways_to_find_subtarget):
                        paths.append(path + sub_paths[i])
                    
        return res, paths
    
    def noOfWays(self, nums, target):
        res = 0
        
        if sum(nums) < target:
            return 0
        
        if target == 0:
            return 1
        
        for i in range(len(nums)):
            if nums[i] <= target:
                subTarget = target - nums[i]
                no_of_ways_to_find_subtarget = self.noOfWays(nums[i+1:], subTarget)
                
                res += no_of_ways_to_find_subtarget
        
        return res
        
tc = [
    ([10,1,2,7,6,1,5], 8)
]
for nums, target in tc:
    sol = Solution()
    
    # testing no Of Ways
    # print(sol.noOfWays(nums, target))
    
    # all paths to form target
    # print(sol.allPathsToFormTarget(nums, target))
    
    #just the paths
    nums.sort()
    print(sol.combinationSum2(nums, target))