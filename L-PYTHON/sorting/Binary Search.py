A = [1, 2, 3, 4, 5, 100]
def binary_search(A, value):
    first = 0
    last = len(A) - 1
    while (first <= last):
        mid = (first + last) // 2
        if A[mid] == value:
            print(A[mid], "is present in list")
            exit()
        else:
            if value < A[mid]:
                last = mid - 1
            else:
                first = mid + 1
binary_search(A, 100)


