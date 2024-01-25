# python program to find number of ways of partitioning it.
n = 3
s = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
	for j in range(n+1):
		if j > i:
			continue
		elif(i==j):
			s[i][j] = 1
		elif(i==0 or j==0):
			s[i][j]=0
		else:
			s[i][j] = j*s[i-1][j] + s[i-1][j-1]
ans = 0
for i in range(0,n+1):
	ans+=s[n][i]
print(ans)
