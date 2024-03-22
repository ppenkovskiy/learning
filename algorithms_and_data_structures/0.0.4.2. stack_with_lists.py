# Stack implementation in using Python lists (python lists == dynamic arrays data structure in programming).
# But when there are thousands of elements on the stack, it is better to use deque (doubly linked list),
# because adding elements to the end of a dynamic array may require creating a full copy of it,
# which is  time-consuming.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)  # output:           "Stack: [1, 2, 3]"
print("Pop:", stack.pop())  # output:             "Pop: 3"
print("Peek:", stack.peek())  # output:           "Peek: 2"
print("Is Empty:", stack.is_empty())  # output:   "Is empty: False"
print("Size:", stack.size())  # output:           "Size: 2"

# In the example above, elements are pushed onto the stack and then popped off the stack,
# demonstrating LIFO behavior, on which STACK data structure is based.
