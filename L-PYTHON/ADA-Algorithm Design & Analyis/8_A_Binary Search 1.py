#Submitted
import sys
from sys import stdin
input = stdin.readline
class BSTNode:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

def Insert(T, z):
    if T.node > z.node:
        if T.left != None:
            Insert(T.left, z)
        else:
            T.left = z
    else:
        if T.right != None:
            Insert(T.right, z)
        else:
            T.right = z

A = []
def Inorder(root):
	if root:
		# First recur on left child
		Inorder(root.left)
		# appends the data of node
		A.append(str(root.node))
		# now recur on right child
		Inorder(root.right)

B = []
def Preorder(root):
	if root:
		# appends the data of node
		B.append(str(root.node))
		# Then recur on left child
		Preorder(root.left)
		# Finally recur on right child
		Preorder(root.right)

n = int(input())
command = input()
if command[0] == "i":
    a,b = command.split()
    root = BSTNode(int(b))
for _ in range(n - 1):
    command = input()
    if command[0] == "i":
        a, b = command.split()
        child = BSTNode(int(b))
        Insert(root, child)
    elif command[0] == "p":
        Inorder(root)
        Preorder(root)
        print(" " + " ".join(A))
        print(" " + " ".join(B))
        A = []
        B = []

























import sys
from sys import stdin
input = stdin.readline
class BSTNode:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

def Insert(T, z):
    if T.node > z.node:
        if T.left != None:
            Insert(T.left, z)
        else:
            T.left = z
    else:
        if T.right != None:
            Insert(T.right, z)
        else:
            T.right = z


A = []
def Inorder(root):
    if root.left == None:
        A.append(str(root.node))
        if root.right != None:
            Inorder(root.right)
    else:
        Inorder(root.left)
        A.append(str(root.node))
        if root.right != None:
            Inorder(root.right)
        else:
            pass


B = []
def Preorder(root):
    B.append(str(root.node))
    if root.left != None:
        Preorder(root.left)
    else:
        pass
    if root.right != None:
        Preorder(root.right)
    else:
        pass


n = int(input())
command = input()
if command[0] == "i":
    a,b = command.split()
    root = BSTNode(int(b))
for _ in range(n - 1):
    command = input()
    if command[0] == "i":
        a, b = command.split()
        child = BSTNode(int(b))
        Insert(root, child)
    else:
        Inorder(root)
        Preorder(root)
        print(" " + " ".join(A))
        print(" " + " ".join(B))
        A = []
        B = []
















































class node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.key = None

class btree:
    def __init__(self):
        self.root = None
    def insert(self, v):
        y = None
        x = self.root
        z = node()
        z.key = v
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    def print_tree(self):
        def inorder(nd):
            if nd.left is not None:
                inorder(nd.left)
            print(' %i' % nd.key, end='')
            if nd.right is not None:
                inorder(nd.right)

        def preorder(nd):
            print(' %i' % nd.key, end='')
            if nd.left is not None:
                preorder(nd.left)
            if nd.right is not None:
                preorder(nd.right)
        inorder(self.root)
        print()
        preorder(self.root)
        print()


n = int(input())
bt = btree()
for i in range(n):
    inp = input()
    if inp.split()[0] == 'insert':
        bt.insert(int(inp.split()[1]))
    else:
        bt.print_tree()

