def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual elements and initialize count array as 0
    count = [0 for _ in range(range_of_elements)]
    output = [0 for _ in range(len(arr))]
    # Store count of each character
    for i in range(0, len(arr)):
        count[arr[i] - min_element] += 1
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # Build the output character array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_element] - 1] = arr[i]
        count[arr[i] - min_element] -=
    # Copy the output array to arr, so that arr now contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output[i]
    print(*arr)
count_sort([-5, -10, 0, -3, 8, 5, -1, 10])





def countSort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
    # Create a count array to store count of inidividul characters and initialize count array as 0
    count = [0 for i in range(256)]
    # For storing the resulting answer since the string is immutable
    ans = ["" for _ in arr]
    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[ i -1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i]) ] -1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

# Driver program to test above function
arr = "geeksforgeeks"
ans = countSort(arr)
print("Sorted character array is % s" %("".join(ans)))

# This code is contributed by Nikhil Kumar Singh