# data = [1,2,3,4,5,20]
# def middle(x,y):
#     a = data[x*2]
#     b = data[(x*2)+1]
#     c = data[y*2]
#     d = data[(y*2)+1]
#     x = (c + a)/2 
#     y = (d + b )/2 
#     return x,y
# print(list((middle(1,2))))


# two sum 
# def twoSum( nums,target ) :
# points = [1,1,2,2,3,3,4,5,7,8,1,5,3,1]
# def intersection(points,p1,p2,p3,p4):
#     x1,y1 = points[p1*2:(p1+1)*2]
#     x2,y2 = points[p2*2:(p2+1)*2]
#     x3,y3 = points[p3*2:(p3+1)*2]
#     x4,y4 = points[p4*2:(p4+1)*2]
#     m1 = (y2-y1)/(x2-x1)
#     m2 = (y4-y3)/(x4-x3)
#     c1 = y2 - m1*x2  # จาก y = mx + c 
#     c2 = y3 - m2*x3  # จาก y = mx + c 
#     x = (c2-c1)/(m1-m2)
#     y = m2*x+c2
#     return x,y
# print(intersection(points,5,6,1,2))











# lis = [1,2,3,4,5,60]
# def num():
#     for i in lis :
#         print(i)
# num()