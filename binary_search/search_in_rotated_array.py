class Solution:
    def search(self, nums , target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
                    
            if nums[mid] < nums[right]:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return -1
            
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))   