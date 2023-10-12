# import pandas as pd
# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)
# import numpy as np
# import matplotlib as mpl
# import matplotlib as plt
# x = np.linspace(0,10,100)
# fig = plt
# print(x)

# import matplotlib.pyplot as plt
# import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
def main():
    program = Lab()
    program.window.mainloop()
class Lab :
    def __init__(self) :
        self.window = Tk()
        self.window.title("Create Graph")
        self.window.geometry("1000x1000")
        self.showbutton()
    def plot(self):
        print(np.pi)
        x  = np.linspace(0,4*np.pi,1000)
        print(x)
        fig = plt.figure()
        plt.plot(x, np.sin(x), '-', color="blue", linewidth=2)
        # plt.plot(x, np.cos(x), '--')
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        # plt.show()
    def showbutton(self):
        button = tk.Button(self.window,text="Showbutton",bg="black",fg="white",command=self.plot).pack()
    
if  __name__ == "__main__" :
    main()

