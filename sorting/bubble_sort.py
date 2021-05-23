def bubbleSort(n , arr):
	for i in range(n):
		for j in range(n-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == '__main__':
	n = int(input().strip())

	arr = list(map(int, input().split(" ")))

	bubbleSort(n, arr)

	print(*arr, sep=" ")