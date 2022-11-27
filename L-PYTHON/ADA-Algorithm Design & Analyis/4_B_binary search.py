n1 = input()
A = list(set(map(int, input().split())))
n2 = input()
B = list(set(map(int, input().split())))
A.sort()
B.sort()
def BinarySearch(A, value):
    first = 0
    last = len(A) - 1
    while (first <= last):
        mid = (first + last) // 2   # mid of the array
        if A[mid] == value:
            return True
            #exit()
        else:
            if value < A[mid]:
                last = mid - 1
            else:
                first = mid + 1
i = 0
for a in A:
    print(a)
for a in A:
    print(a)
    if BinarySearch(B,a):
        i +=1
print(i)