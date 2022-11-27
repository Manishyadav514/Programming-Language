# capitalizing a string
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

# day of the date
import calendar
def Day_Name(d,m,y):
    day = calendar.day_name[calendar.weekday(y,m,d)]
    print(day.upper())
Day_Name(7,1,2021)




#remove, discar, pop
#remove, discar, pop
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split() + ['']))
print(sum(s))
import sys
def fun(s, arr):
    for x in arr:
        if x[:1] == 'p':
            s.pop()
        elif x[:1] == 'd':
            s.discard(x[-1])
        elif x[:1] == 'r':
            if x[1] in s:
                s.remove(x[-1])
    print(sum(s))

n = int(input())
s = set(map(int, input().split()))
n = int(input())
arr = sys.stdin.readlines()
fun(s, arr)

n = input()
s = set(map(int, raw_input().split()))
m = int(raw_input())
for i in xrange(m):
    p = raw_input().split()
    if p[0] == "remove":
        s.remove(int(p[1]))
    elif p[0] == "discard":
        s.discard(int(p[1]))
    else:
        s.pop()
print
sum(list(s))




#n = int(input())
#s = set(map(int, input().split()))
s = set([1, 2, 3, 4 ,5, 6, 7, 8, 9])
arr = [['pop'], ['remove', 9],['discard', 9],['discard', 8],['remove', 7],['pop'],['discard', 6],['remove', 5],['pop'],['discard', 5]]
#for i in range(int(input())):
#    arr.append(list( map(str, input().split())))
fun(s, arr)












# getting the avergae of particular student from the dictionary
def Av_Marks_Student(arr):
    print("{:.2f}".format(sum(arr)/len(arr)))
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    arr = student_marks[query_name]
    Av_Marks_Student(arr)



# Alphabet Rangoli
def print_rangoli(size):
    x = ""
    y = ""
    for i in range((size-1)+1):
        print(x.rjust((size - 1) * 2, "-") + chr(97 + size-1-i) + (y.ljust((size - 1) * 2, "-")))
        x = x + str(chr(97 + size - i - 1)) + "-"
        y = "-" + str(chr(97 + size - i - 1)) + y
    x = x.replace(('a'+"-"), "")
    y = y.replace(("-"+"a"), "")
    for i in range((size-1)):
        x = x.replace((str(chr(97 + i + 1)) + "-"), "")
        y = y.replace(("-" + str(chr(97 + i+1))), "")
        print(x.rjust((size - 1) * 2, "-") + chr(97 + i +1) + y.ljust((size - 1) * 2, "-"))
print_rangoli(10)


################################### Second Highest Element
def Second_Highest(arr):
    a = max(arr)
    b = arr.count(max(arr))
    for i in range(b):
        arr.remove(a)
    print("Second Highest Element :", max(arr))
Second_Highest([2,3,4,5,5])

###################### HackerRank Logo
def HackerRank_logo(thickness):
    c = 'H'
    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))
    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
HackerRank_logo(5)

######################### string formatting
def print_formatted(number):
    binary = bin(number)[2:]
    n = len(binary)
    for i in range(1, number+1):
        print(str(i).rjust(n," "), str(oct(i)[2:]).rjust(n," "), str(hex(i).upper()[2:]).rjust(n, " "), str(bin(i)[2:]).rjust(n, " "))
print_formatted(17)



# happiness
n,m = map(int, input().split())
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
i = 0
for x in array:
    if a.__contains__(x):
        i = i +1
        print(i)
    elif b.__contains__(x):
        i = i-1
        print(i)
    else:
        continue
print(i)

n, m = input().split()
sc_ar = input().split()
A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))
