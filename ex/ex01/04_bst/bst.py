class Node:
    def __init__(self, val):
        self.v = int(val)
        self.l = None
        self.r = None   

def isBST(n):

    if (n==None):
       return True
    
    v=n.v
    l=n.l
    if (l!=None):
        if v < l.v: return False
    
    r=n.r
    if (r!=None):
        if v > r.v: return False

    return isBST(l) and isBST(r)


'''
    5
  3    7
 2 4  6 8
1        9   
123456789

'''
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
n8=Node(8)
n9=Node(9)

n5.l=n3
n5.r=n7
n3.l=n2
n3.r=n4
n2.l=n1
n7.l=n6
n7.r=n8
n8.r=n9

print (isBST(n5))
