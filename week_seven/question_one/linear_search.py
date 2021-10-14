def linear_search(array, item):
    for array_item in array:
        if array_item == item:
            return True
    return False


arr = [1, 2, 3, 4, 5]
it = 4

print(linear_search(arr, it))
