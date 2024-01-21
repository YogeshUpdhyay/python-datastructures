
import sys
import heapq

class Solution:
    def minimumCost(self, nums, k: int, dist: int) -> int:
        # except the first element heapify all the rest element with their indexes
        h = []
        for i in range(1, len(nums)):
            heapq.heappush(h, (nums[i], i))
            
        # we need to get the first k element
        min_idx = sys.maxsize
        max_idx = -sys.maxsize
        partitions = []
        while k > 1:
            partition = heapq.heappop(h)
            min_idx = min(min_idx, partition[1])
            max_idx = max(max_idx, partition[0])
            partitions.append(partition)
            k -= 1
            
        while abs(min_idx - max_idx) > dist:
            partitions.pop()
            partition = heapq.heappop(h)
            min_idx = min(min_idx, partition[1])
            max_idx = max(max_idx, partition[0])
            partitions.append(partition)
        
        
        # once this loop is done we have the partiitons 
        # partitions.sort(key=lambda x: x[1])
        # while abs(partitions[0][1] - partitions[-1][1]) > dist:
        #     # remove the max value partition
        #     partitions.sort()
        #     partitions.pop()
        #     partition = heapq.heappop(h)
        #     partitions.append(partition)
        #     partitions.sort(key=lambda x: x[1])
            
        # calculate cost
        cost = nums[0]
        for i in partitions:
            cost += i[0]
             
        return cost
        
        
sol = Solution()
tc = [
    [[1,3,2,6,4,2], 3,3],
    [[10,1,2,2,2,1], 4, 3],
    [[10,8,18,9], 3,1],
    [[1,6,4,7,9,6,1], 4, 4]
]
for t in tc:
    print(sol.minimumCost(*t))