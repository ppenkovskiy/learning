# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)
# in python lists (dynamic arrays), when you add an element,
# if the list is not long enough - a new list 2 times longer is creating,
# elements from the old one are copied to the new list. which is time-consuming.
# so a stack of python lists (dynamic array) is not always the best solution.
# value = stack.pop()
# print(value)

# if the stack can contain thousands of elements the best way is using deque
from collections import deque

stack = deque([1,2,3])
stack.append(4)
stack.append(5)
print(stack)
last_element_in_stack = stack.pop()
print(last_element_in_stack)
print(stack)
# OR
print('Another way to implement a stack:')
stack = deque([1,2,3])
stack.appendleft(0)
stack.appendleft(-1)
print(stack)
last_element_in_stack = stack.popleft()
print(last_element_in_stack)
print(stack)

