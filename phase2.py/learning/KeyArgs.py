def data(name,surname,age="20"): #default paramiter  กำหนดค่าเริ่มต้น
    print("name : ",name)
    print("surname : ",surname)
    print("age : ",age)
data("mayta","dose",19) # no fix
print()
data(surname = "mayta",name="dose",age=19) # fix
print()
data(surname = "mooping",name="kaoneaw") # ไม่ต้องกรอกอายุเพราะมี default paramiter