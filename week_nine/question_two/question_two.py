def min_heap_swap(integer_list, index, number):
    left = 2 * index
    right = 2 * index + 1
    smallest = 0

    if left <= number and integer_list[left] < integer_list[index]:
        smallest = left
        print("Hey it's within the range.")
        print("Let's take a closer look: \nleft: " + str(left) + " \nsmallest: " + str(smallest))

    else:
        smallest = index
        print("Uhm, there's something not quite right here, is it outside the range?")
        print("Let's take a closer look: \n left: " + str(left) + " \n smallest: " + str(smallest))
    if right <= number and integer_list[right] < integer_list[smallest]:
        smallest = right
    if smallest != index:
        integer_list[index], integer_list[smallest] = integer_list[smallest], integer_list[index]
        min_heap_swap(integer_list, smallest, number)
    return integer_list
    # index = 0
    # parent = index // 2
    # integer_list.insert(0, 0)
    # print(integer_list)
    # if index <= 1:
    #     return
    # elif integer_list[index] > integer_list[parent]:
    #     dummy_value = integer_list[index]
    #     integer_list[index] = integer_list[parent]
    #     integer_list[parent] = dummy_value
    #
    # return integer_list


my_array = [4, 5, 1, 6, 7, 3, 2]
print(min_heap_swap(my_array, 1, len(my_array)))
# print(len(my_array))
