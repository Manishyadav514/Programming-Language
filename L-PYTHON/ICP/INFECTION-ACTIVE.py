import random
import math
mapSize = 200  # this is our world
maxDist = 10  # this is how far from home you can go
infectionDist = 7  # how close you need to be to get infected
numPersons = 100  # number of people in our world
numInfected = 5  # number of initial infections
class Person:
    # location 0 holds the id counter
    # location 1 holds the number of people currently infected
    # location 2 holds number of total infections (ever)
    mem = [0, 0, 0]  # inside an array, we have shared memory
    # these are helper functions
    def buildNextID(self):
        self.mem[0] = self.mem[0] + 1
        return self.mem[0]
    def increaseActiveInfections(self):
        self.mem[1] = self.mem[1] + 1
    def decreaseActiveInfections(self):
        self.mem[1] = self.mem[1] - 1
    def increaseTotalInfections(self):
        self.mem[2] = self.mem[2] + 1
    def __init__(self, X=None, Y=None):
        if X is None:
            X = random.randint(0, mapSize)
        if Y is None:
            Y = random.randint(0, mapSize)
        self.x = X
        self.y = Y
        self.homex = X
        self.homey = Y
        self.age = random.randint(5, 95)
        self.status = 2  # recovered=0, susceptible=2, infected=5
        self.timeToRecover = 0  # how many days you need to recover once infected
        self.id = self.buildNextID()
    # we assume this is called exactly once each day
    def moveRandom(self):
        # this person, "self" has a home location (homex, homey)
        # randomly move this person to a new location (x,y)
        # within distance maxDist from home
        temp = self.homex + random.randint(-maxDist, maxDist)
        if temp < 0:
            temp = 0
        if temp > mapSize:
            temp = mapSize
        self.x = temp
        temp = self.homey + random.randint(-maxDist, maxDist)
        if temp < 0:
            temp = 0
        if temp > mapSize:
            temp = mapSize
        self.y = temp
        if self.status == 5:
            # if I am infected
            self.timeToRecover = self.timeToRecover - 1
            if self.timeToRecover <= 0:
                self.status = 0  # now I am recovered!
                self.decreaseActiveInfections()  # we need to update number of active infections
    def infect(self):
        # if I am susceptible
        if self.status == 2:
            self.status = 5  # then "self" is infected
            self.increaseActiveInfections()  # number of active infections +1
            self.increaseTotalInfections()
            if self.age > 70:
                self.timeToRecover = 28
            elif self.age > 50:
                self.timeToRecover = 21
            else:
                self.timeToRecover = 14  # now you need 14 days to recover
    def __str__(self):
        s = f"{self.id} is located at x={self.x}, y={self.y}"
        return s
def distanceBetween(A, B):
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)
def transmission(P):
    n = len(P)
    for i in range(0, n):
        for j in range(i + 1, n):
            d = distanceBetween(P[i], P[j]) / infectionDist
            if d < 1:
                # this is subtly wrong
                # the smaller d is, the more likely infection should be
                r = random.random()  # this a number between 0 and 1
                if d < r:
                    # if either one is infected, then both get infected
                    # recovered=0, susceptible=2, infected=5
                    if P[i].status + P[j].status == 7:  # one infected, one susceptible
                        P[i].infect()
                        P[j].infect()
# first creating numPersons people
P = [Person() for i in range(0, numPersons)]
# initial infections
# we infect some random person
# TODO: start with numInfected people
# how do we do this?
# google "randomly choose some items from a list"
# random.sample(P, 5)
# then I just call .infect on each of these individually
bad = random.sample(P, numInfected)
for x in bad:
    x.infect()
for day in range(1, 50):
    # =============================================
    # this happens on each day
    # =============================================
    # move each person to a new x,y
    for person in P:
        person.moveRandom()
    # check if any two people spread the infection to each other
    transmission(P)
    # print how many people are infected
    print(f"Day {day}: {P[0].mem[1]} active infections")
    # =============================================
