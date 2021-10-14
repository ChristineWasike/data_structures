from week_eight.question_two.BinaryTreeNode import *


def height(node):
    # Check that is a node is a leaf the height should be added as 0
    if node is None:
        return 0

    else:
        # Calculating the max height of the left subtree
        left_height = height(node.left)
        # Calculating the max height of the right subtree
        right_height = height(node.right)

        # Use the greater height as the max height
        max_height = max(left_height, right_height) + 1
        return max_height


sample_tree = BinaryTreeNode(1)
sample_tree.left = BinaryTreeNode(2)
sample_tree.right = BinaryTreeNode(3)
sample_tree.left.left = BinaryTreeNode(4)
sample_tree.left.right = BinaryTreeNode(5)
sample_tree.right.left = BinaryTreeNode(6)
sample_tree.right.right = BinaryTreeNode(7)

print(height(sample_tree))
