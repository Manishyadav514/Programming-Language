class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
root = Node(1)
root.left	 = Node(2)
root.right	 = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# A function to do inorder tree traversal
def Inorder(root):
	if root:
		# First recur on left child
		Inorder(root.left)
		# then print the data of node
		print(root.val),
		# now recur on right child
		Inorder(root.right)
print("\nInorder traversal of binary tree is")
Inorder(root)

# A function to do postorder tree traversal
def Postorder(root):
	if root:
		# First recur on left child
		Postorder(root.left)
		# the recur on right child
		Postorder(root.right)
		# now print the data of node
		print(root.val),
print("\nPostorder traversal of binary tree is")
Postorder(root)

# A function to do preorder tree traversal
def Preorder(root):
	if root:
		# First print the data of node
		print(root.val),
		# Then recur on left child
		Preorder(root.left)
		# Finally recur on right child
		Preorder(root.right)
print("Preorder traversal of binary tree is")
Preorder(root)

