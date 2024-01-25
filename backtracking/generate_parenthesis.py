class Solution:

    def generateParenthesis(self, n):
        dp = [[-1] * (2 * n + 1) for _ in range(n)]
        
        def generate_ways(nopen, nclose):
            if nopen == nclose == n:
                res.append("".join(stack))
        for 


sol = Solution()
print(sol.genereateParenthesis(3))

