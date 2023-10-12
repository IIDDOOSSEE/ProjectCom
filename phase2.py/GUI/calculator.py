from tkinter import *

def main():
    program = Calculator()
    program.window.mainloop()
class Calculator :
    def __init__(self) :
        self.window = Tk()
        self.window.title("Calculator")
        self.text_var = StringVar(value=0)
        self.content = ""
        # display 5 x 4
        self.display = Entry(font=50, bg="green", bd=3, width=25,textvariable=self.text_var,justify=RIGHT)  
        self.display.grid(row=0, columnspan=4)
        self.MyBtn()
    def PressBtn(self,number):
        self.content+=str(number)
        self.text_var.set(self.content)

    def clear(self):
        self.text_var.set("0")
        self.content = ""
    def calculate(self):
        self.result = eval(self.content)

    def MyBtn(self):
        self.window.option_add("*font","30")
        # row1
        btn7 = Button(text="7",width=6,height=3,command=lambda:self.PressBtn(7)).grid(row=1,column=0)
        btn8 = Button(text="8",width=6,height=3,command=lambda:self.PressBtn(8)).grid(row=1,column=1)
        btn9 = Button(text="9",width=6,height=3,command=lambda:self.PressBtn(9)).grid(row=1,column=2)
        btnc = Button(text="c",width=6,height=3,bg="orange",command=lambda:self.clear()).grid(row=1,column=3)
        # row2
        btn4 = Button(text="4",width=6,height=3,command=lambda:self.PressBtn(6)).grid(row=2,column=0)
        btn5 = Button(text="5",width=6,height=3,command=lambda:self.PressBtn(5)).grid(row=2,column=1)
        btn6 = Button(text="6",width=6,height=3,command=lambda:self.PressBtn(4)).grid(row=2,column=2)
        btn_plus = Button(text="+",width=6,height=3,bg="orange",command=lambda:self.PressBtn("+")).grid(row=2,column=3)
        # row3
        btn1 = Button(text="1",width=6,height=3,command=lambda:self.PressBtn(4)).grid(row=3,column=0)
        btn2 = Button(text="2",width=6,height=3,command=lambda:self.PressBtn(3)).grid(row=3,column=1)
        btn3 = Button(text="3",width=6,height=3,command=lambda:self.PressBtn(2)).grid(row=3,column=2)
        btn_minus = Button(text="-",width=6,height=3,bg="orange",command=lambda:self.PressBtn("-")).grid(row=3,column=3)
        # row4
        btndot = Button(text=".",width=6,height=3,command=lambda:self.PressBtn(".")).grid(row=4,column=0)
        btn0 = Button(text="0",width=6,height=3,command=lambda:self.PressBtn(0)).grid(row=4,column=1)
        btn_devide = Button(text="/",width=6,height=3,bg="orange",command=lambda:self.PressBtn("/")).grid(row=4,column=2)
        btn_muti = Button(text="x",width=6,height=3,bg="orange",command=lambda:self.PressBtn("x")).grid(row=4,column=3)
        # row5
        btnequal  = Button(text="=",width=13,height=3,command=self.calculate()).grid(row=5,columnspan=2)
        btn_Lbrac = Button(text="(",width=6,height=3,command=lambda:self.PressBtn("(")).grid(row=5,column=2)
        btn_Rbrac = Button(text=")",width=6,height=3,command=lambda:self.PressBtn(")")).grid(row=5,column=3)

if __name__ == "__main__":
    main()
