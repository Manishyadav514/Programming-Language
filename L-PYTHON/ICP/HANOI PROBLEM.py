# METHOD 1
def  hanoi(height, fromPole, toPole,withPole):
    if height>= 1:
        hanoi(height-1, fromPole, withPole,  toPole)
        print ("Move disk={} from {} to  {}.".format(height,fromPole, toPole))
        hanoi(height-1, withPole, toPole, fromPole)
hanoi(3, "A", "C", "B")

#METHOD 2...WRONG
def  hanoi(disks, fromPole, withPole, toPole):
    if disks == 1:
        print("Move disk 1 from {} to {}.".format(fromPole, toPole))
        return
    hanoi(disks , fromPole, toPole, withPole)
    print("Move disk {} from peg {} to peg {}.".format(disks,fromPole, toPole))
    hanoi(disks , withPole,fromPole,toPole)            # IT MOVES DISK FROM WP TO TP
disks = int(input("Enter number of disks:"))
hanoi(disks, "A", "B", "C")

# METHOD 3
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
height = int(input("Enter number of disks:"))
moveTower(height,"A","C","B")
