# import random
# while True :
#     bool = ["Open","Not open"] 
#     I_Ploy = random.choice(bool)
#     print(I_Ploy)
#     print("dose want to watch cartoon")
#     if I_Ploy == "Open":
#         break


from tkinter import *
window = Tk()
window.geometry("500x500")
s = Button(text="one")
s.grid(row=0,column=0)
# Button(text="two").grid(row=2,column=5)
y = Button(text="three")
y.grid(row=0,column=5)
window.mainloop()