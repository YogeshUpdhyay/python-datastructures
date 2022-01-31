import sys


def findEarliestMonth(stockPrice):
    minMonth = sys.maxsize
    minNet = sys.maxsize
    n = len(stockPrice)
    i = 0
    lsum = 0
    rsum = sum(stockPrice)

    while i < n-1:
        lsum += stockPrice[i]
        rsum -= stockPrice[i]
        net = abs((lsum//(i+1)) - (rsum//(n-i-1)))
        if net < minNet:
            minMonth = i+1
            minNet = net
        i += 1

    return minMonth


print(findEarliestMonth(list(map(int, input().split()))))
