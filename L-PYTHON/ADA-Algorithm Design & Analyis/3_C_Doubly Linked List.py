# 3
from collections import deque
dq = deque()
for _ in [None] * int(input()):
    s = input()
    if s == "deleteFirst":
        dq.popleft()
    elif s == "deleteLast":
        dq.pop()
    else:
        a, b = s.split()
        if a == "insert":
            dq.appendleft(b)
        else:
            if b in dq:
                dq.remove(b)
print(" ".join(dq))

# 2
from collections import deque
arr = deque()
n = int(input())
for _ in range(n):
    x = input()
    if x == "deleteFirst":
        arr.popleft()
    elif x == "deleteLast":
        arr.pop()
    else:
        a, b = x.split()
        if a == "insert":
            arr.appendleft(b)
        else:
            if b in arr:
                arr.remove(b)
print(*arr)

arr =[]
for _ in range(n):
    x = input()
    if x == "deleteFirst":
        arr.popleft()
    elif x == "deleteLast":
        arr.pop()
    else:
        x, y = x.split()
        if x == "delete":
            arr = set(arr)
            arr.discard(y)
            arr = list(arr)
        elif x == "insert":
            arr.append(y)
print(*arr)



