#User function Template for python3

def merge(arr, l, m, r): 
    # code here
    left = arr[l:m]
    right = arr[m:r+1]
    nl = m-l
    nr = r-m+1
    
    i, j, k = 0, 0, l
    
    while(i < nl and j < nr):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while(i < nl):
        arr[k] = left[i]
        i += 1
        k += 1

    while(j < nr):
        arr[k] = right[j]
        j += 1
        k += 1
        
        
def mergeSort(arr, l, r):
    #code here
    n = r-l+1
    
    if n < 2:
        return
    
    m = int(n / 2) + l

    mergeSort(arr, l, m-1)
    mergeSort(arr, m, r)
    merge(arr, l, m, r)
        

if __name__ == "__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    mergeSort(arr, 0, n-1)
    print(*arr, sep=" ")