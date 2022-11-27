#++++++++++++ CONDITIONS ++++++++++++++++#






#############################
# IF/ELSE/ELIF
####
x=5
if x==1:
    print("one")
elif x==2:
    print("two")
elif x==3:
    print("three")
else:
    print(
#####"false")



print("===================================")




#############################
# Print anything n times.
#####
# A.WHILE LOOP
# 1.
i=1
while i<=5:
    print("manish",i)
    i=i+1
# 2.
i=5
while i>=1:
    print("manish",i)
    i=i-1
#####
# PRINT SOMENTHING BESIDE
#####
i=1
while i<=5:
    print("manish",end="**")
    j=1
    while j<=4:
         print("dada",end="**")
         j=j+1
    i=i+1
    print()
#####




print("===================================")




#############################
# PRINT SEQ OR SET LINE BY LINE
#####
x=[10,"ram",20]
for i in x:
    print(i)
for i in range (1,20):
    if i%5!=0:                             # leaving digit divisible by five
        print(i)
# 1 T0 100 EXCEPT DIVISIBLE BY 15
for i in  range(1,31):
    if i%3==0 and i%5==0:
        continue
    print(i)
#####



print("===================================")




#############################
#WENDING MACHINE
#####
av=5
x=4
i=1
while i<av:
    print("Candy")
    if i>=av:
        print("out of stock")
        print("avilable cande is",av)
    i=i+1
print("Bye")
#####



print("===================================")




#############################
# USE OF PASS-CONTINUE-BREAK
#####
for i in range(5):
    if i==3:
        continue                        # leave 3 chance and process forward
    print("hello",i)
for i in range(5):
    if i==3:
        break                           # its leave 3 chance and end further process
    print("GOOD",i)
for i in range(1,11):
    if i%2!=0:                          # use= on placo of !to print only odd nnnmber
        pass                            # PASS =... OR NO-OP INSTRUCTION
    else:
        print(i)
print("bye")
#####



print("===================================")




#############################
# PRINT DESIRED DIVISIBLE NUMBERS FROM ARRAY
#####
for i in range(6):
    for j in range(8):
        print("#",end="*")                              #end="" to  print # in same line
    print()                                             #to print # into another line
nums=[10,58,67,78,80,76]
for i in nums:
    if i%5==0:
        print(i)
        break
else:
    print("not found")
# IDENTIFY PRIME
num=10
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("Prime")
#####



print("===================================")




#############################
# TAX CALCULATION HAVING DIFFERENT VALUE OF TAX AT DIFFERENT INCOME
#####
n=100000
t_percent=30
if n<=15:
    if n>=12.5:
        t_percent=25
    if n>10 and n<12.5:
        t_percent=20
    if n>7.5 and n<10:
        t_percent=15
    if n>5 and n<7.5:
        t_percent=10
    if n>2.5 and n<5:
        t_percent=5
    if n<2.5:
        t_percent=0
tax= n*t_percent/100
print("TAX:",tax,'lakh')
t_Oldpercent=30
if n<=15:
    if n>12.5:
        t_Oldpercent=30
    if n>10 and n<12.5:
        t_Oldpercent=30
    if n>7.5 and n<10:
        t_Oldpercent=20
    if n>5 and n<7.5:
        t_Oldpercent=20
    if n>2.5 and n<5:
        t_Oldpercent=5
    if n>2.5:
        t_Oldpercent=0
Oldtax=n*t_Oldpercent/100
print("Old Tax:",Oldtax)
diftax=tax-Oldtax
print("Difference in tax=",diftax)
#####



print("===================================")




#############################
# ELSE/IF/ELIF-USE IN FAMILY TOUR PLANNING DECISION
#####
print("0=NO AND 1=YES")
f= int (input (print("Mr ROY:"))) #Mr Roy ’s choice
m = int (input (print("Mrs Roy:"))) #Mrs Roy ’s choice
g = int (input (print("Mrs Roy's Mother:"))) #Mrs Roy ’s mother ’s choice
d = int (input (print("Daughter:"))) #Daughter ’s choice
#METHOD ONE
if f == 1 and m == 1:
    print("GO")
elif f==1 and m==1 and g==1:
    print("Go")
elif f == 1 and m == 1 and d == 1:
    print("GO")
elif m == 1 and d == 1 and g == 1:
    print("GO")
elif f==1 and d==1 and g==1:
    print("GO")
elif f == 1 and m == 1 and g == 1 and d == 1:
    print("GO")
else:
    print("0")
#METHOD TWO
if f==1 and m==1:
    print("GO")
else:
    if f==1 and m==1 and g==1:
        print("Go")
    else:
        if f==1 and m==1 and d==1:
            print("GO")
        else:
            if m==1 and d==1 and g==1:
                print("GO")
            else:
                if f==1 and d==1 and g==1:
                    print("GO")
                else:
                    if f==1 and m==1 and g==1 and d==1:
                        print("GO")
                    else:
                        print("0")

#####



print("===================================")




#############################
# PRINTING ALL THE NON-REPEATING SEQUENCE FORMED BY DIGITS-WAYS OF  NON REPEATING ARRANGEMENT
######
A=[1,2,3]
for i in A:
    print("i", i)
    for j in A:
        print("j", j)
        for k in A:
            print("k", k)
            if i!=j and j!=k and k!=i:
                print(i,j,k)
i=1
while i<=3:
    j=1
    while j<=3:
        k=1
        while k<=1:
            if i==j or j==k or k==i:
                continue
            else:
                print(i,j,k)
            k+=1
        j+=1
    i+=1
#####



print("===================================")




#############################
# PRINT SEQ OR SET LINE BY LINE
#####
#####



print("===================================")




#############################
# PRINT SEQ OR SET LINE BY LINE
#####
#####



print("===================================")




#############################
# PRINT SEQ OR SET LINE BY LINE
#####
#####



print("===================================")




#############################
# PRINT SEQ OR SET LINE BY LINE
#####
#####



print("===================================")




#############################
# PRINT SEQ OR SET LINE BY LINE
#####