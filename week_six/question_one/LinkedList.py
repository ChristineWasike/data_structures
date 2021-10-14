class Node:
    def __init__(self, node):
        self.value = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.head = None

    """
    Creating the search algorithm to ensure that one can look up an item
    A boolean is returned in this method. 
    """

    def search(self, item):
        current = Node(self.head)
        found = False
        while current is not None and not found:
            if current.value == item:
                found = True
            else:
                current = current.next
        return found
