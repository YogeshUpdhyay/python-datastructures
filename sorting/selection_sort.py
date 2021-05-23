

def selectionSort(arr):
    #code here
    # Traverse through all array elements
    for i in range(len(arr)):
        
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        


n = int(input())
arr = list(map(int, input().strip().split()))
selectionSort(arr)
for i in range(n):
    print(arr[i],end=" ")
print()