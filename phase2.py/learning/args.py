# *args -- data = tuple
# plus number function
def add(*args):
    summation = 0 
    lis = []
    for item in args:
        lis.append(item)
        summation+=item
    print("number = ",lis)
    print("summation = ",summation)
add(10)
add(10,20)
add(100,200,5)
print()
# kwargs -- data = dict
def data(**dose):
    print(dose)
data(fname = "dose",lname = "mayta",age = 20,status = "single")