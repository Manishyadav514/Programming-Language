# ++++++++++++ PYTHON TOOLS ++++++++++++++++#





#############################
# CONSOLE INPUT/ CONSOLE OUTPPUT-INPUT BY KEYBOARD AND OUTPUT ON THE SCREEN
#####
# x,y,z=input("Enter three digits:").split()
# print(x, y, z)
# scores=[int(n) for n in input("Enter value").split()]              # IT CREATES  A LIST OF SCORES
# print(scores, sep=",", end="!")
# FORMATTED PRINTING
# 1...USING FORMATTED STRING LITERAL
#
R,B,H=1.233234234,90,120
print(f'1: radius={R}  breadth={B} Height={H}')
#   NB
n='man dhan tan yadav'
for x in n.split():
    print(f'{x:10}')
# 2...FORMAT(0) METHOD OF STRING OBJECT
name, age, gender="Manish", 19, "m"
print('2:''name={}, age={}, gender={}'.format(name, age, gender))
print('3:''name={2}, age={0}, gender={1}'.format(age, gender, name))
print('name={0:10} gender={0:5}'.format(name, gender))
print("radius={0:2.2f}".format(R))
#####




print("===================================")





#############################
# DECISION CONTROL INSTRUCTION
#####
a=40
b=30
print("1.1:", 75 and a>=20 and b<=60 and 35, -30 and a>=20 and b< 15 and 35, -30 and a>=20 and 0 and 35)
print("1.2:", 75 or a>=20 or 75, a<20 or 0 or 35)
print("1.3:", not (a<=b))
x=10
print("1.4:", "Biger than 5" if x>=5 else "Lower than 2" if x<=2 else 'GOOD')
#print("1.5:", 'true' if any(a,b,c,d))
########







print("===================================")





#############################
# REPEATITION CONTROL INSTRUCTION
#####
for i, ele in enumerate([10,20,30]):
    print(i, ele)
for i in range(5,10,2):
#for i in range(20, 5, -2):
    print(i, end=",,")
# INFINITE LOOP
i=1
while 1:
# while True:
    print(i)
    i+=1
    if i>10:
        break
a=1
b=2
c=3
for x in "abc":
    print(x)
import math
length=10
precision=3
for n in range(1,10):
    a=math.sqrt(n)
    b=math.pow(n,1/3)
    print(f'{n:10}{a:{length}.{precision}}{b:{length}.{precision}}')

# MULTIPLE STRING
student=10
qulified=5
print(f'\n{"STUDENT:":<1}{student:<10}',
      f'\n{"qulified:":<10}{qulified:<10}')

details={"Manish":6393241779, "Deepak": 8787085500, "Saloni":7081289995}
for name, mono in details.items():
    print(f"{name:10}:{mono:20}")
#####



print("===================================")



#############################
# ARGUMENTS IN PYTHON FUNCTION
#####
# 1.0:  POSITIONAL/ REQUIRED ARGUMENTS
def p(i,j,k):
    print(i*j, k.upper())
print("1.0:", p(1,2,"manish"))                                   # MUST BE IN THE ORDER AS PERFORM ACTION
# 1.1:  KEYWORD ARGUMENT
def person(name,age):
    return age-6,name
print("1.2:", person(age=10,name='navin' ))                      # NO MATTER SEQUENCE, VARIABLES ARE DEFINED
# 1.0 and 1.1 can be used together
def person(i, int, str):
    return i, int, str
print("1.2:", person(10, int=10,  str="mhgfds" ))                    # 1.0 MUST PRECEDE 1.1
# 1.3.VARIABLE LENGTH POSITIONAL ARGUMENT
def add(a,*b):                                                       # *b means it can have multiple value
    c=a
    for i in b:
        c=c+i
    return c
print("1.3:", add(10,20,300,300))
# 1.4: VARIABLE LEANGTH KEYWORD ARGUMENT
#####
def person(name,**data):                                             # **b means it can have multiple keyword ardument
    return name, data
print("2.1", person('manish',age=19,sex='male') )                    #having keyword
#dic={"name":"manish", "data":"not available"}
#print(**dic)
# COMINING ALL
def all(i,j,*args,x,y,**kwargs):
    print(i,j)
    for var in  args:
        print(var,end=",")
    print(x.y)
    for name, value in kwargs.items():
        print(name,value,end=",")
print(10,20,100,200)
# DEFAULT VALUE.,6' ALREADY RECALLED IN FUNCTION
def person(name,age=18):
    return name,age-6
