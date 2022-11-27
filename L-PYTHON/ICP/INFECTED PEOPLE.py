#3/04/2020
#INFECTED PEOPLE

import random
import math
mapSize = 100
maxDist = 10
infectionDist = 5
class Person:
    # location 0 holds the id counter
    # location 1 holds the number of people currently infected
    mem = [0, 0]  # inside an array, we have shared memory
    def __init__(self, X=None, Y=None):
        if X is None:
            X = random.randint(0, mapSize)
        if Y is None:
            Y = random.randint(0, mapSize)
        self.x = X
        self.y = Y
        self.homex = X
        self.homey = Y
        self.status = 2  # recovered=0, okay=2, infected=5
        self.id = self.mem[0]
        self.mem[0] = self.mem[0] + 1
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

    def infect(self):
        self.status = 5
        self.mem[1] = self.mem[1] + 1

    def __str__(self):
        s = f"{self.id} is located at x={self.x}, y={self.y}"
        return s
# code
def distanceBetween(A, B):
    return math.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)

def transmission(P):
    n = len(P)
    for i in range(0, n):
        for j in range(i + 1, n):
            d = distanceBetween(P[i], P[j])
            if d < infectionDist:
                # this is subtly wrong
                # if either one is infected, then both get infected
                # recovered=0, okay=2, infected=5
                if P[i].status + P[j].status > 6 and P[i].status + P[j].status < 10:
                    P[i].infect()
                    P[j].infect()

def countInfected(P):
    c = 0
    for x in P:
        if x.status == 5:
            c = c + 1
    return c

numPersons = 100
P = [Person() for i in range(0, numPersons)]

bad = random.choice(P)
bad.infect()

for day in range(50):
    # move each person to a new x,y
    for person in P:
        person.moveRandom()
    # check transmission
    transmission(P)
    # print how many people are infected
    print(f"On day {day}, the number of infected people is {P[0].mem[1]}")
# for x in P:
#  x.moveRandom()
