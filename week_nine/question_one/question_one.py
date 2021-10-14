"""
Write a function that inputs a list of integers and returns True if it is a min heap
(parents are always less than children) and False if not.
"""


def min_heap_check(integer_list, index, length):
    # Check for when it's a leaf node
    if index > int((length - 2) / 2):
        return True

    # If the internal node is less than its children, and equal
    # then its recursively true from the children
    if (integer_list[index] <= integer_list[2 * index + 1] and
            integer_list[index] <= integer_list[2 * index + 2] and
            min_heap_check(integer_list, 2 * index + 1, length) and
            min_heap_check(integer_list, 2 * index + 2, length)):
        return True
    return False


test_array = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
another_test = [12, 11, 13, 5, 6, 7]
one_more = [5]
print(min_heap_check(test_array, 0, len(test_array) - 1))
