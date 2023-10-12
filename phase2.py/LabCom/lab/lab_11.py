# 1
# class Vehicle :
#     def __init__(self,name,speed,mileage) :
#             self.n = name
#             self.s = speed
#             self.m = mileage
        
# class Bus(Vehicle):
#     def __init__(self, name, speed, mileage):
#         super().__init__(name, speed, mileage)
#     def namea(self):
#          return self.n
#     def speeda(self):
#          return self.s
#     def milea(self):
#          return self.m
# n = input("Enter the bus name:\n")
# s = float(input("Enter the maximum speed of the bus:\n"))
# m = float(input("Enter the mileage of the bus:\n"))
# obj = Bus(n,s,m)
# print("Vehicle Name:",obj.namea(),"Speed:",obj.speeda(),"Mileage:",obj.milea())

# 2
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)

# print(type(School_bus))
# print(isinstance(School_bus, Vehicle))

# 3
# capa = int(input("Enter the seating capacity of the bus:\n"))
# class Vehicle :
#     def __init__(self,name,speed,mile):
#         self.n = name
#         self.s = speed
#         self.m = mile
# class Bus(Vehicle):
#     def __init__(self, name, speed, mile,*capa):
#         super().__init__(name, speed, mile)
#     def capa(self):
#         if capa == "":
#             return 50 
#         else : 
#             return capa
        
# School_bus = Bus("School Volvo", 12, 50)
# print("The seating capacity of a School Volvo is",School_bus.capa(),"passengers")

        
# 4
# class Vehicle :
#     def __init__(self,name,mile,seat):
#         self.n = name
#         self.s = seat
#         self.m = mile
#     def fare(self):
#         return float(self.s * 100)
# class Bus(Vehicle) :
#     def __init__(self, name, mile, seat):
#         super().__init__(name, mile, seat)
#     def fare(self):
#         return float((self.s * 100) +(0.1*self.s * 100) )

# name = input("Enter the bus name:\n")
# mileage = float(input("Enter the mileage of the bus:\n"))
# seat = int(input("Enter the seating capacity of the bus:\n"))
# obj = Bus(name,mileage,seat)
# print("Total Bus fare is:",obj.fare())

# 5
# number = int(input("Enter an integer:\n"))
# dic = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
# k = []
# for i in dic.keys():
#     k.append(i)
# k = k[::-1]
# v = []
# for i in dic.values():
#     v.append(i)
# v = v[::-1]
# class  IntegerToRoman  :
#     def int_to_roman(self,n) :
#         global number
#         ans = ""
#         start = 0
#         while number > 0 :
#             for i in range(number//k[start]):
#                 ans+=v[start]
#                 number-=k[start]
#             start+=1
#         return ans
# obj = IntegerToRoman()
# print(IntegerToRoman().int_to_roman(number))
# print("The Roman numeral representation of",number,"is",obj.int_to_roman(number))


# class  IntegerToRoman  :
#     def int_to_roman(self,n) :
#         ans = ""
#          while n[-1] == 4 :
            
#         if n > 100 : 
#             ans = ans+dic[100]*(n//100)
#             n%=100
#         if n >= 50 : 
#             ans = ans+dic[50]*(n//50)
#             n%=50
#         if n >= 10 : 
#             ans = ans+dic[10]*(n//10)
#             n%=10
#         if n >= 5 :
#             ans = ans+dic[5]*(n//5)
#             n%=5
#         if n >= 1 :
#             ans = ans+dic[1]*(n//1)
#             n%=1
#         return ans
# obj = IntegerToRoman()
# print("The Roman numeral representation of",number,"is",obj.int_to_roman(number))


# 6
# Accept user input for car details
# car_make = input("Enter the car's make (manufacturer): ")
# car_model = input("Enter the car's model: ")
# car_year = int(input("Enter the car's year: "))
# car_doors = int(input("Enter the number of doors in the car: "))
# class Vehicle :
#     def __init__(self,manu,model,year):
#         self.ma = manu 
#         self.mo = model  
#         self.ye = year
#     def start_engine(self):
#         return "The"+" "+str(self.ye)+" "+self.ma+" "+self.mo+"'s"+" "+"engine is now running."
#     def stop_engine(self):
#         return "The"+" "+str(self.ye)+" "+self.ma+" "+self.mo+"'s"+" "+"engine is now stopped."
# class Car(Vehicle):
#     def __init__(self, manu, model, year,door):
#         super().__init__(manu, model, year)
#         self.door = door
#     def honk(self):
#         return "The"+" "+str(self.ye)+" "+self.ma+" "+self.mo+" "+"goes 'Honk! Honk!'"
# class Motorcycle(Vehicle):
#     def __init__(self, manu, model, year, kick):
#         super().__init__(manu, model, year)
#         self.kick = kick
#     def wheelie(self):
#         if self.kick :
#             return "The"+" "+str(self.ye)+" "+self.ma+" "+self.mo+" "+"pops a wheelie!"
#         else :
#             return "The"+" "+str(self.ye)+" "+self.ma+" "+self.mo+" "+"can't do a wheelie without a kickstand."
# # Create a Car object
# car = Car(car_make, car_model, car_year, car_doors)

# # Accept user input for motorcycle details
# motorcycle_make = input("Enter the motorcycle's make (manufacturer): ")
# motorcycle_model = input("Enter the motorcycle's model: ")
# motorcycle_year = int(input("Enter the motorcycle's year: "))
# motorcycle_has_kickstand = input("Does the motorcycle have a kickstand? (yes/no):\n").lower() == "yes"

# # Create a Motorcycle object
# motorcycle = Motorcycle(motorcycle_make, motorcycle_model, motorcycle_year, motorcycle_has_kickstand)

# # Example usage:
# print(car.start_engine())
# print(car.honk())
# print(car.stop_engine())

# print(motorcycle.start_engine())
# print(motorcycle.wheelie())
# print(motorcycle.stop_engine())


# n = int(input("number :"))
# dic = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
# k = []
# v = []
# for i in dic.keys():
#    k.append(i)
# for i in dic.values():
#    v.append(i)
# k = k[::-1]
# v = v[::-1]
# def IntToRoman():
#    global n 
#    result = ""
#    item = 0
#    while n > 0 :
#       for i in range(0,n//k[item]):
#          result+=v[item]
#          n -= k[item]
#       item+=1
#    return f"the result is {result}"
# print(IntToRoman())

