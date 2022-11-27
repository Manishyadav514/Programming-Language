A = [1, 2, 3, 4, 5, 100]
x = 2
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print("Yes!")
search(A, x)