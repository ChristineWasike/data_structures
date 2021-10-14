"""
Write a fibonacci(n) function that finds the nth Fibonacci Number
"""


def fibonacci(number_position):
    # First two terms
    number_1, number_2 = 0, 1
    count = 0

    if number_position <= 0:
        print("Please enter a positive number")
    elif number_position == 1:
        print("The fibonacci number for number " + str(number_position) + " is: " + str(number_1))
    else:
        while count < number_position:
            print("The fibonacci number for number " + str(number_position) + " is: " + str(number_1))
            nth_position = number_1 + number_2

            # update values
            number_1 = number_2
            number_2 = nth_position
            count += 1


print(fibonacci(4))
