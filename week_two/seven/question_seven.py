def char_dictionary_function(string):
    # Initializing an empty dictionary to hold the characters as keys
    # and have their occurrences map on as values
    #
    occurrence_dictionary = {}

    # Looping through the string and assigning each character a value of its occurrences in the given string
    for character in string:
        occurrence_dictionary[character] = string.count(character)

    return occurrence_dictionary


# char_dictionary_function("christine")
print(char_dictionary_function("I am a sentence with whitespaces    "))
