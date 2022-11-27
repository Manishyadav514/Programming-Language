L = [1,2,3,4,5,7,8,9]
x = 3
k = 2
def binarySearch(arr, l, r, b):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == b:
            print("Number is present:",b)
            exit()
        elif arr[mid] > b:
            return binarySearch(arr, l, mid - 1, b)
        else:
            return binarySearch(arr, mid + 1, r, b)
    else:
        return 1000
def KbinarySearch(arr, value, num ):
    #print(arr,num,value)
    for i in range(num):
        #print(len(arr)//num)
        low = i*len(arr)//num
        high = (i+1)*len(arr)//num
        print(low,high)
        if value < arr[high-1]:
            binarySearch(arr, low, high, value)
        elif value == arr[high-1]:
            print("yes")
        else:
            continue
KbinarySearch(L,x,k)



