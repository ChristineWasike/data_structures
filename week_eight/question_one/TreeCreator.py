"""
Write a function that inputs a list of lists and returns if it can form a tree
with the root as the first element of the list and each other element a subtree
"""


def tree_checker(list_of_lists):
    if type(list_of_lists) is not list:
        return "This is not tree because: it is not a list"

    # Empty lists in this case do not constitute trees
    elif len(list_of_lists) is 0:
        return "This is not a tree because: it is empty"

    # For my check, the list of lists has to contain only integer data types
    elif type(list_of_lists[0]) is not int:
        return "This is not a tree because: first element not an integer"

    else:
        # This checks that all subtrees returned are all tree and if one or more happen not to be the case then the
        # entire list of lists fails to qualify as a tree
        all([tree_checker(x) for x in list_of_lists[1:]])
        return "This is a tree"


sample_list = [5, 6]
print(tree_checker(sample_list))
