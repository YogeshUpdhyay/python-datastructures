def searchInSorted(arr, n, k, left, right):

    if right < left:
        print(False)
        return

    mid = int((left + right)/2)

    if arr[mid] == k:
        print(True)
        return
    elif k < arr[mid]:
        searchInSorted(arr, n, k, left, mid-1)
    else:
        searchInSorted(arr, n, k, mid+1, right)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().split(" ")))

    k = int(input().strip())

    searchInSorted(arr, n, k,  0, n-1)