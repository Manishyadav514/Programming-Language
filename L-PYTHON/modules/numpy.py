from numpy import *


#CREATING DSEIRE NUMBER OF MATRIX
print("1:",sqrt(array([16,36,64,80])))
print("2:",array([10,20,30])+array([10,20,30]))             # adding two array
print("3:",array([16,36,64,80])+5)      # Adding single digit to whole array
print("4:",zeros(5))                           #ZEROS/ONES
print("5:",ones(5))                            # ONES
print("6:",arange(1,15,2))                    # ARRANGING ARRAY FROM1 TO 15 HAVING 2 GAP
print("7:",logspace(1,15,2))
print("8:",sin(array([16,36,64,80])))                    # GIVES SIGN VALUE OF ARRAY
arr1=array([16,36,64,80])
print("9:",arr1.dtype)                   # PRINT DATA TYPE INT/FLOAT
arr2=array([1,3,5],float)           # CHANGE ARRAY TYPE
print("10:",arr2.dtype)
print("11:",arr2)
arr2=array(arr2,int)
print("12:",concatenate([arr1,arr2]))     # THAT ALSO ADD ARRAY

# DEEP COPY
from numpy import *
arr1=array([10,20])
arr2=arr1.copy()
print(arr1)
arr1[1]=7
print(arr2)
print(id(arr1))
print(id(arr2))
# SHALLOW COPY
from numpy import *
arr1=array([10,20])
arr2=arr1.view()
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
######



print("===================================")




#############################
# MATRIX
#####
from numpy import *
arr=array([[1,2,3,8,5,6],[4,9,0,5,6,2]])
print("1:",arr.shape)
print("2:",matrix([[1,2,3,8,5,6],[4,9,0,5,6,2]]))
print("3:",matrix('1,2;4,5,;9,8'))
print("4:ARRAY SIZE=", arr.size)                          #SIZE-GIVES TOTAL ELMENT OF BOTH
print("5:",matrix('1,4;4,5,')*matrix('1,4;4,5,'))
print("6:", arr.flatten())            # FLATTEN-PRINT TWO ARRAYS IN SINGLE
print("7:", arr.reshape(3,4))         # MATRIX OF THREE ROW AND FOUR COLOUMN
print("8:", arr.reshape(2,2,3))       # TWO MATRIX EAXH WITH TWO ROW AND THREE COLOUMN
