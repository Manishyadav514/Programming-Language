n = int(input())
a = list(map(str, input().split()))
arr = a[:]
# bubble sort
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if arr[j][1] > arr[j + 1][1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(' '.join(arr))
print('Stable')
# selection sort
for i in range(len(a)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if a[min_idx][1] > a[j][1]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]
print(' '.join(a))
print('Stable' if arr == a else 'Not stable')




















