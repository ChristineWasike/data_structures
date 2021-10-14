import sys
import traceback

from week_three.question_one.ArrayClass import *


def question_one():
    new_array = ArrayClass([1, 2, 3, 4])

    print("Items in: " + str(new_array))
    print("Size of array: " + str(new_array.array_length()))
    print("Second item in array: " + str(new_array.get_element(1)))
    print("Change value of third element: " + str(new_array.set_element(7, 1)))
    print(str(new_array.set_element(16, 3)))
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(traceback.print_tb(exc_traceback, limit=1, file=sys.exc_info()))

    test_array = ArrayClass([3, 5, 7, 9, 13])
    print(str(test_array.set_element(18, 5)))


question_one()
