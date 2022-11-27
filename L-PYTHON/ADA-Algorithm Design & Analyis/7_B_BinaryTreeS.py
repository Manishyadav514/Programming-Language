# individual nodes in a BST
class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1

n = int(input())
h, tree, d = [], [], []  # initializing empty array for height, depth and tree
for i in range(n):
    h.append(0)
    d.append(0)
    tree.append(Node())

def BinaryTree():
    def height(u):
        h1 = h2 = 0
        if tree[u].right != -1: h1 = height(tree[u].right) + 1
        if tree[u].left != -1: h2 = height(tree[u].left) + 1
        h[u] = max(h1, h2)
        return h[u]

    def depth(u, dep):
        d[u] = dep
        if tree[u].right != -1 : depth(tree[u].right, dep + 1)
        if tree[u].left != -1 : depth(tree[u].left, dep + 1)
        return d[u]

    def sibling(u):
        if tree[tree[u].parent].left != u:
            return tree[tree[u].parent].left
        else:
            return tree[tree[u].parent].right

    def degree(u):
        cnt = 0
        if tree[u].left != -1: cnt += 1
        if tree[u].right != -1: cnt += 1
        return cnt

    def set_type(u):
        if tree[u].parent == -1:
            return "root"
        elif tree[u].left == -1 and tree[u].right == -1:
            return "leaf"
        else:
            return "internal node"

    for i in range(n):
        id, left, right = map(int, input().split())
        tree[id].left = left
        tree[id].right = right
        if left != -1: tree[left].parent = id
        if right != -1: tree[right].parent = id
    root_idx = 0
    for i in range(n):
        if tree[i].parent == -1:
            root_idx = i
            break
    # BST height
    height(root_idx)
    # BST depth
    depth(root_idx, 0)

    for i in range(n):
        print('node %i: parent = %i, sibling = %i, degree = %i, depth = %i, height = %i, %s' % (i, tree[i].parent, sibling(i), degree(i), d[i], h[i], set_type(i)))
BinaryTree()

