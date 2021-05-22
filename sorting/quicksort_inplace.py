# Also called as Lumoto Partitioning technique

def partition(arr, start, end):
    pivot = arr[end]
    p_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1
        
    arr[p_index], arr[end] = arr[end], arr[p_index]
    print(*arr, sep=" ")
    return p_index

def quicksort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quicksort(arr, start, p_index-1)
        quicksort(arr, p_index+1, end)
        # print(*arr, sep=" ")

if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().split(" ")))

    quicksort(arr, 0, n-1)