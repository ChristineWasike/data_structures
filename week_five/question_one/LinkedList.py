from week_five.question_one.Node import *


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    """
    This method returns the value of the head in the linked list
    """

    def __str__(self):
        return str(self.tail)

    """
    This method checks whether a linked listed is empty or not and returns a boolean response.
    """

    def is_empty(self):
        return self.head is None

    """
    This is an append method to ensure that the incoming node/item is appended 
    to the right side of the head. It also becomes the tail reference of the linked list.
    """

    def append_node(self, item):
        # new_node = Node(item)
        # current = self.head
        # while current.get_next() is not None:
        #     current = current.get_next()
        # current.set_next(new_node)

        tail = Node(self.tail)
        item_node = Node(item)

        if self.head is None:
            self.head = item_node
        else:
            self.head = self.tail

        tail.set_next(item_node)
        self.tail = item_node

    """
    This method prepends an item to the start of the linked list, to the left of the tail.
    This item becomes the new head of the linked list.
    """

    def prepend_node(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    # Tailored for the prepend method
    # TODO Come back and check that it works even with the append method
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count
