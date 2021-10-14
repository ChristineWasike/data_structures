class ArrayClass:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return str(self.array)

    def array_length(self):
        return len(self.array)

    def get_element(self, index):
        return self.array[index]

    def set_element(self, value, index):
        self.array[index] = value
        return self.array[index]

# [None for y in range(self.length)]
