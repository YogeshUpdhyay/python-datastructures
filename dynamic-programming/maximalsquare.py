class Solution:
    def maximalSquare(self, matrix) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = [[-1] * cols for _ in range(rows)]

        # comparing up and left the first row and col will be the same
        dp[0] = [int(i) for i in matrix[0]]
        for row in range(1, rows):
            dp[row][0] = int(matrix[row][0])

        # filling up all the values of the dp matrix now
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = 1 + min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) if all([dp[i-1][j], dp[i][j-1], dp[i-1][j-1], int(matrix[i][j])]) else int(matrix[i][j])
        
        # parsing through the dp matrix to get the max value
        result = max([max(i) for i in dp])

        return result*result
    
sol = Solution()
sol.maximalSquare([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]])