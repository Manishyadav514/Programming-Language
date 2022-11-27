#1/04/2020
# 0.) =>> see generateword.py
# 1. build "persons"
# 3. simulate!
# map: n
# 0,n....n,n
# 0,0 ...n,0
######
####################
#ADDING NUMBER IN AN ARRAY
####################
######
# METHOD 1
####################
A=[]
for i in range(0,10):
    A.append(i)
print("A=",A)
# METHOD 2
####################
B=[3*i for i in range(0,5)]    # WE CAN ALSO USE INSTEAD OF 3*i=3+i, 3i etc
print("B=",B)
def f(i):
    return 2*i
B1=[f(i) for i in range(0,5)]
print("B1=",B)












######
######################
#Fun: Generate random names (and learn how to make passwords!
######################
######
import random
import string
def GenerateWordOld(wordlength):
    box=string.ascii_letters   #ascii_lowercase
    w=''
    for i in range(0, wordlength):
        w=w+random.choice(box)
    return w
######################
def GenerateWord(wordlength):
    #box=string.ascii_letters   #ascii_lowercase
    box = string.ascii_letters+string.digits
    return ''.join( random.choice(box) for i in range(0, wordlength) )
    #return string.plus(random.choice(box) for i in range(0, wordlength))
    #return string+''.join(random.choice(box) for i in range(0, wordlength))
    #return [(random.choice(box) for i in range(0, wordlength))]
######################
def GenerateName(n):
    box = string.ascii_lowercase
    upper=string.ascii_uppercase
    s=random.choice(upper)
    return s+''.join(random.choice(box) for i in range(0,n))
######################
def GenerateNameNew1(n):
    return random.choice( string.ascii_uppercase) + ''.join( random.choice(string.ascii_lowercase) for i in range(1,n))
#######################
def GenerateNameNew2(n):
    box = string.ascii_lowercase
    s = random.choice(string.ascii_uppercase)
    return s + ''.join(random.choice(box) for i in range(0, n))
######################
w1=GenerateWordOld(12)
w2=GenerateWord(12)
w3=GenerateName(12)
w4=GenerateNameNew2(12)
print(w1,'\n',w2)
print(w3, w4, end='    Thanks')
#print(string.ascii_letters)
#print(string.digits)










#########
###################################
# 2. make the persons move around
##################################
########
import random
mapSize = 1000
class Person:
    idval = [0]  # inside an array, we have shared memory
    ########################
    def __init__(self, X=None, Y=None):
        if X is None:
            X = random.randint(0, mapSize)
        if Y is None:
            Y = random.randint(0, mapSize)
        self.x = X
        self.y = Y
        self.id = self.idval[0]
        self.idval[0] = self.idval[0] + 1
    #######################
    def moveRandom(self):
        X = random.randint(0, mapSize)
        Y = random.randint(0, mapSize)
    ######################
    def __str__(self):
        s = f"{self.id}'s home is located at x={self.x}, y={self.y}"
        return s
##########################
numPersons = 5
P = [Person() for i in range(0, numPersons)]
# print their home locations
for x in P:
    print(x)
for x in P:
    x.moveRandom()
