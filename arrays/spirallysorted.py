def isSpirallySorted(arr, n):
    start = 0
    end = n-1
    while start < end:
        if arr[start] > arr[end]:
            return False

        start += 1

        if arr[end] > arr[start]:
            return False

        end -= 1
    return True


# Driver Code
if __name__ ==  "__main__" :
    arr = [ 1, 10, 14, 20, 18, 12, 5 ];
    N = len(arr);
 
    # Function Call
    if (isSpirallySorted(arr, N)) :
        print("YES");
    else :
        print("NO");