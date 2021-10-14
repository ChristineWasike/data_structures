a = ["a", "b", "c", "d", 1]
b = [1, 2, 3, 4, "d", "b"]
c = ["f", "animal", False, True, 2, "a", "c"]


def list_function(first_list, second_list, third_list):
    # Initializing an empty array that will contain all elements whether duplicate or not
    main_list = []

    # List of lists created here
    large_list = [first_list, second_list, third_list]

    # looping through each list and then appending each element within it to a list main_list
    for single_list in large_list:
        for element in single_list:
            main_list.append(element)

    # Removing the duplicates from the main list by creating a dictionary with the list items as keys
    # This automatically removes the duplicates
    # We then get the convert the dictionary back to a list
    final_list = list(dict.fromkeys(main_list))

    return final_list


f_list = ["a", "b", "c"]
s_list = ["d", "e", "f", "g"]
t_list = ["h", "i", "j", "k", "l"]
print(list_function(f_list, s_list, t_list))
