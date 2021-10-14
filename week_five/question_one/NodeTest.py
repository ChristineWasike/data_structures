from week_five.question_one.Node import *
import unittest


class NodeTest(unittest.TestCase):
    # Check that a node has successfully been created
    def test_node_class(self):
        test_node = Node(54)
        self.assertEqual(str(test_node), "Node " + str(test_node.get_data()) + " created.")

    # Check that the data within a node can be retrieved
    def test_get_data_from_node(self):
        test_node = Node("I'm a node.")
        self.assertEqual(test_node.get_data(), "I'm a node.")

    # Check that the value of an existing node can be set to something new
    def test_set_data_to_node(self):
        test_node = Node(109)
        self.assertEqual(test_node.set_data(99), 99)

    # Check that upon creating a node, the value of next node is set to None
    def test_next_node_set_to_none(self):
        test_node = Node(345)
        self.assertEqual(test_node.next_node, None)

    # Check that next node can be set for the existing node
    def test_set_next_node(self):
        test_node = Node([1, 2, 3, 4])
        self.assertEqual(test_node.set_data([3, 4, 5]), [3, 4, 5])

    # Check that the next node can be retrieved from the node
    def test_get_next_node(self):
        test_node = Node(1)
        test_node.set_next(2)
        self.assertEqual(test_node.get_next(), 2)
