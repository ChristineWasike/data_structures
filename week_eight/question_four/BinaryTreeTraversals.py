from week_eight.question_four.BinaryTree import *


def print_postorder(root):
    result = "Postorder: "
    if root:
        # First recur on left child
        result = (str(print_postorder(root.left)))

        # the recur on right child
        result = (str(print_postorder(root.right)))

        # now print the data of node
        result += (str(root.value) + ", ")

    return result


test_tree = BinaryTree(4)
test_tree.root.left = BinaryTreeNode(2)
test_tree.root.right = BinaryTreeNode(6)
test_tree.root.left.left = BinaryTreeNode(1)
test_tree.root.left.right = BinaryTreeNode(3)
test_tree.root.right.left = BinaryTreeNode(5)
test_tree.root.right.right = BinaryTreeNode(7)

# Traversal types: preorder, inorder and postorder

print(test_tree.print_order("preorder"))

print(test_tree.print_order("inorder"))

print(print_postorder(test_tree.root))
# print(test_tree.print_order("postorder"))
