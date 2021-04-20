# two pointer method
def getMinDiff(arr, n, k):
    # code here
    if (n == 1):
        return 0

    arr.sort()

    ans = arr[n-1] - arr[0]

    small = arr[0] + k
    big = arr[n-1] - k

    if (small > big):
        small, big = big, small
 
    # Traverse middle elements
    for i in range(1, n-1):
     
        subtract = arr[i] - k
        add = arr[i] + k
 
        # If both subtraction and addition
        # do not change diff
        if (subtract >= small or add <= big):
            continue
 
        # Either subtraction causes a smaller
        # number or addition causes a greater
        # number. Update small or big using
        # greedy approach (If big - subtract
        # causes smaller diff, update small
        # Else update big)
        if (big - subtract <= add - small):
            small = subtract
        else:
            big = add
 
    return min(ans, big - small)

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    k = int(input())
    min_diff = getMinDiff(arr, len(arr), k)
    print(min_diff)