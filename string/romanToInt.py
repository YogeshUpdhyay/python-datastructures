def romanToInt(s):
    rtn = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    i = len(s)-2
    val = rtn[s[-1]]
    while i >= 0:
        if rtn[s[i]] < rtn[s[i+1]]:
            val -= rtn[s[i]]
        else:
            val += rtn[s[i]]
            
        i-=1
    return val


print(romanToInt("XIX"))