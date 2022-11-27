# METHOD 2
B = [10,80,30,40,15,90,10,80,30,90,63,-2]
def bubbleSort(arr):
    n = len(arr)
    k = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k = k + 1
    print("1:",arr)
    print("Number of swap performed:", k)
bubbleSort(B)


# METHOD 1
A=[10,80,30,40,15,90,10,80,30,90,63,-2]
def BubbleSort(arr):
    def Sort(arr):
        B = []
        for i in range(len(arr) - 1):                     # N element so length n but index upto n-1
            if arr[i] > arr[i + 1]:
                B.append(arr[i])
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return len(B)
    n=Sort(arr)
    if n!=0:
        BubbleSort(arr)
    else:
        print("A:", A)
BubbleSort(A)

