from week_four.question_one.Stack import *

sample_stack = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
stack_test = Stack(sample_stack)

print("Print stack: " + str(stack_test))
print("Peek(View recent item): " + stack_test.peek())
print("Popped element(removed recent element): " + str(stack_test.pop()))
print("Pushed element(Added recent element): " + str(stack_test.push("April")))
