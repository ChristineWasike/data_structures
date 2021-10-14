class AssociativeArrayClass:
    def __init__(self, associative_array):
        self.associative_array = associative_array

    def __str__(self):
        return str(self.associative_array)

    def add(self, key, value):
        self.associative_array[key] = value
        return self.associative_array

    def remove(self, key):
        self.associative_array.pop(key)
        return self.associative_array

    def modify(self, key, new_value):
        self.associative_array[key] = new_value
        return self.associative_array

    def lookup(self, key):
        return self.associative_array[key]
