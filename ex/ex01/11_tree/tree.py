class Tree:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.name)

def total(tree):
    if tree == None: return 0
    return int(tree.name) + total(tree.left) + total(tree.right)

def print_tree(tree):
    if tree == None: return 0
    print (tree.name)
    print_tree(tree.left)
    print_tree(tree.right)

def print_tree_inorder(tree):
    if tree == None: return 0
    print_tree_inorder(tree.left)
    print (tree.name)
    print_tree_inorder(tree.right)

def print_tree_postorder(tree):
    if tree == None: return 0
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print (tree.name)

left = Tree(2)
left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)

print (tree)  
print (total(tree))  

print ('print tree order')
print_tree(tree)  
print ('print tree in order')
print_tree_inorder(tree)  
print ('print tree post order')
print_tree_postorder(tree)  

'''
http://openbookproject.net/thinkcs/python/english2e/ch21.html
'''
