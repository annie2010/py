class Queue:
    def __init__(self):
        self.items = []
    def enque(self, item):
        self.items.insert(0, item)
    def deque(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size() == 0


q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)

print ( [q.deque() for i in range(q.size()) ] )
