class Node:
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.children = []
    def __str__(self):
        return str(self.name)
    def addChild(self,c):
        self.children.insert(0,c)
    def getChildren(self):
        return self.children

def bfs(root):

   root.level = 0

   q = []
   q.insert(0,root)

   while (q):
       p = q.pop()
       print (p, p.level)
       for c in p.children:
           c.level = p.level + 1
           q.insert(0,c)


'''
        A
     B    C
   D E F  G
 H  I
 '''

A=Node('A') 
B=Node('B')
C=Node('C')
D=Node('D')
E=Node('E')
F=Node('F')
G=Node('G')
H=Node('H')
I=Node('I')

A.addChild(B)
A.addChild(C)
B.addChild(D)
B.addChild(E)
B.addChild(F)
C.addChild(G)
D.addChild(H)
D.addChild(I)

bfs(A)

