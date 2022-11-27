# LIST / ARRAY






#############################
# SOME WORK PERFORMED IN ARRAY
#####
from array import *                                     # ARRAY IMPORTED
arr = array("i",[10,20,-30,23])                          # ‘i’,(+/-) both can be use but in case ‘I’ used then only +ve
arr.remove(10)
print("1:",  arr)                                       # REMOVE SELECTED ELEMENT FROM ARRAY
arr.reverse()
print("2:",arr)
print("3:occurence:",  arr.count(10))                   # NUMBER OF RECURRENCE OF X
print("4:ADDRESS & SIZE:",  arr.buffer_info())          # shows address and size of -BUFFER_INFO ()
arr.append(100)
print("5:",arr)                                         # ADD A NEW DIGIT IN END OF ARRAY
arr.reverse()
print("6:",arr)                                         # reversing array's value
print("7:NO OF INDEX 0:",arr[0])                        # PRINT ONE VALUE FROM ARRAY BY USING INDEX NO.
print("8:TYPE:",array.typecode)                         #shows type of array-“TYPECODE”
print("9:",array("i",[1,23])+array("i",[9,7]))          # MIXING TWO ARRAYS
print("10:",sum(array("i",[1,23])+array("i",[9,7])))           # SUM OF ALL THE DIGIT IN ARRAY
newArr=array(arr.typecode, (a*a for a in arr))         #  CHANGING ARRAY INTO NEW ARRAY
print("11",  newArr)
print("12:", arr.itemsize)

#array.pop([i])
#print("13:", arr.byteswap())
#####




print("===================================")





#############################
# CHECK WHETHER ALL ELEMENTS OF THE ARRAY ARE SAME OR NOT
#######
def check(A):
    #return all(i==A[0] for i in len(A))
    return len(list(A))<=1
    #return A.count(A[0])==len(A)
    #return A and [A[0]] * len(A) == A
    #return A[1:]==A[-1:]
print("1.1:", check([1,1,1]))
print("1.2:", check([1,2,1]))
print("1.3:", check(["a","b","c"]))
######





print("===================================")






#############################
# FILTER
#####
# 1 EVEN
def is_even(n):
     return n%2==0
nums=[2,3,4,4,5,5]
print("1:", list(filter(is_even, nums)))

# 1 .ODD
def is_odd(n):
     return n%2!=0
nums=[2,3,4,4,5,5]
print("2:",  list(filter(is_odd, nums)))

#  3 .DOUBLE WITH EVEN
nums=[2,3,4,5,6,7,8,9]
c=list(filter(lambda n:n%2==0,nums))
doubles=map(lambda n:2*n,nums)
print("3:", c)

#COUNTING EVEN ODD NUMBER IN LST
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst={10,20,3,4,5}
even,odd =count(lst)
print(even)
print(odd)
#####



print("===================================")




#############################
# CHECK WHETHER ALL ELEMENTS OF THE ARRAY ARE SAME OR NOT
#######
#####



print("===================================")




#############################
# CHECK WHETHER ALL ELEMENTS OF THE ARRAY ARE SAME OR NOT
#######
#####



print("===================================")




#############################
# CHECK WHETHER ALL ELEMENTS OF THE ARRAY ARE SAME OR NOT
#######


#array.byteswap(),array.frombytes(s).,array.fromfile(f, n),array.fromlist(list),array.fromstring(),array.fromunicode(s)
#Use array.frombytes(unicodestring.encode(enc)) to append Unicode data to an array of some other type.array.index(x)
#Return the smallest i such that i is the index of the first occurrence of x in the array.array.insert(i, x)
#Insert a new item with value x in the array before position i. Negative values are treated as being relative to the end of the array.

#Removes the item with the index i from the array and returns it. The optional argument defaults to -1, so that by default the last item is removed and returned.
#array.tobytes()
#Convert the array to an array of machine values and return the bytes representation (the same sequence of bytes that would be written to a file by the tofile() method.)New in version 3.2: tostring() is renamed to tobytes() for clarity.array.tofile(f)
#rite all items (as machine values) to the file object f.
#array.tolist()
#Convert the array to an ordinary list with the same items.
#array.tostring()
#Deprecated alias for tobytes().
#Deprecated since version 3.2, will be removed in version 3.9.
#array.tounicode()
#Convert the array to a unicode string. The array must be a type 'u' array; otherwise a ValueError is raised. Use array.tobytes().decode(enc) to obtain a unicode string from an array of some other type.



