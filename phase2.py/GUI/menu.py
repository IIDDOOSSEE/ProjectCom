from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
def main():
    program = GUI()
    program.window.mainloop()
class GUI : 
    def __init__(self) :
        self.window = Tk()
        self.window.geometry("1000x1000")
        self.window.title("page 1")
        self.button()
        self.menu()
    def menu(self) :
        # menu item
        self.mymenuitem = Menu()
        self.mymenuitem.add_command(label="open file",command=self.open_flie)
        self.mymenuitem.add_command(label="save file")
        # main menu
        self.mymenu = Menu()
        self.window.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="file",menu=self.mymenuitem)
        self.mymenu.add_cascade(label="edit")
        self.mymenu.add_cascade(label="selection")
    def open_flie(self):
        my_filetypes = [('all files', '.*'), ('text files', '.txt')]
        answer = filedialog.askopenfilename(parent=self.window, 
                                 initialdir=os 
                                 .getcwd(),
                                 title="Select file",
                                 filetypes=my_filetypes)
        try:
            if answer :
                the_file = open(answer)
                self.text_file = the_file.read()
                self.mytext.insert(tk.END,self.text_file)
            elif not answer :
                messagebox.showinfo("Cancle","Click cancle")
                
        except UnicodeDecodeError: 
            messagebox.showerror("Error","Invalid file types")
            
    def button(self):
        self.mytext = tk.Text(self.window,height=30,width=75,fg="white",bg="black")
        self.mytext.place(relx=0.2)
        print(type(self.mytext))

if __name__ == "__main__":
    main()