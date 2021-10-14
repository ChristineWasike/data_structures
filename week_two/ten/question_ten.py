# Input an integer n and outputs a list with 1 once, 2 twice, 3 three times….n n-times e.g. f(3) = [1,2,2,3,3,3]

def n_times_display(number):
    number_list = []
    i = 1
    j = 1

    while i <= number:
        number_list.append(str(i) * j)
        i += 1
        j += 1
    return number_list


print(n_times_display(34))
