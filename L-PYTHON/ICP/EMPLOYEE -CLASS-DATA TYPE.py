#    10/04/2020  #  15-April-2020
# CUSTOM EMPLOYEE -CLASS/DATA TYPE
#e1 = Employee("Employee Name", "Designation", "Dept", salary, dob, doe, email, phone, office, boss)
# print(e1) => ?
# we want the system to automatically assign an EmpID
# acccess and edit functions
#e1.setSalary(newval)
#e1.getSalary()


# Custom "Employee" class/data type

class Employee:
  # this function is called automatically
  # when you do x = Employee(...)
  def __init__(self, eName, eDesig, eDept, salary, yearOfBirth, yearJoined, email, phone, office, boss, add, tagline):
    self.employeeName = eName
    self.designation  = eDesig
    self.department   = eDept
    self.prevSalaries = []
    self.salary       = salary
    self.yearOfBirth  = yearOfBirth
    self.yearJoined   = yearJoined
    self.email        = email
    self.phone        = phone
    self.office       = office
    self.boss         = boss
    self.address      = add
    self.tagline      = tagline
  ##################################
  def getSalary(self):
      return self.salary
  #################################
  def setSalary(self, newSalary):
      self.prevSalaries.append(self.salary)
      self.salary = newSalary
    ##############################
  def __str__(self):    ######### \n\ TO CHANGE THE LINE
    return f"\n\
    =======================\n\
    1.Name:{self.employeeName}\n\
    2.Designation:{self.designation}\n\
    3.Department:{self.department}\n\
    4.Salary:{self.salary}\n\
    5.DOB:{self.yearOfBirth}\n\
    6.Date of Joined:{self.yearJoined}\n\
    7.Contact:{self.email}, {self.phone}\n\
    8.Office:{self.office}\n\
    9.Boss:{self.boss}\n\
    10.Address:{self.address}\n\
    11.Tagline:{self.tagline}\n\
    ==========================="

#############################
e1 = Employee("Manish Yadav", "Ashoka", "Student", 200000, 2000, 2020, "manish271208@gmail.com", None, "India", None, "Tulsipur","Hero of the world")
e1.phone=6393241779         # WE CAN FURTHER UPDATE ANY VALUE
print(e1) # e.__str__(e)


# we want the system to automatically assign an EmpID
# acccess and edit functions
#e1.setSalary(newval)
#e1.getSalary()
################################################33










print("+++++++++++===========================")















#################################################3
import random
class Employee:
  def __init__(self, eName, eDept, salary,eDesig, yearOfBirth, yearJoined, email, phone, office, boss, tagline):
    self.employeeName = eName
    self.department   = eDept
    self.designation  = eDesig
    self.prevSalaries = []
    self.salary       = salary
    self.yearOfBirth  = yearOfBirth
    self.yearJoined   = yearJoined
    self.email        = email
    self.phone        = phone
    self.office       = office
    self.boss         = boss
    self.tagline      = tagline
    ##############################
  for i in range(2):
      def __str__(self):  ######### \n\ TO CHANGE THE LINE
          return f"\n\
        =======================\n\
        1.Name:{self.employeeName}\n\
        2.Department:{self.department}\n\
        3.Salary:{self.salary}\n\
        4.Designation:{self.designation}\n\
        5.DOB:{self.yearOfBirth}\n\
        6.Date of Joined:{self.yearJoined}\n\
        7.Contact:{self.email}, {self.phone}\n\
        8.Office:{self.office}\n\
        9.Boss:{self.boss}\n\
        10.Tagline:{self.tagline}\n\
        ==========================="
#############################
e1 = Employee(None, None, 20000, "Ashoka University", None, 2020, None, None, "India", None,None)
#############################
def hasFriend():
    n=int(input(print("Enter Number of Employees:")))
    E = []
    for i in range(n):
        taglines = ["Good","Hero","Ranger","Human",  "Junior"]
        x = random.choice(taglines)
        e1.tagline = x
        E.append(x)
        Name = input(print("Enter Name:"))
        e1.employeeName = Name
        Department = input(print("Enter Department:"))
        e1.department = Department
        print(e1)
    for i in range(len(E)):
        if E.count(E[i])>=2:
            print(E[i])
    ##################################

hasFriend()