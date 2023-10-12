1
class PowerCalculatorz :
    def __init__(self) :
        pass
    def calculator_power(self,x,n):
        self.x = x
        self.n = n 
        result = pow(self.x,self.n)
        return round(result,3)
obj = PowerCalculatorz()
x = float(input("Enter the base (x):\n"))
n = int(input("Enter the exponent (n):\n"))
print(str(float(x))+"^"+str(int(n)),"=",obj.calculator_power(x,n)) 


# 2
# class Rectangle :
#     def area(self,width,height):
#         self.area = width * height
#         return self.area
#     def para(self,width,height):
#         self.para = (2*width)+(2*height)
#         return self.para
# w = int(input("Give a width:\n"))
# l = int(input("Give a height:\n"))
# obj = Rectangle()
# print("Area:",obj.area(w,l))
# print("Perimeter:",obj.para(w,l))

# 3
# class Student :
#     def avg(self,name,grade) :
#         self.n = name
#         self.g = grade
#         total = 0
#         for i in self.g :
#             total+=i
#         return total/len(s)
# obj = Student()
# n = input("Name of student:\n")
# s = [int(e) for e in input("Enter the grade with space:").split()]
# print()
# print("Average Grade:",obj.avg(n,s))

# 4.
# class  Student :
#     def name(self,student_name):
#         self.n = student_name
#         return self.n
#     def marks(self,marks):
#         self.m = marks
#         return float(self.m)
#     def newn(self,nn):
#         self.n = nn
#         return self.n
#     def newm(self,nm) :  
#         self.m = nm
#         return float(self.m) 
# obj = Student()
    
# n = input("Enter student name:\n")
# m = int(input("Enter student marks:\n"))
# print("Original Student Name:",obj.name(n))
# print("Original Marks:",obj.marks(m))
# nn =input("Enter new student name:\n")
# nm =int(input("Enter new student marks:\n"))
# print("Modified Student Name:",obj.newn(nn))
# print("Modified Marks:",obj.newm(nm))


# 5
# class Library :
#     def check(self,book) :
#           result = ""
#           for i in lis :
#                 j = i+", "
#                 result+=j
#           return result[0:-2]          
    
# obj = Library()
# name = input("Give a library name:\n")
# count = int(input("How many book you neet to add:\n"))
# lis = []
# for i in range(count):
#         need = input("Name of book:\n")
#         lis.append(need) 
# print("Books in",name,"Library:",obj.check(count))