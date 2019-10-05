def bubble(arr):
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				swapped = True
		
		if swapped == False:
			break

	return arr

def main():
	n = list(map(int,input().split()))
	for i in bubble(n):
		print(i,end=' ')

if __name__ == '__main__':
	main()