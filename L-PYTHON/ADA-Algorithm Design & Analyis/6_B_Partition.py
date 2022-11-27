n = int(input())
A = list(map(int, input().split()))
# DIVIDING ARRAY INTO TWO PARTS
def partition(A, p, r):
    x = A[r]                   # pivot value, right most element in A
    i = p                      # Left most element's index
    for j in range(p, r):
        if A[j] <= x:
            A[j], A[i] = A[i], A[j]
            i = i+1            # INCREASE THE PLACE OF i or wall
            #print(A)
    # swap element at r index with element at index i
    A[i], A[r] = A[r], A[i]
    A[i] = "[%d]" %A[i]
    print(" ".join(map(str, A)))
partition(A, 0, len(A)-1 )

"""
Partition(A, p, r)
1 x = A[r]
2 i = p-1
3 for j = p to r-1
4     do if A[j] <= x
5        then i = i+1
6            exchange A[i] and A[j]
7 exchange A[i+1] and A[r]
8 return i+1

12
13 19 9 5 12 8 7 4 21 2 6 11

9 5 8 7 4 2 6 [11] 21 13 19 12
"""














# second
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    _tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = _tmp

    return i + 1


def main():
    n = int(input())
    Array = list(map(int, input().split()))
    q = partition(Array, 0, n - 1)
    Array[q] = "[%d]" % Array[q]
    print(" ".join(map(str, Array)))  # " ".join???????????§????????£??????????????£???


if __name__ == '__main__':
    main()
