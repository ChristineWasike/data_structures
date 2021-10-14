"""
Create BinaryTreeNode and BinaryTree Classes including the primary methods
"""


# In a binary search tree, each node can only have up to 2 children hence represented by the left and right
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