print("1.2:", person(name='navin' ))                            #PUTTING AGE WILL OVERWRITE ASSIGNED VALUE
# PANGRAM CHECKING
def ispangram(s):
    aplhaset={"abcdefghijklmnopqrstuwxyz"}
    return aplhaset<=set(s.lower())
print(ispangram(" The quick brown fox jumps over the lazy dog"))
# SORTING HYPHON SEPERATED SEQUENCE
def sorting_hyphon(s1):
    item=[s for s in s1.split("-")]
    item.sort()
    s2="__".join(item)
    return s2
print("", sorting_hyphon("manish-deepak-salman-"))
# CHECKING PALINDROME
def ispalindrome(s):
      t=s.lower()                                 # IMMUTABLE STRING COLLECTED TO ANOTHER VARIABLE
      left=0
      right=len(t)-1
      while right>=left:
          if t[left]!=t[right]:
              return False
          if t[right]=='':
              right-=1
          if t[left]=='':
              left+=1
          left+=1
          right-=1
          return True
print(ispalindrome("rats live on no eviln star"))
# REMOVING DUPLICATE ITEMS
def removing_duplicate(s):
    t=[ele for ele in s.split(" ") ]
    return " ".join(sorted(list(set(t))))
print(removing_duplicate(" ram is is good , good as it was never expected"))
# COUNTING THE FREQUENCY OF WORD
def frequency(s):
    freq={}
    for word in s.split():
        freq[word]=freq.get(word,0)+11
    return freq
print(frequency("is he, what you think he is ?"))
# CREATING SENTENCES
def creatre_sentence(a,b,c):
    return [(x+""+y+" "+z) for x in a for y in b for z in c]
print(creatre_sentence(["Ram","Shyam"],["reads","plays"],["books","nothing"]))
########
# RECURSION
def prime_factor(n):
    i=2
    while i<=n:
        if n%i==0:
            print(i)
            n=n//i
        else:
            i+=1
prime_factor(17)
#########






print("===================================")





#############################
# FUNCTIONAL PROGRAMING
#####
def prime_factor(n):
    i=2
    while i<=n:
        if n%i==0:
            print(i)
            n=n//i
        else:
            i+=1
prime_factor(17)
def add(x,y,f):
    print(x+y)
    f()
def fun():
    print('Hey')
f=fun
a=add                        # ASSIGNING A FUNCTION TO VARIABLE
a(1,2,f)                  # PASSING FUNCTION AS ARGUMENT TO A FUNCTION

# LAMBDA FUNCTION
print((lambda s:s.lstrip().rstrip().upper())("Manish"))
print((lambda s:s*s*s)(10))
lst=[2,4,6]
p=lambda l:sum(l)
print((p)(lst))
# HIGH ORDER FUNCTIONS
# 1.1 MAP
import math
print(list(map(math.factorial, lst)))
# FILTER
def filt(n):
    if n%5==0:
        return True
    else:
        return False
l=[10,22,30,2]
lt=['A','B',2,3]
print(list(filter(filt,l)))
# print(list(filter(str.isalpha,lt)) )
# REDUCE
from functools import reduce
b=[4,8,9,10]
def getsum(x,y):
    return x+y
print(reduce(getsum,b))
# USE IN ONE FUNCTION
print(reduce( lambda x,y:x+y,b))             # INT OBJECT IS NOT ITRERABLE
print(list(filter(lambda n:n%5==0,b)))
print(list(filter(lambda n:n%5==0,b)))
print("1.2", list(filter(lambda n:n>10, map(lambda n:n*n*n,b) )))
c=[1,2,3]
d=[3,2,1]
print(list(map(lambda n1,n2:n1+n2,c,d)))
######





print("===================================")





#############################
# LOCAL AND GLOBAL VARIABLE
#####
a=10              #GLOBAL VARIABLE-work as outer
def something():
    a=3          #LOCAL VARIABLE-of function
    return a
print("1.1:", a)
print("1.2:", something())
#
a=10
def something():
    global a   # NO LOCAL VARIABLE- GLOBAL BECOMES LOCAL it work without writing
    a=20
    return a
print("2.1:", something())
print("2.2:", a)
# 1.3 CHANGING GLOBAL VARIABLE WITHOUT EFFECTING INNER VARIABLE
a=10
def man():
    a=12
    x=globals()['a']
    return x
    globals()['a']=1
print("3.1:", man())
print("3.2:", a)
#
a=10
def update(x):
    print(id(x))
    x=8
    return id(x), x
