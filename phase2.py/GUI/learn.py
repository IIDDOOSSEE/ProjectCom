from tkinter import *
from tkinter.filedialog import *
import tkinter as tk
import numpy as np

# INSERT File 
# window = Tk()
# window.geometry("700x700")
# message = Text(width=20,height=20,bg="black",fg="white")
# message.pack()
# print(type(message))
# def selectfile():
#     chooseFile = askopenfilename()
#     file_content = open(chooseFile,encoding="utf8")
#     message.insert(tk.END,file_content.read())

# btn1 = Button(text="select file",command=selectfile).pack()

# window.mainloop()
def calculate():
    result = (radius.get())**2 * np.pi
    ans.insert(0,result)
def clear():
    rad.delete(0,END)
    ans.delete(0,END)

window = Tk()
# window.option_add("*font","impact 30")
radius = IntVar()
Label(text="radius :").grid(row=0,sticky=W)
rad = Entry(textvariable=radius,width=30)
rad.grid(row=0,column=1)
Label(text="area :").grid(row=1,sticky=E)
ans = Entry(width=30)
ans.grid(row=1,column=1)
Button(text="calculate",command=calculate).grid(row=2,column=1,sticky=W)
Button(text="clear",command=clear).grid(row=2,column=1,sticky=E)
    
window.mainloop()
    