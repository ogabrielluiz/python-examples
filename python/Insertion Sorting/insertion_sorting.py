def insertion_sorting(input_array):
    for i in range(len(input_array)):
        value, position = input_array[i], i
        while position > 0 and input_array[position-1] > value:
            input_array[position] = input_array[position - 1]
            position = position - 1
        input_array[position] = value

    return input_array


if __name__ == '__main__':
    user_input = int(input("Enter number of elements in your array: "))
    input_array = list(map(int, input("\nEnter the array elements separated by spaces: ").strip().split()))[:user_input]
    sorted_array = insertion_sorting(input_array)
    print('Here is your sorted array: ' + ','.join(str(number) for number in sorted_array))
