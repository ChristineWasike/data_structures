from week_four.question_two.Queue import *

sample_queue = ["The", "Quick", "Fox", "Jumps", "Over", "The", "Lazy", "Dog"]
queue_test = Queue(sample_queue)

print(queue_test)
print(queue_test.peek())
print(queue_test.deque())
print(queue_test.enqueue("Marshmallow"))
