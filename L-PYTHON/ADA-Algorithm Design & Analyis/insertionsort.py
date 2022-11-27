# it would print the steps of insertionsort
x = int(input())
arr = list(map(int, input().split()))
def insertionsort(n, arr):
    for i in range(n):
        key = arr[i]       # value, we can start comparison from
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # change the list as string
        list = [str(a) for a in arr]
        list = " ".join(list)
        print(list)
insertionsort(x, arr)