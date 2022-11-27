n1 = input()
A = list(set(map(int, input().split())))
n2 = input()
B = list(set(map(int, input().split())))
A.sort()
B.sort()
# linear search function
def LinearSearch(arr, x):
    for i in range(len(arr)):
        # if element of A is in B, return True
        if arr[i] == x:
            return True
i = 0
for a in A:
    if LinearSearch(B,a):
        i +=1
print(i)
