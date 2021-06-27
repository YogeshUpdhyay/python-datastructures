def findFirstLastElement(n, arr):
    first = -1
    last = -1

    for index, value in enumerate(arr):
        if n == value:
            if first == -1:
                first = index
            else:
                last = index
    return first, last

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(" ")))
    first, last = findFirstLastElement(n, arr)
    print("{} {}".format(first, last))