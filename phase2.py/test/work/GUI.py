from tkinter import *
window = Tk()
window.title("MY GUI")
# Tk()
# กำหนดขนาดและตำแหน่ง 
window.geometry("500x400+0+0")

# ใส่ข้อความในหน้าจอ 
mylabel1 = Label(window,text="Hello GUI",foreground="red",font=20,bg="pink").pack()
mylabel2 = Label(window,text="Tkinter",font=50,foreground="green",bg="blue").pack()
mylabel3 = Label(window,text="Text3",font=35,foreground="orange",bg="black").pack()

# Button & COMMAND 
def ShowMessage():
    # print("Hello Tkinter!")
    message = txt.get()
    print(message)

btn1 = Button(window,text="submit",fg="white",bg="green",font=30,command=ShowMessage).pack()
btn2 = Button(window,text="cancel",fg="white",bg="red",font=30).pack()

# text area
txt = StringVar()
mytext = Entry(window,textvariable=txt).pack()


window.mainloop() 