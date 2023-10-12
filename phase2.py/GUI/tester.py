from tkinter import *
import tkinter as tk
# def test():
#     beta = Tester()
#     beta.root.mainloop()
# class Tester :
#     def __init__(self) :
#         self.root = Tk()
#         self.root.geometry("500x500")
#         self.btn()
#     def btn(self):
#         btn1 = Button(self.root,text="1")
#         btn1.grid()

# if __name__ == "__main__" :
#     test()
# from tkinter import *

# win = Tk()
# Label(text="hello").grid(padx=5,pady=5)
# text = Text(win,bg="green")
# text.grid(row=1, column=0, columnspan=3, rowspan=4)
# b1 = Button(win, text="Button 1")
# b1.grid(row=1, column=1 )
# b2 = Button(win, text="Button 2")
# b2.grid(row=1, column=2 )
# b3 = Button(win, text="Button 3")
# b3.grid(row=1, column=0 )
# win.mainloop()


from tkinter import *
from tkinter import ttk

# -เปิดเกมมาเลือก 3 โหมด PVP PVA AVA
def main():
    program = Othello()
    program.window.mainloop()
class Othello :
    def __init__(self) :
        self.window = Tk()
        self.window.title("Othello")
        self.black = PhotoImage(file="C:/python/phase2.py/GUI/black.png")
        self.window.geometry("900x700")
        self.window.config(bg="blue")
        area = Frame(self.window)
        area.grid(row=0, column=0,sticky=N)

        header = Label(text="Choose mode", font=("Arial", 30),bg="#b3fdff") 
        header.grid(row=0,column=2,pady=20,sticky=N)
        Button(text="P V P", font=("Arial", 20),command=self.board).grid(row=1,column=1,padx=50,sticky=N)
        Button(text="P V A", font=("Arial", 20),command=self.board).grid(row=1,column=2,padx=50)
        Button(text="A V A", font=("Arial", 20),command=self.board).grid(row=1,column=3,padx=50)
    def board(self):
        for i in range(4,12):
            for j in range(4,12):
                if (i+j) %2 == 0 :
                    green = Button(bg="green",width=5,height=2)
                    green.grid(row=i ,column=j,sticky=W)
                else :
                    darkgreen =Button(bg="darkgreen",width=5,height=2)
                    darkgreen.grid(row=i ,column=j,sticky=W)

if __name__ == "__main__" :
    main()