def reverse(x):
    rev = 0
    num = abs(x)
    while num/10 != 0:
        rev = rev * 10 + (num%10)
        num //= 10
    return rev if x > 0 else (rev*-1)

print(reverse(-123))