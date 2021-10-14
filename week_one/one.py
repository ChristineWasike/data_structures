from week_one.functions import *
import time


# Question 1 - Time tracker
def max_value_time_tracker(number_of_list_items):
    # Setting the start time
    start_time = time.time()
    max_value(number_of_list_items)

    # Subtracting the start time from the send time to get the number of seconds it took to run the algorithm
    print("Time taken: " + str((time.time() - start_time)) + " seconds.")
    return time.time() - start_time


def lower_case_time_tracker(string):
    start_time = time.time()
    lower_case_func(string)
    print("Time taken: " + str((time.time() - start_time)) + " seconds.")
    return time.time() - start_time

def list_sort_time_tracker(number_of_list_items):
    start_time = time.time()
    list_sort(number_of_list_items)
    print("Time taken: " + str((time.time() - start_time)) + " seconds.")
    return time.time() - start_time


max_value_time_tracker(10)
lower_case_time_tracker("STRING")
list_sort_time_tracker(10)
