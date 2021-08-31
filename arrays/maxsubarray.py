# to find the max sum for a contiguos subarray of the give array

# def maxSubArraySum(a,size):
      
#     max_so_far = 0
#     max_ending_here = 0
      
#     for i in range(0, size):
#         max_ending_here = max_ending_here + a[i]
#         if (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
 
#         if max_ending_here < 0:
#             max_ending_here = 0  
#     return max_so_far

def maxSubArraySum(a, size):
    current_max = global_max = [0]
    for i in range(1,size):
        current_max = max([i], [i]+current_max)
        if current_max > global_max:
            global_max = current_max
    
    return global_max

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    max_sum = maxSubArraySum(arr, len(arr))
    print(max_sum)