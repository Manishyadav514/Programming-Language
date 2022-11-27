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

def delete(root, value):
    existFlg = False
    ro = None
    while root is not None:
        if value == root.node:
            existFlg = True
            break
        elif value < root.node:
            ro = root
            root = root.left
        else:
            ro = root
            root = root.right
    # if the node to be deleted is a leaf
    if root.left is None and root.right is None:
        # if parent node exists
        if not ro is None:
            if ro.left == root:
                ro.left = None
            else:
                ro.right = None
        # if the parent node doesn't exists
        else:
            root = None
    # if the node to be deleted has only left child
    elif root.right is None:
        if ro is None:
            root = root.left
        elif ro.left == root:
            ro.left = root.left
        elif ro.right == root:
            ro.right = root.left
    # has only right child
    elif root.left is None:
        if ro is None:
            root = root.right
        elif ro.left == root:
            ro.left = root.right
        elif ro.right == root:
            ro.right = root.right
    # node needs to be deleted has two childs
    else:
        # get the smallest node of the right child
        rp = root.right;
        rq = root
        while not rp.left is None:
            rq = rp
            rp = rp.left
        # swap the value of the node to be deleted and the minimum node of the right child
        root.node = rp.node
        # delete the smallest node of the right child
        if rq.left == rp:
            rq.left = None
        elif rq.right == rp:
            rq.right = None

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
    elif command[0] == "d":
        delete(root, int(command[7:]))
    elif command[0] == "p":
        Inorder(root)
        Preorder(root)
        print(" " + " ".join(A))
        print(" " + " ".join(B))
        A = []
        B = []
