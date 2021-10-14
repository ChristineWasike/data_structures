# Function that removes whitespace from a string
# 

def whitespace_remover(whitespace):
    # Using the split method, this splits the words within the string into different strings within a list
    # The join method then concatenates each element(word) of the list with a single space
    return " ".join(whitespace.split())

