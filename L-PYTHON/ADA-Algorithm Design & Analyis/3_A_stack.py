A = list(map(str, input().split()))
arr = []
for c in A:
    #print("A:", c)
    if c.isdigit():
        arr.append(c)
        #print(c)
    elif c in "+-*":
        a = arr.pop()
        b = arr.pop()
        #print(a,b)
        arr.append(str(eval(b + c + a)))
print(arr[0])
