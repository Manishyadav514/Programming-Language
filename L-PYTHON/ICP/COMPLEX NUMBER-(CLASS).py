#27/03/2020
#init_()  / CLASS
import math
class Complex:
    # stuff defined here is shared (weird, right??)
    # try this with an array and see
    def __init__(self, realIn=0, imaginaryIn=0):
        if isinstance(realIn, Complex):
            realIn = realIn.real
            imaginaryIn = realIn.imaginary
        # this is specific to each instance
        self.real = realIn
        self.imaginary = imaginaryIn
    # ====================
    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        # you reach this point only in the else condition
        return f"{self.real} + {self.imaginary}i"
    # ====================
    def __repr__(self):  # don't worry about this rn
        return str(self)
    # ====================
    def __add__(self, other):
        # just in case other is not a complex number
        if isinstance(other, (int, float)):
            other = Complex(other, 0)
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return Complex(r, i)
    # ====================
    def __sub__(self, other):
        # just in case other is not a complex number
        if isinstance(other, (int, float)):
            other = Complex(other, 0)
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return Complex(r, i)
    # ====================
    def __mul__(self, other):
        # just in case other is not a complex number
        if isinstance(other, (int, float)):
            other = Complex(other, 0)
        # (a+ib+jc+kd)(e+if+jg+kh) = (ae -bf-gc-dh) + i(af -be)+j(ec+ag)+k(de+ah)+ij(bc+\=)+ik()+jk()
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.imaginary * other.real + self.real * other.imaginary
        return Complex(r, i)
    # ====================
    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)
c1 = Complex(3, 4)  # 3 + 4i
print(c1)
print([c1])
print(f"c1={c1}")  # print tells c1: what do you look like as a string??
c2 = Complex(5, -7)  # 5 - 7i ==> naively, you'll print 5 + -7i
print(f"c2={c2}")
c3 = (c1 + c2) * (c1 + 5)  # c1+c2 => +(c1, c2) => c1.__add__(self, c2)
# c3 = mult( add(c1, c2), add(c1, complexify(5,0))))))))))))
print(f"c3 = {c3}")
######################################







print("===================================SUPER-COMPLEX-NUMBER")






############################################3
# SCN
import math
class Complex:
    def __init__(self, realIn=0, imaginaryIn=0, imaginaryIn2=0, imaginaryIn3=0,):
        if isinstance(realIn, Complex):
            realIn = realIn.real
            imaginaryIn = realIn.imaginary
            imaginaryIn2 = realIn.imaginary2
            imaginaryIn3 = realIn.imaginary3
        # this is specific to each instance
        self.real = realIn
        self.imaginary = imaginaryIn
        self.imaginary2 = imaginaryIn2
        self.imaginary3 = imaginaryIn3

    ###############  CREATING STRING OF SCN-5.1(A)
    def __str__(self):
        # IN CASE ANY REAL OR IMAGINARY PART ARE NEGATIVE
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i+ {self.imaginary2}j+ {self.imaginary3}k"
        elif self.imaginary2 < 0:
            return f"{self.real} + {self.imaginary}i- {-self.imaginary2}j+ {self.imaginary3}k"
        elif self.imaginary3 < 0:
            return f"{self.real} + {self.imaginary}i+ {self.imaginary2}j- {-self.imaginary3}k"
        # IT WILL RUN ON ELSE CONDITION SO IF NO PARTS ARE NEGATIVE THEN IT WILL PRINT POSITIVE VALUES
        return f"{self.real} + {self.imaginary}i + {self.imaginary2}j + {self.imaginary3}k"
    ######################################
    def __repr__(self):
        return str(self)

    ################ "B ADD"-FUNCTION TO ADD TWO GIVEN SCN-5.1(B)
    def __add__(self, other):
        # just in case other is not a complex number
        if isinstance(other, (int, float)):
            other = Complex(other, 0)
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        j = self.imaginary2 + other.imaginary2
        k = self.imaginary3 + other.imaginary3
        return Complex(r, i,j,k)

    ##############- FUNCTION TO MULTIPLY TWO SCN-5(C)
    def __mul__(self, other):
        # just in case other is not a complex number
        if isinstance(other, (int, float)):
            other = Complex(other, 0)
        # ON MULTIPLYING TWO GIVEN SCN, WE GET:
        # (a+ib+jc+kd)(e+if+jg+kh) = (ae -bf)+i(be+af+cg)+j(ag+ce+dh)+k(de+ah)+ij(cf+bg)+ik(df+bh)+jk(dg+ch)
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.imaginary * other.real + self.real * other.imaginary + self.imaginary2 * other.imaginary2
        j = self.real * other.imaginary2 + self.imaginary2 * other.real+self.imaginary3*other.imaginary3
        k = self.imaginary3 * other.real + self.real * other.imaginary3 + self.real * other.imaginary
        ij=self.imaginary2*other.imaginary + self.imaginary*other.imaginary2
        ik=self.imaginary3*other.imaginary + self.imaginary*other.imaginary3
        jk=self.imaginary3*other.imaginary2 + self.imaginary2*other.imaginary3
        # Now, this multiplied complex number will have seven parts (r,i,j,k,ij,k,jk) for which complex number should be modified.
        # I tried but got failure in printing other parts. But if the complex number is considered for only four parts (r,i,j,k), it gives appropriate answer for them.
        return Complex(r, i,j,k)
    ###########################################
c1 = Complex(2,1,1,1)
c2 = Complex(2,1,1,1)
print(c1)
print(c2)
c3=c1+c2
print("Sum (c1+c2):",c3)
c4=c1*c2
print("Multiply (c1*c2):",c4)

