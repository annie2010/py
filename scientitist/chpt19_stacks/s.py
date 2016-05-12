class Stack:

   def __init__(self):
       self.items = []

   def push(self, item):
       self.items.append(item)

   def pop(self):
       if self.empty():
           return None
       else:
           return self.items.pop()

   def empty(self):
       return (self.size() == 0)

   def size(self):
       return len(self.items)


s=Stack()
s.push(1)
s.push(2)
s.push(3)

print ( [ s.pop() for i in range(s.size() ) ] )     
