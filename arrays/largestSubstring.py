def largestSubstring(s, k):
    n = len(s)
    
    if(n == 0 or n < k):
        return 0 
    if(k <= 1):
        return n
    
    counts = {}
    for x in s:
        counts[x] = counts.get(x,0) + 1
    
    l = 0
    while(l < n and counts[s[l]] >= k):
        l+=1
        
    if(l>=n-1):
        return l
    
    ls1 = largestSubstring(s[:l],k)
    while(l < n and counts[s[l]] <k):
        l+=1
    ls2 = largestSubstring(s[l:], k) if(l < n) else 0
    
    return max(ls1, ls2)

print(largestSubstring("aaabb", 3))