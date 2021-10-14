def bubble_sort(array):
    for item_index in range(len(array)):
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                swapper = array[index]
                array[index] = array[index + 1]
                array[index + 1] = swapper
    return array


print(bubble_sort([9, 4, 10, 4, 7, 5, 9]))
