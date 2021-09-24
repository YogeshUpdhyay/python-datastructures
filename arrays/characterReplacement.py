def characterReplacement( s: str, k: int) -> int:
    maxSubstr = 0
    n = len(s)
    for i in range(n):
        anchor = s[i]
        changes = 0
        j = i+1
        while j < n and changes < k:
            if s[j] != anchor:
                changes += 1
            j+=1
        maxSubstr = max(maxSubstr, j - i)
    return maxSubstr

print(characterReplacement("AABABBA", 1))