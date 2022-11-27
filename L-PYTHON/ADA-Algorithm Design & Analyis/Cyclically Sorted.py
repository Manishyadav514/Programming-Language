A= [10, 29, 33,45,  3, 6, 7]
A =[1,2,3,1,2,3]

def findMin(arr, low, high):
    while (low < high):
        mid = low + (high - low) // 2;
        print(arr[mid])
        if (arr[mid] == arr[high]):
            high -= 1;
        elif (arr[mid] > arr[high]):
            low = mid + 1;
        else:
            high = mid;
    print(arr[high])


n1 = len(A);
findMin(A, 0, n1 - 1)
