# 1
from collections import deque
n, q = map(int, input().split())
dq = deque()
for _ in range(n):
    p, t = map(str, input().split())
    dq.append([p, int(t)])
total = 0
while dq:
    pt = dq.popleft()
    if pt[1] <= q:
        total += pt[1]
        print(pt[0], total)
    else:
        total += q
        dq.append([pt[0], pt[1] - q])

# 2
from collections import deque
n, q = map(int, input().split())
A = deque(input().split() for _ in range(n))
time = 0
while A:
    a,b = A.popleft()
    if int(int(b)) <= q:
        time = time + int(b)
        print(a, time)
    else:
        b = int(b) - q
        time += q
        A.append([a,b])


