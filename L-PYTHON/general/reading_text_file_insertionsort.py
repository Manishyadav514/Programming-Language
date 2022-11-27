file = open("number.txt", "r")
for line in file:
    fields = line.split(",")
    A = [int(ele) for ele in fields]
print(A)

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]       # value, we can start comparison from
        j = i - 1
        #print( arr,i,key,"j:",j)
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Insertion sort:",arr)
insertionsort(A)

def binary_search(A, value):
    first = 0
    last = len(A) - 1
    while (first <= last):
        mid = (first + last) // 2
        if A[mid] == value:
            print("Present at index :", mid + 1)
            exit()
        else:
            if value < A[mid]:
                last = mid - 1
            else:
                first = mid + 1
n = int(input("Enter a number that you are looking for : "))
binary_search(A, n)
