K = int(input())
A = list(map(int, input().split()))     # input array
B = [0 for i in range(len(A))]    # output array
def Counting_Sort(A,B, K):
    min_A = int(min(A))
    # C array to store count
    C =[]
    for i in range(int(max(A)) - min_A + 1):
        C.append(0)
    # Store count of each character
    for i in range(0, K):
        C[A[i] - min_A] += 1
    # Change C[i] so it contains the actual position of this element
    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]
    # output
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j] - min_A] - 1] = A[j]
        C[A[j] - min_A] -= 1
    # A now have sorted
    for i in range(0, K):
        A[i] = B[i]
    print(*A)

Counting_Sort(A, B,K)

"""
A = [-5, -10, 0, -3, 8, 5, -1, 10]
B = [0 for _ in range(len(A))]
K = len(A)
"""