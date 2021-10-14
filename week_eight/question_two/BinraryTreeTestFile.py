from week_eight.question_two.BinaryTree import *

# Creating a tree

#                            5
#                      /           \
#                     3             7
#                  /     \       /     \
#                 1       2     6       8


my_tree = BinaryTree(5)
my_tree.root.left = BinaryTreeNode(3)
my_tree.root.right = BinaryTreeNode(7)
my_tree.root.left.left = BinaryTreeNode(1)
my_tree.root.left.right = BinaryTreeNode(2)
my_tree.root.right.left = BinaryTreeNode(6)
my_tree.root.right.right = BinaryTreeNode(8)
