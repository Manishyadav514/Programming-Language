n = int(input())

arr = tuple(tuple(map(int, input().split())) for _ in range(n))

dp = [[10 ** 10] * n for i in range(n)]      # dp [i] [j] is the minimum number of calculations for the interval [i, j]


for d in range(n):
    dp[d][d] = 0

def Matrix_Chain_Multiplication():
    for l in range(1, n):
        for i in range(n):
            j = i+l
            if j >= n:
                continue
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1])
    print(dp[0][-1])

Matrix_Chain_Multiplication()




















n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(arr)
s = 1

def Scalar_Multiplicatin_in_Matrix(arr,s):
    if len(arr)==1:
         print(s)
    else:
        s = s * arr[0][0] * arr[0][1] * arr[1][1]
        print(s)
        print(arr[0][0], arr[0][1], arr[1][1])
        arr[0] = [arr[0][0],arr[1][1]]
        arr.remove(arr[1])
        print(arr)
        Scalar_Multiplicatin_in_Matrix(arr, s)

Scalar_Multiplicatin_in_Matrix(arr,s)