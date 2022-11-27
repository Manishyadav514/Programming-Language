def swap(A, x, y):
    A[x], A[y] = A[y], A[x]


arr = [10, 80, 30, 40, 15, 90, 10, 80, 30, 90, 63, 2]

# DIVIDING ARRAY INTO TWO PARTS
def partition(arr, left, right):
    x = arr[right]                   # RIGHT MOST DIGIT VALUE
    wall = left                      # LEFT MOST DIGIT PLACE IN ARRAY IS WALL
    for i in range(left, right):
        if arr[i] < x:
            swap(arr, i, wall)
            wall = wall+1            # INCREASE THE PLACE OF WALL
    # SWAP RIGHT MOST DIGIT TO CURRENT WALL PLACE
    swap(arr, wall, right)
    return wall


# SORTING ELEMENTS OF THE DIVIDED PARTS
def quicksort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quicksort(arr, left, p-1)
        quicksort(arr, p+1, right)


n = len(arr)
quicksort(arr, 0, n-1)
print("Sorted array is:")

# PRINTING SORTED ELEMENTS
for i in range(n):
    print("%d" % arr[i])
