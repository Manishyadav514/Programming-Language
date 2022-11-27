
def findMin(arr, low, high):
    while (low < high):
        mid = low + (high - low) // 2;
        if (arr[mid] == arr[high]):
            high -= 1;
        elif (arr[mid] > arr[high]):
            low = mid + 1;
        else:
            high = mid;
    return arr[high];

if __name__ == '__main__':
    arr1 = [5, 6, 2,3, 4];
    print("The minimum element is ",
          findMin(arr1, 0, len(arr1) - 1));



def rotate(arr, n):
    x = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];
    arr[0] = x;
arr = [1, 2, 3, 4, 5]
n = len(arr)
print("Given array is")
for i in range(0, n):
    print(arr[i], end=' ')
rotate(arr, n)
print("\nRotated array is")
for i in range(0, n):
    print(arr[i], end=' ')


