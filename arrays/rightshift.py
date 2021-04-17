def rightshift(arr, n):
    last = arr[n-1]
    i = n - 1
    while i > 0:
        arr[i] = arr[i-1]
        i -= 1
    arr[0] = last
    return arr

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    arr = rightshift(arr, len(arr))
    print(arr)