print(f"{P[0].mem[2]} total infections")
# for x in P:
#  x.moveRandom()










################################
###############################

import random
import math
mapSize = 200  # this is our world
maxDist = 10  # this is how far from home you can go
infectionDist = 7  # how close you need to be to get infected
numPersons = 100  # number of people in our world
numInfected = 5  # number of initial infections
class Person:
    # location 0 holds the id counter
    # location 1 holds the number of people currently infected
    # location 2 holds number of total infections (ever)
    mem = [0, 0, 0]  # inside an array, we have shared memory
    # these are helper functions
    def buildNextID(self):
        self.mem[0] = self.mem[0] + 1
        return self.mem[0]
    def increaseActiveInfections(self):
        self.mem[1] = self.mem[1] + 1
    def decreaseActiveInfections(self):
        self.mem[1] = self.mem[1] - 1
    def increaseTotalInfections(self):
        self.mem[2] = self.mem[2] + 1
    def __init__(self, X=None, Y=None):
        if X is None:
            X = random.randint(0, mapSize)
        if Y is None:
            Y = random.randint(0, mapSize)
        self.x = X
        self.y = Y
        self.homex = X
        self.homey = Y
        self.age = random.randint(5, 95)
        self.status = 2  # recovered=0, susceptible=2, infected=5
        self.timeToRecover = 0  # how many days you need to recover once infected
        self.id = self.buildNextID()
    # we assume this is called exactly once each day
    def moveRandom(self):
        # this person, "self" has a home location (homex, homey)
        # randomly move this person to a new location (x,y)
        # within distance maxDist from home
        temp = self.homex + random.randint(-maxDist, maxDist)
        if temp < 0:
            temp = 0
        if temp > mapSize:
            temp = mapSize
        self.x = temp
        temp = self.homey + random.randint(-maxDist, maxDist)
        if temp < 0:
            temp = 0
        if temp > mapSize:
            temp = mapSize
        self.y = temp
        if self.status == 5:
            # if I am infected
            self.timeToRecover = self.timeToRecover - 1
            if self.timeToRecover <= 0:
                self.status = 0  # now I am recovered!
                self.decreaseActiveInfections()  # we need to update number of active infections
    def infect(self):
        # if I am susceptible
        if self.status == 2:
            self.status = 5  # then "self" is infected
            self.increaseActiveInfections()  # number of active infections +1
            self.increaseTotalInfections()
            if self.age > 70:
                self.timeToRecover = 28
            elif self.age > 50:
                self.timeToRecover = 21
            else:
                self.timeToRecover = 14  # now you need 14 days to recover
    def __str__(self):
        s = f"{self.id} is located at x={self.x}, y={self.y}"
        return s
def distanceBetween(A, B):
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)
def transmission(P):
    n = len(P)
    for i in range(0, n):
        for j in range(i + 1, n):
            d = distanceBetween(P[i], P[j]) / infectionDist
            if d < 1:
                # this is subtly wrong
                # the smaller d is, the more likely infection should be
                r = random.random()  # this a number between 0 and 1
                if d < r:
                    # if either one is infected, then both get infected
                    # recovered=0, susceptible=2, infected=5
                    if P[i].status + P[j].status == 7:  # one infected, one susceptible
                        P[i].infect()
                        P[j].infect()
# first creating numPersons people
P = [Person() for i in range(0, numPersons)]
# initial infections
# we infect some random person
# TODO: start with numInfected people
# how do we do this?
# google "randomly choose some items from a list"
# random.sample(P, 5)
# then I just call .infect on each of these individually
bad = random.sample(P, numInfected)
for x in bad:
    x.infect()
for day in range(1, 50):
    # =============================================
    # this happens on each day
    # =============================================
    # move each person to a new x,y
    for person in P:
        person.moveRandom()
    # check if any two people spread the infection to each other
    transmission(P)
    # print how many people are infected
    print(f"Day {day}: {P[0].mem[1]} active infections")
    # =============================================
print(f"{P[0].mem[2]} total infections")
# for x in P:
#  x.moveRandom()
