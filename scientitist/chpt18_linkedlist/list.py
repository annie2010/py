class Node:
    def __init__(self, name, next=None):
        self.name = name
        self.next = next
    def __str__(self):
        return str(self.name)

def print_forward(node):
    while (node):
       print (node)
       node = node.next
    print

def print_backward(list):
    if list == None:
       return
    print_backward(list.next)
    print (list)

node1=Node(1)
node2=Node(2)
node3=Node(3)

node1.next=node2
node2.next=node3

print ("forward")
print_forward(node1)

print ("backward")
print_backward(node1)
