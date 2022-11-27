# detecting number of prime present inside the list.
def PrimeCheck(x):
    # if x is even
    if x == 2:
        return 1
    # if x is odd
    if x < 2 or x % 2 == 0:
        return 0
    # Check the divisibility of x with numbers below root(x).
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return 0
    return 1


n = int(input())
count = 0
for x in range(n):
    i = int(input())
    count += PrimeCheck(i)
print(count)