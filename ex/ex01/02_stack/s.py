#!/usr/bin/env python

class Stack:
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        if (self.empty()):
            return None
        else:
            return self.items.pop()
    def empty(self):
        return 0 == self.size()
    def size(self):
        return len(self.items)

s=Stack()
s.push(1)
s.push(2)
s.push(3)

print ( [ s.pop() for i in range(s.size()) ] )