print("4.1:", update(a))
print("4.2:", id(a),a)
#
def update(lst):
    lst[1]=25
    return id(lst), lst
lst=[10,20,30]
print("5.1:", id(lst))
print("5.2:", update(lst))
#######




print("===================================")




#############################
# CLASS and OOPS CONCEPT
#####
# COSTRUCTOR= define the memory of the class
class computer:
    pass
c=computer()     #COMPUTER ARE CONSTRUCTOR
c1=computer()    # contructor decide the memory of that class
print("1.1:", id(c))
print("1.2:", id(c1))
#####
class computer:
    def config(self):
        print("15gb,i3,8")
com=computer
print("2.1:", com)
print("2.2:", type(com))
computer.config(com)
######
class compuetr:
    pass             # nothing print so use pass
com=compuetr
print("3.1:", id(com))
print("3.2:", com)
# __init__(self)
# 1.
class computer:
    def __init__(self):
        print("4.1:", "in init")
    def config(self):
        print("4.2:", "i5,16gb,1TB")
com1=computer()
com2=computer()
com1.config()
com2.config()
# 2.
class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram      #value we passed assigned to those object
    def config(self):
        print("5.1: confif is:", self.cpu, self.ram)    # WE PASSING SELF TO USE IT FETCH THE VALUE
com1=computer('i5',16)
com2=computer('Man',8)
com1.config()
com2.config()
#####



print("===================================")



#######################
# 3. HOW TO CREATE A VARIABLE IN OBJECT
#####
class computer:
    def __init__(self,name,age):
        self.NAME=name
        self.AGE=age                     #value we passed assigned to those object
    def update(self):
        self.AGE=30
    def compare(self, other):
        if self.AGE==other.AGE:
            return "They are of the same age:"
        else:
             return False
c1=computer("MANISH",20)                            # changing age will not print same REMOVE IT(SAME AGE)
c2=computer("RAHUL",20)
print("1.1:", c1.compare(c2))
print("1.2:", c1.NAME)
print("1.3:", c2.NAME)
#####




print("===================================")




#############################
# 4.HOW TO CHANGE VARIABLE WITHOUT EFFECTING OTHER
#####
class car:
    def __init__(self):
        self.mil=10
        self.com="Tyota"
c1=car()
c2=car()
c1.mil=15          #TO CHANGE MILAGE
c2.com="BMW"       #TO CHANGE COMPANY
print("1:", c1.mil, c1.com)
print("2:", c2.mil,c2.com)
# 5.CHANGING VARIABLE EFFECTING WITH OTHER(INSTANCE AND CLASS VARIABLES)
########
class car:
    wheel=4                         # CLASS VARIABLE DEFINED OUSIDE __INIT__
    def __init__(self):
        self.mil=10                 #BOTH ARE INSTANCE VARIABLE
        self.com="Tyota"
c1=car()
c2=car()
c1.mil=15                           #TO CHANGE MILAGE
c2.com="BMW"                        #TO CHANGE COMPANY
car.wheel=5                         #WE HAVE TO USE CLASS(car) BECAUSE THAT IS CLASS VARIABLE IT EFFECTS BOTH
print("3:", c1.mil, c1.com, c1.wheel)
print("4:", c2.mil,c2.com, c2.wheel)
#####



print("===================================")




#####################
# 7.error====CLASS INSIDE THE CLASS
#####
class student:
    def __init__(self,name, rollno,):
        self.n=name
        self.r=rollno
        self.l=self.laptop()
    def show(self):
        print(self.n, self.r)
        self.l.show()
    class laptop:
        def __init__(self):
            self.brand="hp"
            self.pro='i5'
            self.sto=8
        def show(self):
            print(self.brand,self.pro,self.sto)

s1=student("MANISH",19)
s1.show()
#####



print("===================================")



#############################
# 6. SET/GET==ACCESSOR/MUTATOR
#####
class student:
    school="JNV"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+ self.m2+ self.m3)/3
    def total_avg(self,*b):
        return (self.m1+ self.m2+ self.m3)/3+s2.avg()
    def get_m1(self):                           #GETTER; FETCH THE VALUE=ACCESSOR
        return self.m1
    def set_m1(self):                           #SETTER:CHANGE THE VALUE=MUTATOR
        return self.m1
s1= student(15,15,60)
s2= student(30,30,30)
#s3= student(50,30,10)     #It should be corrected
print(s1.avg())
print(s1.total_avg(s2,s3))
#####



print("===================================")




#############################
# PRINT SEQ OR SET LINE BY LINE
#####
#####



print("===================================")

















