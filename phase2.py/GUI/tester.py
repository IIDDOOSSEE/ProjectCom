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
root = Tk()
root.configure(bg="light gray")
left_frame = tk.Frame(root, bg="blue")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
root.mainloop()
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