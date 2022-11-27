# ++++++++++++ MATHEMATICAL OPERATION ++++++++++++++++#





#############################
# ARITHMETIC OPERATIONS
######
a=10
b=2
a+=b          # a=a+b
print("1:",a)      # a=12
a-=b          # a=a-b
print("2:",a)      # a=10
a/=b          # a=a/b
print("3:",a)      # a=5
a*=b          # a=a.b
print("4:",a)      # a=10
a**=b         # a=a^b
print("5:",a)      # a=100
a//=b         # FLOOR DIVISION--LARGEST INTEGER<=QUOTIENT
print("6:",a)      # a=50
a%=7         # a-(b*(a//b))
print("7:",a)      # a=1
#####
a=10
b=3
print("1.1:", b+a)
print("1.2:", b-a)
print("1.3:", a/b)                                         # FLOOR DIVISION # GIVES EXACT FLOST VALUE OF QUOTIENT AFTER DEVISION
print("1.4:", a//b)                                        # GIVES INTEGER VALUE LOWER OR EQUAL OF QUOTIENT AFTER DEVISION
print("1.5:", a%b)                                         # a-(b*(a//b)) # GIVES REMAINDER AFTER DEVISION
print("1.6:", a**b)
print("1.7:", a*b)
print("1.8:", 10//3**2%5/2)
print("1.9:", 2-10//3**4%5/2+10)                           # PEMDAS
print("1.9:", -10//3,10//-3,-10//-3)
print("2.0:a-(b*(a//b)):", -10%3, 10%-3, -10%-3)
#####



print("===================================")





##########################
# CONVERSIONS
print("1:",int(23.3))
print("2:",float(20))
print("3:",bool(20))
print("4:",str(100))
print("5:",chr(32))
print("6:",complex(23.3,10))
print("7:", int(True))
print("8:", int("100", 8), int('10', 2))              # OCTAL/BINARY TO DECIMAL INT
n=23.1
print(n)
print("9:       %d"%(float(n)))                         # CHANGING NUMBER INTO INTEGER
print("1.0:     %.2f"%(float(n)))                       # A DECIMAL NUMBER HAVING TWO PLACE AFTER DECIMAL
print('1.1:     %0.5d'%(float(n)))                      # INTEGER HAVING FIVE DIGIT LEADING WITH ZERO IF NEEDED
print('1.2:   ', round(float(n)))                       # ROUND OF TO NEAR
n=str("13.45")
print('1.2:'   ,int(n[0]))                              # RETURNS FIRST DIGIT OF THE NUMBER (STRING)
#####
# APPLICATION
print("manish yadav"+str(23.4))
#####





print("===================================")





#############################
#   ROOT VIA BINARY SEARCH
####
def nthroot(x, n):
    x = float(x)
    n = int(n)
    low = 1
    high = x
    let = (low + high) / 2
    while abs(let ** n - x) >= 0.00001:
        if let ** n > x:
            high = let
        else:
            low = let
        let = (low + high) / 2
        return let
print("1:",nthroot(9,2))           # x=input(print("Enter a number x>=1:")) # n=input(print("Enter a number n>0:"))
# VIA SIMPLE FUNCTION
def nthroot(x, n):
    x = float(x)
    n = int(n)
    z=x**1/n
    return z
print("2:", nthroot(8,2))
######



print("===================================")




#############################
# FACTORIAL
#####
# 1.1
def fac1(n):
    if n==0:
        return 1
    return n*fac1(n-1)        # RETURN BACK TO THIS POINT AGAIN WHENEVER 0 CONDITION WILL NOT REACH
print("1.1:",fac1(3))
# 1.2
def fac2(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
print("1.2:",fac2(3))
######



print("===================================")




#############################
# SQUARE OF A NUMBER
#####
# 2.1
def sq(a):
    c=a*a
    return c
print("2.1:",sq(4))
# 2.2
def sq(a):
    return a*a
print("2.2:", sq(4))
# 2.3
f=lambda a:a*a
print("2.3:", f(9))
######



print("===================================")




#############################
# FIBONACCI SEQUENCE FIND
#####
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b*n
            b=c
            return c
print("3.1:", fib(4))
######



print("===================================")




#############################
# DIVISION
#####
def div1(a,b):
    if a<b:
        a,b=b,a
    return a/b
print("1:", div1(2,4))
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return  func(a,b)
    return  inner
div=smart_div(div)
div(2,4)
######



print("===================================")




#############################
# ADDITION
#####

# 1.
def add_sub(x,y):
   c=x+y
   d=x-y
   return c, d
result1,result2=add_sub(5,4)
print(result1,result2)
# 2.
def add(x,y):
    c=x+y
    print(c)
add(4,3)
# 3.
def update(x):
    print(id(x))
    x=8
    print("x",x)
a=10
update(a)
print(id(a))
print("a",a)
######



print("===================================")





#############################
# BUILT IN FUNCTIONS IN  MATH MODULE
#####
print("1.1:", abs(-2.1))
print("1.2:", pow(3,2))
print("1.3:", min(2,3,1,10))
print("1.4:", max(2,3,1,10))
print("1.5:", divmod(4,2))                  # RETURN A//B AND A%B
print("1.6:", bin(10))
print("1.7:", hex(10))
print("1.8:", oct(10))
print("1.9:", "a:", round(2.59), "b:",  round(2.59851, 3))
#####



print("===================================")






# ++++++++++++ MATH MODULE++++++++++++++++#





#############################
# ARITHMETIC OPERATIONS
######
from  math import *
# MATHEMATICAL FUNCTION
print("1.0:", pi,e)
print("1.1:", sq(2))
print("1.2:", sqrt(4))
print("1.3:", fac1(4), fac2(4), factorial(4))
print("1.4:", fabs(-2.29) )                                      # ABSOLUTE VALUE
print("1.5:",  log10(10), log(10), log1p(10), log2(10) )
print("1.6:", exp(0), expm1(0), frexp(0),  )
print("1.7:", trunc(5.9) )                                    #
print("1.8:", ceil(-2.29) )                                   # SMALLEST INTEGER>=X
print("1.9:", floor(-2.29) )                                  # LARGEST INTEGER<=X
print("2.0:", modf(-2.29) )                                   #
# TRIGNOMENTRIC FUNCTION
print("2.1:", degrees(1) )                                  # DEGREE TO RADIAN
print("2.2:", radians(180) )                                  # RADIAN TO DEGREE
print("2.3:", sin(90), cos(90), tan(1) )                      # FUNCTION OF X RADIAN
print("2.4:", sinh(1), cosh(1), tanh(1) )                   # HYPERBOLIC SINE OF X
print("2.5:", asin(1), acos(1), atan(1) )                   # SINE INVERSE OF X, IN RADIAN
#print("2.6:", asinh(1), acosh(1), atanh(1) )                #
print("2.7:", hypot(2,10) )                                 # SQRT(X*X+Y*Y)
##########


print("===================================")




print("===================================")




#############################
# DIVISION
#####

######



print("===================================")




#############################
# DIVISION
#####

######



print("===================================")




#############################
# DIVISION
#####

######



print("===================================")




#############################
# DIVISION
#####

######



print("===================================")




#############################
# DIVISION
#####

######



print("===================================")







