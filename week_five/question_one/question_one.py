from week_five.question_one.Node import *
from week_five.question_one.LinkedList import *

"""
Implement a linked-list class (with a tail reference) and all of
the relevant primary methods. You will need to build a node class to help you.
"""


# alphabet_linked_list = LinkedList()
# # a_node = Node("a")
# # b_node = Node("b")
# # c_node = Node("c")
# # d_node = Node("d")
#
# alphabet_linked_list.append_node('a_node')
#
# alphabet_linked_list.append_node('b_node')
#
# print(alphabet_linked_list.head)
# alphabet_linked_list.append_node('c_node')
# print(alphabet_linked_list)


#
# print(alphabet_linked_list.size())
# a_node.set_next(b_node)
# print(a_node.get_next())
#
# alphabet_linked_list.prepend_node(d_node)
# print(alphabet_linked_list)
# print(alphabet_linked_list.size())

def abracadabra(head):
    my_list = head
    while my_list:
        if my_list.next_node is None:
            break
        if my_list.val is my_list.next_node.val:
            my_list.next_node = my_list.next_node.next_node.next_node
        else:
            my_list = my_list.next_node

    print(head)
    return head


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(2)
node_4 = Node(3)
node_5 = Node(4)
node_6 = Node(5)
node_7 = Node(5)
node_8 = Node(6)
node_9 = Node(7)
linked_list = LinkedList()
linked_list.append_node(node_1)
linked_list.append_node(node_2)
linked_list.append_node(node_3)
linked_list.append_node(node_4)
linked_list.append_node(node_5)
linked_list.append_node(node_6)
linked_list.append_node(node_7)
linked_list.append_node(node_8)
linked_list.append_node(node_9)

print(abracadabra(linked_list.head))
