def rowWithMax1s(arr, n, m):
    # code here
    max = 0
    row = -1
    for i in range(n):
        count = arr[i].count(1)
        if  count > max:
            max = count
            row = i
    return row

if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split(" "))))
    print(rowWithMax1s(arr, n, m))