def mergeIntervals(arr):
    arr.sort()
    ans = []
    temp = arr[0]

    for i in range(1, len(arr)):
        if arr[i][0] <= temp[1]:
            temp[1] = temp[1] if temp[1] > arr[i][1] else arr[i][1]
        else:
            ans.append(temp)
            temp = arr[i]
    ans.append(temp)
    return ans

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split(" "))))
    print(mergeIntervals(arr))