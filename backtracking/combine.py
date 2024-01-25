class Solution:
    def combine(self, n: int, k: int):
        paths = []
        nums = list(range(1, n+1))

        def dfs(i, path):
            if len(path) == k:
                paths.append(path.copy())
                return 

            for j in range(i, n):
                path.append(nums[j])
                dfs(j  + 1, path)
                path.pop()
            

        dfs(0, [])

        return paths

sol = Solution()
print(sol.combine(4, 2))