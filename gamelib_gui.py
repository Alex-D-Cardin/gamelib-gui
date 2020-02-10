#!/usr/bin/python3
#Alex Cardin
#2/10/2020

'''Game_Library_1.py done through GUI'''

import pickle
import tkinter as tk
from tkinter import scrolledtext as st

TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

#Classes go here
class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
#Functions go here


##MAIN
if __name__ == "__main__":
    pickle_file = open("game_lib.pickle", "rb")
    root = tk.Tk()
    root.title("Game Library")
    root.geometry("500x500")
    
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0)
    
    root.mainloop()