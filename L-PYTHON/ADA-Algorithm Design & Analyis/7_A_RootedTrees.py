# working
n = int(input())
sibling = [-1 for i in range(n)]
parent = [-1 for i in range(n)]
child = [-1 for i in range(n)]
def RootedTree():
    # To find the depth
    def depth(u):
        i = 0
        while parent[u] != -1:
            u = parent[u]
            i += 1
        return i
    # To create a child
    def children(u):
        if child[u] == -1:
            return []
        A = []
        A.append(child[u])
        while sibling[child[u]] != -1:
            child[u] = sibling[child[u]]
            A.append(child[u])
        return A
    #
    def set_type(u):
        s = "internal node"
        if parent[i] == -1:
            s = "root"
        elif child[i] == -1:
            s = "leaf"
        return s
    for i in range(n):
        arr = [int(i) for i in input().split()]
        index = arr[0]
        if arr[1] != 0:
            child[index] = arr[2]
            for i in range(2, len(arr)):
                parent[arr[i]] = index
                if i != len(arr) - 1:
                    sibling[arr[i]] = arr[i + 1]
    # argument to print the result
    for i in range(n):
        print("node {}: parent = {}, depth = {}, {}, {}".format(i, parent[i], depth(i), set_type(i), children(i)))
RootedTree()


