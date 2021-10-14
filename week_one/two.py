import time
import random
import memory_profiler
from memory_profiler import profile
from week_one.functions import *


# 2 - Tracking the space used by an algorithm.

@profile
def array_generator_memory(number_of_list_items):
    integer_list_fun(number_of_list_items)


@profile
def max_value_memory(number_of_list_items):
    # Created a variable and assigned it the value of the largest digit in the list
    max_number = max(integer_list_fun(number_of_list_items))

    # Printing the largest digit
    print("The largest number in the list is: " + str(max_number))


@profile
def lower_case_memory(string):
    lower_case_func(string)


@profile
def sort_list_memory(number_of_list_items):
    list_sort(number_of_list_items)


max_value_memory(30)
lower_case_memory("STRING")
sort_list_memory(5)
