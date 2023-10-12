# class Employee :
#     def __init__(self,name,salaty) :
#         self.name = name
#         self.salary = salaty
#     def showdata(self):
#         print(f"name : {self.name}, salary : {self.salary}")
# obj1 = Employee("dose",2000)
# obj1.showdata()

# class Point:
#     def __init__(self,initx,inity ):
#         self.x = initx
#         self.y = inity
#     def getX(self) :
#         return self.x
#     def getY(self) :
#         return self.y
#     def distance(self) :
#         return ((self.x**2)+(self.y**2))**0.5
#     def __str__(self) :
#         return "x=" + str(self.x) + ", y=" + str(self.y) +", distance = "+ str(((self.x**2)+(self.y**2))**0.5)

    
# class Point :
#     def __init__(self) :
        
# import math

# class Circle:
#     def __init__(self, point1, point2, point3):
#         self.point1 = point1
#         self.point2 = point2
#         self.point3 = point3

#     def find_center_radius(self):
#         x1, y1 = self.point1
#         x2, y2 = self.point2
#         x3, y3 = self.point3

#         # Calculate the midpoint of the line segment between point1 and point2
#         midpoint1 = ((x1 + x2) / 2, (y1 + y2) / 2)

#         # Calculate the midpoint of the line segment between point2 and point3
#         midpoint2 = ((x2 + x3) / 2, (y2 + y3) / 2)

#         # Calculate the slopes of the lines passing through the two midpoints
#         if x1 != x2:
#             slope1 = -(y2 - y1) / (x2 - x1)
#         else:
#             slope1 = math.inf

#         if x2 != x3:
#             slope2 = -(y3 - y2) / (x3 - x2)
#         else:
#             slope2 = math.inf

#         # Calculate the center coordinates (h, k)
#         h = (midpoint2[1] - midpoint1[1] + slope1 * midpoint1[0] - slope2 * midpoint2[0]) / (slope1 - slope2)
#         k = slope1 * (h - midpoint1[0]) + midpoint1[1]

#         # Calculate the radius (r) using the distance formula
#         r = math.sqrt((x1 - h) ** 2 + (y1 - k) ** 2)

#         return (h, k), r

# # Example usage:
# point1 = (0, 0)
# point2 = (1, 0)
# point3 = (0, 1)

# circle = Circle(point1, point2, point3)
# center, radius = circle.find_center_radius()

# print(f"Center of the circle: {center}")
# print(f"Radius of the circle: {radius}")

import math
class Point :
    def __init__(self,x,y) :
        self.x = x
        self.y = y 
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceFromOrigin(self):
        return ((self.x**2 + self.y**2))**0.5
    def distanceFromPoint(self,q):
        dx = (q.getX()-self.x)
        dy = (q.getY()-self.y)
        return math.sqrt(dx**2+dy**2)
p = Point(3,3)
r = Point(6,7)
print(p.distanceFromPoint(r))


        