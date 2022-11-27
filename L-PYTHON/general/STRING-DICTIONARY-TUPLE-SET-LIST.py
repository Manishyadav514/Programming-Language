# ++++++++++++ STRING-DICTIONARY-TUPLE-LIST ++++++++++++++++#







#############################
#######





print("===================================")






print("===================================")






#############################
# SET
#####
set={1,"MANISH",2,"DEEPAK",3,"CHANDAR"}          # 2
print("1.2:SET:",set)                           # SET IS NOT COLLABLE
set.remove("CHANDAR")
print("3.2:SET:CHANDAR IS REMOVED:",set)                  # tup.remove(30)
set.add( "CHANDAR")                                       # tup.add(30)   #    # set.add[2, 35]
print("4.2: CHANDAR ADDED:",set)
print("5.2(LEN SET):",len(set))
print("7.2:",{'nums'+'values'})
print("9.2:", set.pop())                                  #print("9.1:", tup.pop(1))
print("12.2:", sum({2,3,10}))
# print({'navin','kiran','john'}+{3,4})
s={"ram", "good"}
a={1,21}
print(s.update(a))
s.discard("ram")
s.remove((1))
print(s)
s.clear()
print(s)
# MATHEMATICL SET OPERATION
x={50,60,70,80}
y={60,7,1}
print(x.isdisjoint(y))
print(y.issubset(x))
print(x.issuperset(y))
print(x|y)                        # UNION
print(x>=y)                       # PRINT TRUE IF X IS SUPERSET OF Y
print(x<=y)                       # PRINT TRUE IF X IS SUBSET OF Y
print(x & y)                      # INTERSECTION
print(y-x)                        # DIFFERENCE
print(x^y)                        # SYMMETRIC DIFFERENCE
x|=y                              # UPDATE A TO A|B, lIKE THAT, x&=y, x^=y,x-=y
print(x)

# intersection of sets and sorting
n = input()
arr1 = set(map(int, input().split()))
n = input()
arr2 = set(map(int, input().split()))
arr3 = sorted((arr1.difference(arr2)).union(arr2.difference(arr1)))
for x in arr3:
    print(x)



#####



print("===================================")




#############################
#  TUPLE
####
tup = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10  # OR (1,2,3,4,5,6,7,8,9,10) # ONE ITEM, A=(10,)   AND ZER ITEM A=()
# x=([4,1,7],"ram") IT ALSO A TUPLE
print("1:TUP:", tup)
print("2(LEN TUP):", len(tup))
print(tup[1])                                            # CAN BE INDICES...
# tup[0]=12 SHOWS ERROR SINCE IT'S IMMUTABLE
print(tup[3:7])                                          # SLICED
print(tup.index(10))
print(max(tup), min(tup))
print(sum(tup), sorted(tup))
print(tuple(reversed(tup)))                              # REVERSED
print(tuple(tup[::-1]))                                  # REVERSED
n="MANISH"
print(*n)


print(tuple([1, 2]),tuple({10, 20}))                     # TUPLE FUNCTION-SET/LIST TO TUPLE
print(tuple((x,x**2) for x in range(5)))
print("3:", ('navin', 'kiran', 'john') + (10, 20))
print("4:", ('nums' + 'values'))
print("5:", sum(tup))

X=(10,20,30)
Y=(30,20,10)
a=(X,Y)
print(a[0][0])
print(2,X,3,Y)
print(2,*X,2)
# DISPOSABLE VARIABLES
tup1=(2,14,22,48,23)
x,_,_,_,y=tup1
i,*_,j=tup1                           # INTO SINGLE DISPOSABLE VARIABLES
print(x,y,_)
print(i,j,_)
#
lst=("a","b",("d"),"q")
for i in lst:
    if isinstance(i,tuple):
        print(i)
details = (("Manish", 19, "m"), ("Reena", 18, "f"))
for n, a, s in details:
    print(n,a,s)
######




print("===================================")





#############################
# PRINT SEQ OR SET LINE BY LINE
#####

#####



print("===================================")




