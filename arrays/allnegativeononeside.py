# two pointer method
def sortnegative(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:

            left+=1
        elif arr[left] > 0 and arr[right] < 0:

            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] > 0:

            right -= 1
        else:
            
            left += 1
            right -= 1
    
    return arr

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    arr = sortnegative(arr)
    print(arr)