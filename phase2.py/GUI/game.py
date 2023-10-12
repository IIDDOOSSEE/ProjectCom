# import tkinter as tk
# from tkinter import *
# from tkinter import PhotoImage


# #ตารางโชว์
# class windowgame:

#     def __init__(self):
#         self.root = tk.Tk()
#         self.phototable = PhotoImage(file="C:\\python\\phase2.py\\GUI\\bg.png")
#         self.table, self.score = self.frame()
#         self.st = self.background()
        
        
#     def frame(self):
#         table = tk.Frame(self.root, bg='red', width=400, height=400)
#         table.grid(row=1, column=0)
        
#         score = tk.Frame(self.root, bg='blue', width=400, height=100)
#         score.grid(row=0, column=0)
        
#         return table, score
    
#     def background(self):
#         button_grid = []
#         for i in range(8):
#             row_column = []
#             for a in range(8):
#                 button = tk.Button(self.table, image=self.phototable)
#                 button.grid(row=i, column=a, padx=2, pady=2)

#                 row_column.append(button)
#             button_grid.append(row_column)  
#         return button_grid
      

# #pvp
# class pvp:
#     def __init__(self):
#         self.pvp_window = windowgame()

# def open_pvp():
#     pvp_window = pvp()

# #ทำmainหน้าแรกเพื่อเลือกPVP PVA
# class Window1:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Othello")
#         self.root.geometry("300x150")

#         self.label = tk.Label(self.root, text="WELCOME TO OTHELLO")
#         self.label.grid(row=0, column=2)

#         self.button_pvp = tk.Button(self.root, text="   PVP   ", bg="grey", fg="white",command=open_pvp )
#         self.button_pvp.grid(row=2, padx=5, pady=5)

#         self.button_pva = tk.Button(self.root, text="   PVA   ", bg="grey", fg="white")
#         self.button_pva.grid(row=2, column=3)

#         self.root.mainloop()

# Window1()









import tkinter as tk

# Create a class for the main menu window
class Window1:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Othello")
        self.root.geometry("300x150")

        self.label = tk.Label(self.root, text="WELCOME TO OTHELLO")
        self.label.grid(row=0, column=2)

        self.button_pvp = tk.Button(self.root, text="   PVP   ", bg="grey", fg="white", command=self.open_pvp)
        self.button_pvp.grid(row=2, padx=5, pady=5)

        self.button_pva = tk.Button(self.root, text="   PVA   ", bg="grey", fg="white")
        self.button_pva.grid(row=2, column=3)

    def open_pvp(self):
        pvp_window = PvPWindow()
        # self.root.mainloop()

# Create a class for the PvP game window
class PvPWindow:
    def __init__(self):
        self.pvp_window = tk.Toplevel()
        self.pvp_window.title("PvP Game")

        self.phototable = tk.PhotoImage(file="C:/python/phase2.py/GUI/bg.png")

        self.table, self.score = self.frame()
        self.st = self.background()

    def frame(self):
        table = tk.Frame(self.pvp_window, bg='red', width=400, height=400)
        table.grid(row=1, column=0)

        score = tk.Frame(self.pvp_window, bg='blue', width=400, height=100)
        score.grid(row=0, column=0)

        return table, score

    def background(self):
        button_grid = []
        for i in range(8):
            row_column = []
            for a in range(8):
                button = tk.Button(self.table, image=self.phototable)
                button.grid(row=i, column=a, padx=2, pady=2)

                row_column.append(button)
            button_grid.append(row_column)
        return button_grid

if __name__ == "__main__":
    main_window = Window1()
    main_window.root.mainloop()
