import random


def merge(arr1, arr2):
    arr3 = []
    i = 0
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[i] > arr2[i]:
            arr3.append(arr2[i])
            arr2.remove(arr2[i])
        else:
            arr3.append(arr1[i])
            arr1.remove(arr1[i])

    while len(arr1) != 0:
        arr3.append(arr1[i])
        arr1.remove(arr1[i])

    while len(arr2) != 0:
        arr3.append(arr2[i])
        arr2.remove(arr2[i])

    return arr3


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    arr1 = arr[:middle]
    arr2 = arr[middle:]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)



if __name__ == '__main__':
    random_array = [94, 97, 77, 62, 8, 79, 34, 91]
    print(merge_sort(random_array))
