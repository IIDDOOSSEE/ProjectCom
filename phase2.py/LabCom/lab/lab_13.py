import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import numpy as np
from tkinter import *
def main():
    program = Osci()
    program.window.mainloop()
    
class Osci :
    def __init__(self) :
        self.window = Tk() 
        self.window.title("O S C I")
        self.window.geometry("1000x1000")
        self.Vol_La = Label(text="Voltage",fg="black").grid(row=3,column=5)
        self.KeepVolt = IntVar()
        self.Vol_En = Entry(self.window,textvariable=self.KeepVolt).grid(row=3,column=8)
        self.KeepFreq = IntVar()
        self.Freq_La = Label(text="Frequence").grid(row=5,column=5)
        self.Freq_En = Entry(self.window,textvariable=self.KeepFreq).grid(row=5,column=8)
        self.button = Button(text="Compute",command=self.plot).grid(row=4,column=20)
        


        
    def plot(self):
        voltage = self.KeepVolt.get()
        freqenzy = self.KeepFreq.get()
        GanX = np.linspace(0,1,100)
        GanY = np.linspace(0,2*math.pi*freqenzy,100)
        self.fig = plt.figure()
        plt.plot(GanX,voltage*np.sin(GanY))
        plt.title(f"Waveform:{voltage}V,{freqenzy}Hz")
        plt.xlabel("Time (s)")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.get_tk_widget().place(relx=0.35,rely=0.2)



if __name__ == "__main__":
    main()