from collections import deque

dq = deque()  # creating empty queue
print(dq)


dq = deque([1,2,3,4,5], maxlen=5)  # creating queue with set of initial values
dq.append(6) # this command will remove the current first element '1'
print(dq)


dq = deque([1,2,3,4,5])
dq.append(6)
dq.append(7)
dq.appendleft(0)
print(dq)

dq = deque([1,2,3])
try:
    value_last = dq.pop()  # delete the last element
    value_first = dq.popleft()  # delete the first element
    print(value_last)
    print(value_first)
except IndexError as e:
    print(e)

dq = deque()
try:
    value_last = dq.pop()  # delete the last element
    value_first = dq.popleft()  # delete the first element
    print(value_last)
    print(value_first)
except IndexError as e:
    print(e)


dq = deque()
dq.extend([90,91,92])
dq.extendleft((89,88,87))
print(dq)


dq = deque([1,2,4])
dq.insert(2, 3)
print(dq)



dq = deque([1,3,5])
dq.remove(3)
print(dq)

dq = deque([1,2,3])
dq.clear()
print(dq)

dq_1 = deque([1,2,3])
dq_2 = dq_1.copy()
dq_2.append(100)
print(dq_1)
print(dq_2)

# FIFO
dq.appendleft(10)
value = dq.pop()
#or
dq.append(10)
value = dq.popleft()

# LIFO
dq.appendleft(10)
value = dq.popleft()
#  or
dq.append(10)
value = dq.pop()