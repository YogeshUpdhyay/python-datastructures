
def max_score(numbers, N):

    def gcd(a, b):
        # Everything divides 0
        if (b == 0):
            return a
        return gcd(b, a % b)

    def lcm(a, b):
        return (a / gcd(a, b)) * b

    gcd_a = numbers[0][0]
    gcd_b = numbers[0][1]
    for i in range(N):
        gcd_a = gcd(gcd_a, numbers[i][0])
        gcd_b = gcd(gcd_b, numbers[i][1])

    return int(lcm(gcd_a, gcd_b))


print(max_score([[2, 10], [5, 15]], 2))
