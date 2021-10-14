import unittest
from week_four.question_two.Queue import *


class QueueTest(unittest.TestCase):
    # Checks that a queue data structure has been created
    def test_create_a_queue(self):
        test_array = ['Sydney', 'Maya', 'Albert', 'Daniella']
        test_queue = Queue(test_array)
        self.assertEqual(str(test_queue), "['Sydney', 'Maya', 'Albert', 'Daniella']")

    # Checks that the first element of the queue is viewed
    def test_peek_method(self):
        test_array = ["Surgeon", 'Dentist', 'Ophthalmologist', 'Pediatrician']
        test_queue = Queue(test_array)
        self.assertEqual(test_queue.peek(), "Surgeon")

    # Checks that the new item is added to the back of the queue
    def test_enqueue_method(self):
        test_array = [1, 2, 3, 4]
        test_queue = Queue(test_array)
        self.assertEqual(test_queue.enqueue(5), [1, 2, 3, 4, 5])

    # Checks that the first item on the queue is removed
    def test_deque_method(self):
        test_array = ['Sydney', 'Maya', 'Albert', 'Daniella']
        test_queue = Queue(test_array)
        self.assertEqual(test_queue.deque(), ['Maya', 'Albert', 'Daniella'])
