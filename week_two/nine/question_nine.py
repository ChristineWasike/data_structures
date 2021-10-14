f_list = ["a", "b", "c"]
s_list = ["a", "b", "i", "c"]


def spot_extra_element(first_list, second_list):
    for element in second_list:
        if element not in first_list:
            return element


print(spot_extra_element(f_list, s_list))
