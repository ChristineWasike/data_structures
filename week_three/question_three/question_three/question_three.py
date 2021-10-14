from week_three.question_two.DynamicArrayClass import *


def contains_element(array, val):
    flag = False
    for element in range(0, array.array_length()):
        if array.get_element(element) == val:
            flag = True
    return flag


# Reversing an array
def reverse_array(array):
    # Setting index to the last index in the array
    index = array.array_length() - 1
    reversed_array = []
    new_array = DynamicArray(reversed_array)

    # Looping through the array until the first element
    while index >= 0:
        reversed_array.append(array.get_element(index))
        index -= 1
    return new_array


def insert_element(array, val, index):
    array.set_element(val, index)
    return array


my_array = DynamicArray([1, 2, 3, 4])
# print(reverse_array(my_array))
# print(contains_element(my_array, 4))
print(insert_element(my_array, 8, 3))
