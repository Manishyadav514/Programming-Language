A = [[ 1, 3, 7, 8, 16 ],
[ 2, 3, 8, 13, 17 ],
[ 4, 5, 14, 15, 21 ],
[ 8, 17, 17, 21, 23 ],
[ 11, 17, 24, 26, 30 ]]


def matrix_check(A, value):
    for i in range(len(A)):
        first = 0
        last = len(A[i]) - 1
        while (first <= last):
            mid = (first + last) // 2
            if A[i][mid] == value:
                print("it is available at",i, mid)
                exit()
            else:
                if value < A[i][mid]:
                    last = mid - 1
                else:
                    first = mid + 1
matrix_check(A, 26)


def matrix_nm_check(A, value):
    for i in range(len(A)):
        for j in range(len(A[1])):
            if A[i][j] == value:
                print("Index of ", value, "is", i, j)
matrix_nm_check(A, 26)