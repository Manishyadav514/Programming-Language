def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
# l is for left index and r is right index of the
# sub-array of arr to be sorted
def Merge_Sort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2
        # Sort first and second halves
        Merge_Sort(arr, l, m)
        Merge_Sort(arr, m + 1, r)
        merge(arr, l, m, r)

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print(arr)
Merge_Sort(arr, 0, n - 1)
print(arr)
