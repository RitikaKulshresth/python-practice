# from collections import deque

# stack = deque()

# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.append('d')

# print(stack)

# stack.pop()

# print(stack)

class Stack:

    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def isempty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

