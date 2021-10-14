import random


# PLEASE NOT THAT THESE FUNCTIONS ARE RUNNING IN THE OTHER NUMBERED FILES

# Question 3
def integer_list_fun(number_of_list_items):
    # Empty integer list declared
    number_list = []

    # A loop for typing in the different digits based on how many the user wants
    for number in range(number_of_list_items):
        digit = random.randint(0, 100)
        number_list.append(digit)

    print(number_list)
    return number_list


# Question 3a.
# Find the maximum value in a list
def max_value(number_of_list_items):
    # Created a variable and assigned it the value of the largest digit in the list
    max_number = max(integer_list_fun(number_of_list_items))

    # Printing the largest digit
    print("The largest number in the list is: " + str(max_number))
    return max_number


# Question 3b.
def lower_case_func(string):
    lower_string = string.lower()
    print("Here's your new and improved sentence: \n" + lower_string)


# Question 3c.
def list_sort(number_of_list_items):
    sorted_list = sorted(integer_list_fun(number_of_list_items))

    print("Here is the sorted list of integers: \n" + str(sorted_list))
    return sorted_list
