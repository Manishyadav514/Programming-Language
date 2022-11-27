import turtle                      # Drawing tool
import time                        # Used for functions related to time
import random                      # Used to generate random numbers/sequences
T = turtle.Turtle()                # Initiates turtle
T.hideturtle()                     # Hides turtle cursor
turtle.tracer(0, 0)
xzoom = 20
yzoom = 100
def display(A):
    x_shift = 1000         # Pixel or point to cover
    T.penup()             # To avoid a line at the start
    T.setpos(0 - x_shift, A[0] * yzoom)
    T.pendown()
    for i in range(len(A)):
        color = "red" if A[i] < A[i - 1] else "green"
        T.color(color)
        T.setpos((i * xzoom) - x_shift, A[i] * yzoom)
        T.dot(5)
    turtle.update()  # updates the screen with new graph
    time.sleep(0.1)  # timed delay
# x_new = r * x_old * (1-x_old)
def main():
    A = [0.5] * 60
    for i in range(1000):
        T.clear()
        display(A)
        x_old = A[-1]
        x_new = 3.99 * x_old * (1 - x_old)
        A.append(x_new)              # Adds an element/list to the end of a list
        A.pop(0)                     # Deletes the element at passed index (in this case, 0)
main()
turtle.update()
turtle.done()
