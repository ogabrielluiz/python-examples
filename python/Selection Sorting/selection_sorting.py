def selection_sorting(input_array):
    for cursor in range(len(input_array)):
        position = cursor + 1
        while position < len(input_array):
            if input_array[cursor] > input_array[position]:
                input_array[cursor], input_array[position] = input_array[position], input_array[cursor]
            position += 1

    return input_array


if __name__ == '__main__':
    user_input = int(input("Enter number of elements in your array: "))
    input_array = list(map(int, input("\nEnter the array elements separated by spaces: ").strip().split()))[:user_input]
    sorted_array = selection_sorting(input_array)
    print('Here is your sorted array: ' + ','.join(str(number) for number in sorted_array))
