from week_five.test.LinkedList import *
from week_five.test.Node import *


def abracadabra(head):
    my_list = head
    while my_list:
        if my_list.next_node is None:
            break
        if my_list.data is my_list.next_node.data:
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
linked_list.insert(node_1)
linked_list.insert(node_2)
linked_list.insert(node_3)
linked_list.insert(node_4)
linked_list.insert(node_5)
linked_list.insert(node_6)
linked_list.insert(node_7)
linked_list.insert(node_8)
linked_list.insert(node_9)

# print(abracadabra(linked_list.head))

my_array = [1, 3, 4]
my_set = {}
my_set[my_array[0]] = my_array[0]
print(my_set)
