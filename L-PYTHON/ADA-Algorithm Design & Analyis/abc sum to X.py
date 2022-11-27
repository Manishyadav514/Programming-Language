a = 3
b = 36
c = 10
x = 100
A = []
for i in  range(int(x/a)):
    for j in range(int(x/b)):
        for k in range(int(x/c)):
            if a*i+b*j+c*k == x:
                B = []
                B.append(i)
                B.append(j)
                B.append(k)
                A.append(B)
                print(A)
print(min(A))