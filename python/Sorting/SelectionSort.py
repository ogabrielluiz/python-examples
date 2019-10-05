def selection(arr):
	n = len(arr)
	for i in range(n):
		minindex = i
		for j in range(i+1,n):
			if arr[j] < arr[minindex]:
				minindex = j
		arr[i],arr[minindex] = arr[minindex],arr[i]

	return arr

def main():
	n = list(map(int,input().split()))
	for i in selection(n):
		print(i,end=' ')

if __name__ == '__main__':
	main()