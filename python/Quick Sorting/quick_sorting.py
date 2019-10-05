def quick_sorting(input_array):
    cursor = len(input_array)
    while cursor > 1:
        pivot = input_array.pop()
        left, right = [], []
        for value in input_array:
            if value > pivot:
                left.append(value)
            else:
                right.append(value)
        return quick_sorting(right) + [pivot] + quick_sorting(left)

    return input_array


if __name__ == '__main__':
    user_input = int(input("Enter number of elements in your array: "))
    input_array = list(map(int, input("\nEnter the array elements separated by spaces: ").strip().split()))[:user_input]
    sorted_array = quick_sorting(input_array)
    print('Here is your sorted array: ' + ','.join(str(number) for number in sorted_array))
