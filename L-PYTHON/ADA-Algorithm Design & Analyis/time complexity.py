L  = [1,2,5,6,4,10,9,23,34]
x = 5
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
def binarySearch(arr, l, r, b):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == b:
            return b
        elif arr[mid] > b:
            return binarySearch(arr, l, mid - 1, b)
        else:
            return binarySearch(arr, mid + 1, r, b)
    else:
        return 1000
def time_Complexity(L,x):
    mergeSort(L)
    for a in L:
        b = binarySearch(L, 0, len(L) - 1, x-a)
        if a+b == x:
            print(a, b)
    '''
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i]+L[j] == x:
                print(L[i], L[j],"==",x)
    '''
time_Complexity(L,x)

