class Solution:
    def backtrack(self, dp):
        return False
    
    def wordBreak(self, s: str, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        print(dp)
        
        result = []
        # backtracking the sentences from the array
        for i in range(len(dp)):
            if dp[i] is True:
                # two cases select it or dont select it 
                # by default we select it
                if self.backtrack(dp[i+1:]):
                    result.append()
        return dp[len(s)]   
        
        
    
sol = Solution()
print(sol.wordBreak(
    "catsanddog", 
    ["cat","cats","and","sand","dog"]
))