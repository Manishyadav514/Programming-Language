x = int(input())
B = list(map(int, input().split()))
def bubbleSort(arr):
    n = len(arr)
    k = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k = k + 1
    list = [str(a) for a in arr]
    list = " ".join(list)
    print(list)
    print(k)
bubbleSort(B)

