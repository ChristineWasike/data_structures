"""
Write a gcd(m,n) function which finds the greatest common divisor of positive integers m and n.
You can use the Euclidean Algorithm to help you.
"""


# This function in it's iterable form: Made use of a while loops
# Time complexity: O(n) and the Space complexity: O(1)
def calculate_gcd(larger_number, smaller_number):
    check = True
    result = 0

    while check:
        # In case the first argument is smaller than the second one, a swap is made
        # Assigns a variable to the difference between the two values
        difference = abs(larger_number - smaller_number)

        if difference == larger_number or difference == smaller_number:
            return "Cannot compute gcd of a pair of numbers when one of them is 0."

        # Checks that when the smaller number is smaller than the difference that the larger number is reassigned to the
        # the larger number variable
        if difference > smaller_number:
            larger_number = difference
        elif difference == 0:
            check = False
            result = larger_number
        elif difference < smaller_number:
            larger_number = smaller_number
            smaller_number = difference
        else:
            check = False
            result = difference
    return result


"""
Attempt at a recursive version of the problem
"""


def gcd(larger_number, smaller_number):
    result = 0
    # In case the first argument is smaller than the second one, a swap is made
    # Assigns a variable to the difference between the two values
    difference = abs(larger_number - smaller_number)

    # Checks that when the smaller number is smaller than the difference that the larger number is reassigned to the
    # the larger number variable

    if difference == smaller_number:
        result = difference
        return result
    if difference == larger_number or difference == smaller_number:
        return "Cannot compute gcd of a pair of numbers when one of them is 0."
    else:
        if difference > smaller_number:
            larger_number = difference

        elif difference < smaller_number:
            larger_number = smaller_number
            smaller_number = difference
        # else:
        #     result = difference
        return gcd(larger_number, smaller_number)


print(calculate_gcd(34, 0))
