def merge(A, left, mid, right):
    global count
    # creating temp arrays
    L = A[left:mid]+[float("inf")]
    R = A[mid:right]+[float("inf")]
    # left and right indexes
    l = 0; r = 0
    for k in range(left,right):
        # incrementing count for each comparison
        count += 1
        if L[l] <= R[r]:
            A[k] = L[l]
            l = l + 1
        else:
            A[k] = R[r]
            r = r + 1

def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left+right)//2
        # Sort first and second halves
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
    return A


n = int(input())
A = list(map(int,input().split()))
count = 0
print(*mergeSort(A, 0, n))
print(count)

