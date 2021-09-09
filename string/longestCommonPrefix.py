def longestCommonPrefix(strs):
    n = len(sorted(strs, key=len)[0])
    prefix = ""
    for i in range(n):
        temp = strs[0][i]
        for j in strs:
            if temp != j[i]:
                return prefix
        prefix += temp
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))