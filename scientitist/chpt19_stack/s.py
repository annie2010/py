class Stack:

    def __init__(self):
       self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

s = Stack()

s.push(1)
s.push(2)
s.push(3)

print ([s.pop() for i in range(s.size())]) ## py3.4 - print
print (s.pop())



