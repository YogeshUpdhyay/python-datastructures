
def merge(arr1, arr2):
    i = 0
    while i < len(arr1):
        if arr1[i] <= arr2[0]:
            pass
        else:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            arr2.sort()
        i += 1
    return arr1 , arr2


if __name__ == '__main__':
    arr1 = list(map(int, input().split(" ")))
    arr2 = list(map(int, input().split(" ")))
    arr1, arr2 = merge(arr1, arr2)
    print(*arr1, sep=" ")
    print(*arr2, sep=" ")