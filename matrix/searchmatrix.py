from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    from itertools import chain
    arr = list(chain.from_iterable(matrix))
    if target in arr:
        return True
    else:
        return False

if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split(" "))))
    target = int(input().strip())
    print(searchMatrix(arr, target))