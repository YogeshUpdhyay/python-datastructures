def minJump(arr, n):
    if arr[0] == 0:
        return 0

    jump = 0

    pos = arr[0]
    while pos < n:
        if arr[pos] == 0:
            return 0
        pos += arr[pos]
        jump += 1
    
    return jump  

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    print(minJump(arr, len(arr)))