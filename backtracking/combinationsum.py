from typing  import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        i = 0
        candidates.sort()
        n = len(candidates)
        result = []
        
        while i < n:
            if target - candidates[i] == 0:
                result.append([candidates[i]])
            elif target - candidates[i] >= 0:
                # target not found selecting this value
                ans = self.combinationSum(candidates, target - candidates[i])
                if len(ans) > 0:
                    for a in ans:
                        result.append([candidates[i]] + a)
            else:
                return result
            i += 1
            
        return result


s = Solution()
print(s.combinationSum([2,3,6,7], 7))