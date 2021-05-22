def partition(arr, start, end):
    p = arr[start]
    left = []
    right = [] 
    
    for i in range(start, end+1):
        if arr[i] > p:
            right.append(arr[i])
        
        if arr[i] < p:
            left.append(arr[i])

    arr[start:end+1] = left + [p] + right   
    # print(*arr[start:end+1], sep=" ")  
    return start+len(left)

def quick_sort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quick_sort(arr, start, p_index-1)
        quick_sort(arr, p_index+1, end)
        print(*arr[start:end+1], sep=" ")

if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().split(" ")))

    quick_sort(arr, 0, n-1)