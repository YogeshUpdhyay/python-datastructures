def sortedMatrix(N,Mat):
    #code here
    from itertools import chain
    arr = list(chain.from_iterable(Mat))
    arr.sort()
    ans = [ arr[i:i+N] for i in range(0,N*N,N)]
    return ans

if __name__ == '__main__':
    N = int(input().strip())
    Mat = []
    for i in range(N):
        Mat.append(list(map(int, input().strip().split(" "))))
    ans = sortedMatrix(N, Mat)
    for i in ans:
        print(*i, sep=" ")