a,b = map(int, input().split())
def gcd(a, b):
    # Everything divides 0
    if (a == 0):
        return b
    elif (b == 0):
        return a
        # base case
    elif (a == b):
        return a
        # a is greater
    elif (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)
print(gcd(a, b))