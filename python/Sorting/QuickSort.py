def partition(arr,low,high):
	i = low - 1			#index of the smaller element
	pivot = arr[high]	#pivot

	for j in range(low,high):
		if arr[j] < pivot:
			i += 1
			arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[high] = arr[high],arr[i+1]
	return i + 1

def quicksort(arr,low,high):
	if low < high:
		pi = partition(arr,low,high)

		quicksort(arr,low,pi-1)
		quicksort(arr,pi+1,high)

def main():
	n = list(map(int,input().split()))
	for i in quicksort(n,0,len(n)-1):
		print(i,end=' ')

if __name__ == '__main__':
	main()