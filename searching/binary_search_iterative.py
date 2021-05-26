def searchInSorted(arr, N, K):
    left = 0
    right = N-1

    while(left <= right):
        mid = int((left+right)/2)
        if arr[mid] == K:
            return 1
        elif K < arr[mid]:
            right = mid -1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().split(" ")))

    k = int(input().strip())

    print(searchInSorted(arr, n, k))