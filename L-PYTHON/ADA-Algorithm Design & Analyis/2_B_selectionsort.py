x = int(input())
A = list(map(int, input().split()))
k=0
for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
    if min_idx == i:
        continue
    else:
        k += 1
l = [str(a) for a in A]
l = " ".join(l)
print(l)
print(k)