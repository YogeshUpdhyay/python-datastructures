def characterReplacement(s: str, k: int) -> int:
    chars = {}
    left, maxf, output = 0, 0, 0
    for right in range(len(s)):
        char = s[right]
        
        chars[char] = 1 + (chars.get(char, 0))
        maxf = max(maxf, chars[char])
        
        while (right-left+1) - maxf > k:
            chars[s[left]] -= 1
            left += 1
            
        output = max(output, right-left+1)
    return output


print(characterReplacement("AABABBA", 1))