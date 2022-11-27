import sys

# SETRECURSSION/GETRECURSSION- INCREASE LIMIT OF WRITING WORD
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=1
def fun():
    global i
    i+=1
    print("hello", i)
    fun()
fun()
