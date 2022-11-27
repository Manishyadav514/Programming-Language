
# QUICKSORT


def swap(A,x,y):
    A[x],A[y]=A[y],A[x]
arr=[10,80,30,40,15,90,10,80,30,90,63,-2]

def quicksort(arr, left, right):
    # DIVIDING ARRAY INTO TWO PARTS
    def partition(arr, left, right):
        x = arr[right]                                     # RIGHT MOST DIGIT VALUE
        wall = left                                        # LEFT MOST DIGIT PLACE IN ARRAY IS WALL
        for i in range(left, right):
            if arr[i] < x:
                swap(arr, i, wall)
                wall = wall + 1                             # INCREASE THE PLACE OF WALL
        swap(arr, wall, right)                              # SWAP RIGHT MOST DIGIT TO CURRENT WALL PLACE
        return wall
    # MAIN CODES OF THE QUICKSORT
    if left<right:
        p=partition(arr, left, right)
        quicksort(arr, left, p-1)
        quicksort(arr, p+1, right)
n = len(arr)
quicksort(arr, 0, n-1)
print("SORTED ARRAY USING QUICKSORT IS:", arr)
#####
# MODIFIED TO COUNTING NUMBER OF STEPS
# Function to swap the elements
def swap(A,x,y):
    A[x],A[y]=A[y],A[x]
arr=[2,1,3]
#
B = []                                        # empty array to store the number of swaping performed
def partition(arr, left, right):
    x=arr[left]                               # LEFT MOST DIGIT VALUE
    wall=right                                #  WALL IS THE RIGHT MOST DIGIT PLACE IN ARRAY
    for i in range(left, right):
        if arr[right-i]<x:
            swap(arr,right-i,wall)
            if wall>right-i:                 # TO ADD NUMBER OF SWAP PERFORMED IN EACH PARTITION
                B.append(arr[wall])
            wall=wall-1                      # INCREASE THE PLACE OF WALL
    swap(arr,wall,left)                      # SWAP RIGHT MOST DIGIT TO CURRENT WALL PLACE
    if wall>left:
        B.append(arr[wall])
    return wall
#
D = []
C=[]
def quicksort(arr, left, right):
    if left<right:
        p=partition(arr, left, right)
        for i in range(left,right+1):
            D.append(i)
        C.append(len(B))
        quicksort(arr, left, p-1)
        quicksort(arr, p+1, right)
    return(D,C)

quicksort(arr, 0, len(arr)-1)
print("Number of Comparison",len(D))
print("Number of Swaps Perforned:",sum(C))
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
#
# SWAP FUNCTION TO SWAP ELEMENTS OF THE ARRAY
def swap(A,x,y):
    A[x],A[y]=A[y],A[x]
arr=[2,1,3]

# DIVIDING ARRAY INTO TWO PARTS
B = []                               # EMPTY ARRAY DEFINED TO ADD THE NUMBER  OF SWAPING
def partition(arr, left, right):
    x=arr[right]                   # THE VALUE OF RIGHT MOST DIGIT
    wall=left                         # LEFT MOST DIGIT PLACE IN ARRAY IS WALL
    for i in range(left, right):
        if arr[i]<x:
            swap(arr,i,wall)
            if wall<i:                # SWAPING IS NOT PERFORMED IN THE CASE, WALL=i
                B.append(arr[wall])
            wall=wall+1               # INCREASE THE PLACE OF WALL
    swap(arr,wall,right)              # SWAP RIGHT MOST DIGIT TO CURRENT WALL PLACE
    # THE LAST SWAP HAPPENED IN THE CASE OF RIGHT MOST ELEMENTS
    if wall<right:
        B.append(arr[wall])
    return wall
#SORTING ELEMENTS OF THE DIVIDED PARTS
A = []
C=[]
D=[]
def quicksort(arr, left, right):
    if left<right:
        p=partition(arr, left, right)
        for i in range(left,right+1):
            D.append(i)
        C.append(len(B))
        A.append(p)                             # TO ADD THE VALUE OF P, LATER IT'S USED TO FIND NUMBER OF PARTITION
        quicksort(arr, left, p-1)
        quicksort(arr, p+1, right)
    return(A,C,D)
quicksort(arr, 0, len(arr)-1)
print("Number of Comparison:",len(D))
print("Number of Partition:",len(A))
print("Number of Swaps Perforned:",sum(C))
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])