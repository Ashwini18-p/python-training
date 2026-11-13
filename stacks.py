#stack is a linear data sctructure this works on last in first out the last inserted value is the top element
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()   # pop operation 30 is removed bcoz it is inserted last so stack follows lifo
print(stack)

#peek is used to view the top element we use [-1]

stack = [10,20,30]
print(stack[-1])

#isEmpty operation is used to check whether the stack is empty or not
stack = []
if len(stack) == 0:
    print("stack is empty")
else:
    print("stack is not empty")

#if the stack has some values
stack = [10,20,30]
if len(stack) == 0:
    print("stack is empty")
else:
    print("stack is not empty")

#implementing stack using lists 
stack = []
stack.append(30)
stack.append(50)
stack.append(60)
print("stacks:" , stack)
top = stack[-1]
print("stack top element:",top )
removed = stack.pop()
print("removed top stacl:", removed)
top = stack[-1]
print("stack top element:",top )

#queues also a data structure it follows a fifo means first in first out
queue = []
queue.append(10)
queue.append(30)
queue.append(40)
print(queue)

#dequeue which removes a first element from queue
queue = [10,40,60]
queue.pop(0)
print(queue)   #10 is the top element

#collections with dequeue here we can add and add remove the elements at both ends
#enqueue in deque
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)

#dequeue in deque
from collections import deque
queue = deque([10,20,30])
queue.popleft()   #which deleted the left element
print(queue)

#to access the first element we use [0]

from collections import deque
queue = deque([10,20,30])
print(queue[0])

#to access rear element measn last element
from collections import deque
queue = deque([10,20,30])
print(queue[-1])

#complete deque
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print("queue added:", queue)
removed = queue.popleft()
queue.appendleft(70)
print("full updated queue:", queue)



