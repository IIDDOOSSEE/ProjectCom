import math

print("Input coordinates of two points:")
fLati = float(input("Starting latitude:\n"))
fLong= float(input("Starting longitude:\n"))
sLati = float(input("Ending latitude:\n"))
sLong= float(input("Ending longitude:\n"))
r = 6371.01

def cal(deg):
    rad = deg * math.pi / 180
    return rad

x = math.sin((cal(fLati) - cal(sLati))/2)**2 + (math.cos(cal(fLati))*math.cos(cal(sLati)))*\
math.sin((cal(fLong) - cal(sLong))/2)**2

d = 2*r*math.asin(math.sqrt(x))
str(d)
print("The distance is","%.2f"%(d)+"km.")