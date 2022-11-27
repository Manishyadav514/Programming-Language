
def swap(A,x,y):
    A[x],A[y]=A[y],A[x]
#A=[10,80,30,40,15,90,10,80,30,90,63,-2]
A = [28, 12, 3, 16]
# INSERTIONSORT
def unknownsort(arr):
    for i in range(len(arr)):  # N element so length n but index upto n-1
        for j in range(i):
            if arr[j] > arr[i]:
                swap(arr, j, i)
    print("Unknownsort IS:", A)


# Insertionsort
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



unknownsort(A)
insertionsort(A)


def selectionsort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        print("Selection Sort:", i,A)
selectionsort([10, 80, 30, 40, 15, 90, 10, 80, 30, 90, 63, 2])


# SORTING MULTIPLE KEYS- USING OPERATOR MODULE
import operator

A= [    ("RAHUL",16,2), ("SHIV",3,22),  ("RAHUL",16,3)  ]

print(sorted(A,key=operator.itemgetter(0,1,2)))
print(sorted(A, key=lambda tpl:(tpl[0],tpl[1],tpl[2])))