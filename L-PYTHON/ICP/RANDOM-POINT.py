import turtle
T = turtle.Turtle()
T.hideturtle()                # Hiding Turtle
# turtle.tracer(0,0)          # To direct print line and point without the line movement.
xzoom = 5                    # X AXIS GAP BETWEEN TWO  POINTS
yzoom = 2                     # Y axis length
def display(A):
    T.penup()                 # To avoid a line at the start
    T.setpos(0,A[0]*yzoom)    # It fixes the turtle position x=0 and y=first digit in array*yzoom length
    T.pendown()               # To draw the line
    for i in range(len(A)):
        T.setpos(i*xzoom,A[i]*yzoom)
        T.dot(10,"red") if i%2==0 else T.dot(10,"blue")
def main():
    A = [10,1,20,2,30,3,40,4,50,5,60,6,70,7,80,8]
    display(A)
    turtle.update()
    A.reverse()      # Swamping the first two value of array
    T.clear()                # To clear what we have drawn before.
    display(A)
    turtle.update()
main()
#turtle.update()
turtle.done()