#############################
# LIST
#####
list=[1,"MANISH",2,"DEEPAK",3,"CHANDAR"]
print("1.3:LIST",list)
print("2.3:list[1]",list[1])
list.remove("CHANDAR")
print("3.3:LIST: CHANDAR IS REMOVED", list)
list.append("CHANDAR")
print("4.3:CHANDAR APPENDED:",list)
print("5.3(LEN LIST):",len(list))
print("6.3:LIST ADDED:",[1,2]+[5,6])
print("7.3:",['nums'+'values'])
list.insert(2,77)
print("8.3: LIST insert(2,77):", list)         # print("8.2:",set.insert(2,77))        # print("8.1:",tup.insert(2,77))
print("9.3:", list.pop(2))                     # it removed number at index 2...pop() removed lastt element...leftpop() removed left
print(list)
del list[2:]
print("10.3: ", list)
list.extend([10,20,30])
print("11.3::", list)
#print("12.3:", sum(list))       #  max(list) # sum(list)
a=[2,4,1,5,2,10]
a.sort()                       # set.sort() tup.sort() ---NO SORT PERFORMED
print("13.3:", a)
del(list[2:4])                    # NOT del(set[2:4]) del(tup[2:4])
print("13.4:", list)
list[:]=[]                        # DELETE ELEMENTS ...NOT set[:]=[] tup[:]=[]
print("13.5", list)
list[0:3]=10,20,30,40
print("13.5",list)
del list
print("13.5",list)
#
x=["a","b","c"]
y=[9,10,11]
c=x+y
print("            ",c[0][0])
# SHALLOW COPY                        # CHANGING ONES VALUE CHANGES THE OTHER
lst1=[1,2,3]
lst2=lst1
lst1[1]=5
print("1", lst1, lst2)
# DEEP COPY                          # CHANGING ONES VALUE DOESN'T CHANGE THE OTHER
lst1=[1,2,3]
lst2=[]
lst2=lst2+lst1
lst1[1]=5
print("2", lst1, lst2)
# ADDING TWO MATRIX
m1=[[1,1,1],[2,2,2],[3,3,3]]
#print(len(m1))
#print(len(m1[0]))
#print(m1[1][2])
m2=[[3,3,3],[2,2,2],[3,3,3]]
m=       [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m[i][j]=m1[i][j]+m2[i][j]
print(m)
#####



print("===================================")




#############################
# COMPREHENSION
#####
# LIST
# a=[random.randint(10,20) for n in range(5)]
print("1.1:", [(x,x**2,x**3) for x in range(5)])
print("1.2:", [int(x) for x in ["10","2", "1" ]] )
print("1.3:", [n for n in range(5,10) if n%2!=0])
print("1.4:", [ n for n in range(15,35) if n<20 or n>30])
print("1.5:", [ "!" if alphabet in "aeiou" else alphabet for alphabet in "Techincal"])
print("1.6", [a+b for a in [1,2,3] for b in [3,2,1]])
print("1.7:", [[a+b for a in [1,2,3]] for b in [3,2,1]])
print("1.8:", [(i,j,k) for i in [1,2,3] for j in [1,2,3] for k in [1,2,3] if i!=j and j!=k and k!= i])
arr=[[1,2,3],[4,5,6]]
print("1.9:", [ n for ele in arr for n in ele] )
print("2.0:", [*arr[0],*arr[1]])
mat1,mat2=[[1,2,3,4],[5,6,7,8]],[[8,7,6,5],[4,3,2,1]]
print("2.1:",[[mat1[i][j]+mat2[i][j] for j in range(len(mat1[0])) for i in range(len(mat1))]])
lst=[(),10,(""),20,(1,2),3]
print("2.2:",[tpl for tpl in lst if tpl])                                            # TPL FUNCTION RETURNS TRUE IF TUPLE IS NOT EMPTY
s=' do dreams otherwise you will never fail'
print("2.3:",    ["".join(w.capitalize() for w in s.split())])
print("2.4:",    {"".join(alpha for alpha in k if alpha not in "aeiou"):v for (k,v) in d.items()})

# SET
print("2.5:", { x**3 for x in range(1,5)})
print("2.6:", { n for n in range(15,35) if n<20 or n>30})

# DICTIONARY COMPREHENSION
d={"x":1,"y":2,"z":3}
print("1.1:", {p:v*10 for (p,v) in d.items()})
print("1.2:", {k:("even" if v%2==0 else "odd") for (k,v) in d.items()})
print()
students={"A93":{"name":"manish", "phone":6393241779}, "B94":{"name":"krma", "phone":8787085500}}
print("1.3:",students["A93"]["name"])
print("1.4:",{ k:v for (k,v) in students.items() if k.startswith("A")})
print("1.5:",{k:v["name"] for (k,v) in students.items() if v["name"].startswith("m")})
#######




print("===================================")





