#!/usr/bin/env python

class Queue:
    def __init__(self):
        self.items = []
    def enque(self, val):
        self.items.insert(0, val)
    def deque(self):
        if self.empty():
            return None
        else:
            return self.items.pop()
    def empty(self):
        return 0 == self.size()
    def size(self):
        return len(self.items) 

q=Queue()
q.enque(1)
q.enque(2)
q.enque(3)

print ( [q.deque() for i in range(q.size()) ])   
