# two pointer method

def sort012(arr, n):
    # in case when sorting is not allowed look for swapping methods 
    low = 0
    mid = 0
    high = n-1

    while mid <= high:
        if arr[mid] == 0:
            temp = arr[low]
            arr[low] = arr[mid]
            arr[mid] = temp
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            temp = arr[high]
            arr[high] = arr[mid]
            arr[mid] = temp
            high -= 1
    return arr


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    arr = sort012(arr, len(arr))
    print(arr)