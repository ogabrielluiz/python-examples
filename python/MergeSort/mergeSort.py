def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            elif right[j] < left[i]:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

def print_list(list):
    for i in range(len(list)):
        print(list[i])

if __name__ == '__main__':
    list = [10, 15, 20, 1, 5, 3]
    print("Given array is:",list)
    merge_sort(list)
    print("Sorted array is:",list)
