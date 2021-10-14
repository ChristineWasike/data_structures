import numpy as np

"""
Write a det(A) function that takes an nxn matrix A (can be a list of lists, numpy array, pandas data frame etc
you chose) and finds the determinant.
"""

"""
This function takes in an a square array that is of size nxn. The function then checks whether the matrix is 2x2.
It's important since 2x2 is the base case of the recursion. In the event that the matrix is a 2x2, the determinant 
is easily calculated. This is how: for matrixA = [[a, b], [c, d]] (assuming that the lists within the bigger list are 
the columns of the matrix) then detA = ad - bc. If the matrix is greater than 2x2 then we need to create smaller 
2x2 matrices that we will individually calculate their determinants. 
"""


def calculate_determinant(array):
    number_of_columns = list(range(0, len(array)))
    final_determinant = 0
    if len(number_of_columns) == 2:
        return array[0][0] * array[1][1] - array[0][1] * array[1][0]

    # create a mini array to store smaller arrays

    for number in number_of_columns:
        smaller_array = []
        for number_a in number_of_columns:
            if number == number_a:
                pass
            else:
                smaller_array.append(array[number_a][1:])

        young_determinant = array[number][0] * calculate_determinant(smaller_array)
        if number % 2 == 0:
            final_determinant += young_determinant
        else:
            final_determinant -= young_determinant
        return final_determinant


test_matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(round(np.linalg.det(test_matrix_a)))
print(calculate_determinant(test_matrix_a))

another_matrix = [[5, 4], [2, 4]]
print(round(np.linalg.det([[5, 4], [2, 4]])))
