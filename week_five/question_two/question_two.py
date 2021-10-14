from week_five.question_two.DoublyLinkedList import *

"""
Implement a doubly-linked list class and implement the following methods
a. doublylinkedlist.insert(node, prevNode) - insert node after prevNode
b. doublylinkedlist.delete(node) - delete node from doublylinkedlist
"""

node_one = Node(2)
node_two = Node(3)
doubly_linked_list = DoublyLinkedList()

doubly_linked_list.insert_node(node_one)
doubly_linked_list.insert_node(node_two)


print(doubly_linked_list.tail)
print(node_one.get_previous())
print(node_one.set_next(node_two))
print(str(node_one.get_next()))
