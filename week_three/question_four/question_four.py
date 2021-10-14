from week_three.question_four.AssociativeArrayClass import *

associative_array = {
    1: "one",
    2: "two"
}

associative_array[3] = "three"

print(associative_array)

associative_array.pop(2)

print(associative_array)

my_dictionary = AssociativeArrayClass({1: "3", 2: "6", 3: "9"})
print(my_dictionary)
print(my_dictionary.remove(2))
