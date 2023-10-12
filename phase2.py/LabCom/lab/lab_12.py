from tkinter import *
import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox

# ask for open file 
def main():
    program =  Readfile()
    program.window.mainloop()
class Readfile :
    def __init__(self) :
        self.window = tk.Tk()
        self.window.geometry("1000x1000")
        self.window.title("Text Editor")
        self.mytext = None
        self.m = None
        self.word = None
        self.char = None
        self.size = None
        self.createwidget()
        self.window.bind("<KeyRelease>",self.count)
    def open_file(self):
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
            messagebox.showerror("Error","Fail to open invalid flie type")
        self.count(0)
    def count(self,event):
        length = self.mytext.get("1.0",tk.END).replace(" ","").replace("\n","")
        char0 = "Characters: {}".format(len(length))
        self.char.config(text = char0)

        byte = self.mytext.get("1.0",tk.END)
        count_byte = ""
        if len(byte) == 1:
            count_byte = "N/A"
        else:
            count_byte = len(byte)-1
        rebyte = f"File Size: {count_byte} bytes"
        self.size.config(text = rebyte)

        word =  self.mytext.get("1.0",tk.END).split()
        count_word = f"Words: {len(word)}"
        self.word.config(text = count_word)

    def action_SaveFile(self):
        files = [('Text Document', '*.txt')]
        filename = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
        filename.write(self.mytext.get("1.0",tk.END))


    def createwidget(self) :
        self.open_btn = Button(text="Open",bg="blue",width=15,command =self.open_file).grid(row=0,column=0,padx=10,pady=10)
        self.save_btn = Button(text="Save",bg="green",command=self.action_SaveFile).grid(row=1,column=0,padx=10,pady=10)
        self.clear_btn = Button(text="Clear",bg="red",command=self.clear).grid(row=3,column=0,padx=10,pady=10)

        self.word = tk.Label(self.window, text=" ")
        self.word.grid(row=11,column=0)
        self.char = tk.Label(self.window, text=" ")
        self.char.grid(row=12,column=0)
        self.size = tk.Label(self.window, text=" ")
        self.size.grid(row=13,column=0)
        # self.text = StringVar()
        # self.mytext = Entry(self.window).grid(row=2,column=0,padx=10,pady=10)
        self.search_btn = Button(text="Search",bg="white",command=self.search).grid(row=5,column=0,padx=10,pady=10)
        self.mytext = tk.Text(self.window,height=30,width=75,fg="white",bg="black")
        self.mytext.place(relx=0.2)
        self.m = StringVar()
        texthighlight = Entry(self.window, textvariable=self.m)
        texthighlight.grid(row = 4, column=0)
        # lb4 = tk.Label(self.window, text=' ')
        # lb4.grid(row = 8, column=0)

        
    def clear(self):
        self.mytext.delete("1.0","end")
        self.char.config(text="Characters:0")
        self.size.config(text="File Size: N/A bytes")
        self.word.config(text="Words:0")
        
    def search(self):
        query = self.m.get() 
        if query:
            text = self.mytext.get("1.0", tk.END)
            start = text.find(query)
            if start != -1:
                end = start + len(query)
                self.mytext.tag_remove("search", "1.0", tk.END)
                self.mytext.tag_add("search", f"1.0 + {start}c", f"1.0 + {end}c")
                self.mytext.tag_configure("search", background="yellow")
                self.mytext.mark_set(tk.INSERT, f"1.0 + {end}c")
                self.mytext.see(tk.INSERT)
            else:
                messagebox.showinfo("Not Found", f"'{query}' not found in the text.")
        else:
            messagebox.showwarning("Search", "Please enter a search query.")
if __name__ == "__main__":
    main()