from week_three.question_one.ArrayClass import *


class DynamicArray(ArrayClass):
    def __init__(self, array):
        super().__init__(array)
        self.array = array

    def add_element(self, element):
        self.array.append(element)
        return self.array

    def delete_element(self):
        self.array.pop()
        return self.array
