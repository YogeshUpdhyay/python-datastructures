
def binomial_coefficient(n, k):

    C = [-1]*(n+1)
    C[0] = 1

    for i in range(1,n+1):
        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j-1]
            j -= 1
    return C[k]

if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    print(binomial_coefficient(n, k))