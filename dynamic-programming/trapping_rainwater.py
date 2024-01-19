class Solution:
    def trap(self, height):
        stack = []
        result = 0
        
        for i in height:
            if len(stack) == 0:
                stack.append(i)
            else:    
                if stack[0] <= i:
                    curr_max_height = stack[0]
                    while len(stack) != 0:
                        result += (curr_max_height - stack.pop()) * 1
                    stack.append(i)
                else:
                    stack.append(i)
        
        stack = []            
        for i in height[::-1]:
            if len(stack) == 0:
                stack.append(i)
            else:    
                if stack[0] < i:
                    curr_max_height = stack[0]
                    while len(stack) != 0:
                        result += (curr_max_height - stack.pop()) * 1
                    stack.append(i)
                else:
                    stack.append(i)
        
        return result
    
    
sol = Solution()
sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])