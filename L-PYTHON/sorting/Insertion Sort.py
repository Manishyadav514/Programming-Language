# Insertionsort
A=[10,80,30,40,15,90,10,80,30,90,63,-2]
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