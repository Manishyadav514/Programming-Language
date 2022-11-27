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

'''
10
insert 30
insert 88
insert 12
insert 1
insert 20
find 12
insert 17
insert 25
find 1000
print
'''

def find(root, key):
    if root is None:
        print("no")     # if element is not in BST, prints no
    elif root.node == key:
        #print(root.node, key)
        print("yes")
    elif key < root.node:
        find(root.left, key)
    elif key>root.node:
        find(root.right, key)
    else:
        print("no")

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
    elif command[0] == "f":
        find(root, int(command[5:]))
    elif command[0] == "p":
        Inorder(root)
        Preorder(root)
        print(" " + " ".join(A))
        print(" " + " ".join(B))
        A = []
        B = []
