class Node:
    """
    Initializing the Node class such that it takes in the node value and that
    the next node that it stores is set to None, meaning that it is an independent node.
    """

    def __init__(self, node_data):
        self.node_data = node_data
        self.next_node = None

    """
    Ensuring that the node is printed out when called in the print statement
    """

    def __str__(self):
        return str(self.node_data)

    """
    The get_data method fetches the value that the current node has
    """

    def get_data(self):
        return self.node_data

    """
    the set_data method changes the value within a node to a different value, 
    it also takes in new_value as its parameters.
    """

    def set_data(self, new_value):
        self.node_data = new_value
        return self.node_data

    """
    The get_next method has to do with fetching the value of the next node that it is
    tied to.
    """

    def get_next(self):
        return self.next_node

    """This method sets the value of the next node to a certain value and hence points 
    to a new node in a different point in memory"""

    def set_next(self, new_next_node):
        self.next_node = new_next_node
        return self.next_node
