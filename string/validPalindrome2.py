def validPalindrome(s):
    l, r = 0, len(s)-1

    while l <= r:
        if s[l] != s[r]:
            return isPalindrome(s, l+1, r) or isPalindrome(s,l,r-1)
        l+=1
        r-=1

def isPalindrome(s, l, r):
    while l <= r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

print(validPalindrome("abcbea"))