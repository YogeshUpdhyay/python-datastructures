
def getMinDiff(arr, n, k):
    # code here

    v = [] # all possible variations
    taken = [0]*n # visted array to check if all the arrays are visited or not
    
    # finding all possible values and adding them to the v as [value, index]
    for i in range(n):
        if arr[i]-k >= 0:
            v.append([arr[i]-k,i])
        v.append([arr[i] + k,i])
        
    
    v.sort() # sorting all values
    
    elements_in_range = 0
    left = 0
    right = 0
    
    while elements_in_range < n and right < len(v) :
        
        # if all the indexes are present in the window or not
        if taken[v[right][1]] == 0 :
            elements_in_range+=1
        
        # number of variations in the array
        taken[v[right][1]]+=1

        right+=1
    
    
    ans = v[right - 1][0] - v[left][0] # declaring the answer
    
    while right < len(v) :

        # if the window loses all the indexes
        if(taken[v[left][1]] == 1) :
            elements_in_range-=1
        
        taken[v[left][1]]-=1
        left+=1
        
        # if the window no longer contains all indexes in it
        while elements_in_range < n and right < len(v) : 
            if taken[v[right][1]] == 0 :
                elements_in_range+=1
            
            taken[v[right][1]]+=1
            right+=1
        
        # if all elements are in the range then update the answer 
        if(elements_in_range == n) : 
            ans = min(ans, v[right - 1][0] - v[left][0])
        else :
            break
        
    
    return ans


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    k = int(input())
    min_diff = getMinDiff(arr, len(arr), k)
    print(min_diff)