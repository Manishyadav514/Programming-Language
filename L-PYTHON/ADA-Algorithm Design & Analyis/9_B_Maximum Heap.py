H = int(input())
A = list(map(int, input().split()))


def maxHeapify(A, i):
    l = (i + 1) * 2 - 1
    r = (i + 1) * 2

    # select the node which has the maximum value
    if l < H and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < H and A[r] > A[largest]:
        largest = r

    # value of children is larger than that of i
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)


def buildMaxHeap(A):
    for i in range(H // 2, -1, -1):
        maxHeapify(A, i)
    print("", *A)


buildMaxHeap(A)




