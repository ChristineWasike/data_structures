# Assumed that the sporting is in ascending order
def special_sort(dictionary):
    # A list of keys and values from the dictionary
    list_from_dict = [[key, value] for key, value in dictionary.items()]

    # Sorting the list created by the second item in each smaller list
    # If the values are the same then the sorting is done by the key
    sorted_list = sorted(list_from_dict, key=lambda x: (x[1], x[0]))

    # Casting the sorted list back to a dictionary
    sorted_dict = dict(sorted_list)

    return sorted_dict


a_dict = {6: 50, 4: 0, 8: 40, 3: 68, 0: 20}
print(special_sort(a_dict))
