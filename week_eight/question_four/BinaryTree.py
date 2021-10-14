from week_eight.question_two.BinaryTreeNode import *


class BinaryTree:
    def __init__(self, root):
        self.root = BinaryTreeNode(root)

    def print_order(self, traversal_type):
        traversal_type.lower()
        if traversal_type is "preorder":
            return self.pre_order_traversal(self.root, "Pre-order: ")
        elif traversal_type is "inorder":
            return self.in_order_traversal(self.root, "In-order: ")
        elif traversal_type is "postorder":
            return self.post_order_traversal(self.root, "Post-order: ")
        else:
            return "Not a valid traversal"

    # pre-order traversal: PLR
    def pre_order_traversal(self, start_node, traversal):
        if start_node:
            traversal += (str(start_node.value) + ", ")
            traversal = self.pre_order_traversal(start_node.left, traversal)
            traversal = self.pre_order_traversal(start_node.right, traversal)
        return traversal

    # in-order traversal: LPR
    def in_order_traversal(self, start_node, traversal):
        if start_node:
            traversal = self.in_order_traversal(start_node.left, traversal)
            traversal += (str(start_node.value) + ", ")
            traversal = self.in_order_traversal(start_node.right, traversal)
        return traversal

    # post-order traversal: LRP
    def post_order_traversal(self, start_node, traversal):
        if start_node:
            traversal = self.post_order_traversal(start_node.left, traversal)
            traversal = self.post_order_traversal(start_node.value, traversal)
            traversal += (str(start_node.value) + ", ")
        return traversal
