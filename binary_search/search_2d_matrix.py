class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
    
        def find_correct_row(matrix):
            # first we will use binary search to find the correct row by considering
            # the first element of the rows
            top, bottom = 0, len(matrix) - 1
            while top <= bottom:
                mid = (top + bottom) // 2
                
                if matrix[mid][0] <= target <= matrix[mid][len(matrix[0])-1]:
                    # found the correct row which is the mid one
                    return mid
                elif matrix[mid][0] > target:
                    bottom = mid - 1
                else:
                    top = mid + 1
                
            return -1

        row = find_correct_row(matrix)
        if row == -1:
            return False
        
        # once we have the mid here search in that row
        row = matrix[row]
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

sol = Solution()
sol.searchMatrix([[1]], 3)
