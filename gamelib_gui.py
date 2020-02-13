#!/usr/bin/python3
#Alex Cardin
#2/10/2020

'''Game_Library_1.py done through GUI'''

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st

TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

#Classes go here
class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        
        
        self.lbl_title = tk.Label(text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_add = tk.Button(text = "Add", font = BUTTON_FONT)
        self.btn_add.grid(row = 1, column = 0)
        self.btn_edit = tk.Button(text = "Edit", font = BUTTON_FONT)
        self.btn_edit.grid(row = 2, column = 0)
        self.btn_search = tk.Button(text = "Search", font = BUTTON_FONT)
        self.btn_search.grid(row = 3, column = 0)
        self.btn_remove = tk.Button(text = "Remove", font = BUTTON_FONT)
        self.btn_remove.grid(row = 4, column = 0)
        self.btn_save = tk.Button(text = "Save", font = BUTTON_FONT)
        self.btn_save.grid(row = 5, column = 0)
        
class Search_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        options = ['Genre', 'Title', 'Year', 'Developer', 'Publisher', 'Price', 'Gamemode', 'Console']
        
        self.lbl_title = tk.Label(self, text = "Search Menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT)
        self.btn_back.grid(row = 5, column = 0)
        self.btn_clear = tk.Button(self, text = "Clear", font = BUTTON_FONT)
        self.btn_clear.grid(row = 5, column = 1)
        self.btn_submit = tk.Button(self, text = "Submit", font = BUTTON_FONT)
        self.btn_submit.grid(row = 5, column = 2)
        
        self.grid_rowconfigure(5, weight = 1)
        
        self.lbl_search_by = tk.Label(self, text = "Search By:", font = TITLE_FONT)
        self.lbl_search_by.grid(row = 1, column = 0)
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options)
        self.dbx_search_by = tk.OptionMenu(self, set, *options)
        self.dbx_search_by.grid(row = 1, column = 0)
        
        self.lbl_search_for = tk.Label(self, text = "Search For:", font = TITLE_FONT)
        self.lbl_search_for.grid(row = 3, column = 0)
        self.ent_for = tk.Entry(self, font = BUTTON_FONT)
        self.ent_for.grid(row = 4, column = 0)
        
        self.lbl_filters = tk.Label(self, text = "Filters", font = TITLE_FONT)
        self.lbl_filters.grid(row = 1, column = 2)
        self.frm_filters = SubFrame(self)
        self.frm_filters.grid(row = 2, column = 2)

class Save_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Save Notice", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_save = tk.Button(text = "Save", font = BUTTON_FONT)
        self.btn_save.grid(row = 1, column = 0)

class Edit_Choice_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        options = ['0', '1']
        
        self.lbl_title = tk.Label(text = "Which file to edit?", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_edit_file = tk.Label(self, text = "File To Edit:", font = TITLE_FONT)
        self.lbl_edit_file.grid(row = 1, column = 0)
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options)
        self.dbx_edit_file = tk.OptionMenu(self, set, *options)
        self.dbx_edit_file.grid(row = 1, column = 0)        
        
        self.btn_cancel = tk.Button(text = "Cancel", font = BUTTON_FONT)
        self.btn_cancel.grid(row = 1, column = 0)
        self.btn_ok = tk.Button(text = "OK", font = BUTTON_FONT)
        self.btn_ok.grid(row = 1, column = 1)
        
class Edit_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Edit Menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_cancel = tk.Button(text = "Cancel", font = BUTTON_FONT)
        self.btn_cancel.grid(row = 6, column = 0)
        self.btn_reset = tk.Button(text = "Reset", font = BUTTON_FONT)
        self.btn_reset.grid(row = 6, column = 1)
        self.btn_confirm = tk.Button(text = "Confirm", font = BUTTON_FONT)
        self.btn_confirm.grid(row = 6, column = 2)
        
        self.lbl_genre = tk.Label(text = "Genre:", font = TITLE_FONT)
        self.lbl_genre.grid(row = 1, column = 0)
        
        self.ent_genre = tk.Entry(font = BUTTON_FONT)
        self.ent_genre.grid(row = 1, column = 1)        
        
        self.lbl_dev = tk.Label(text = "Developer:", font = TITLE_FONT)
        self.lbl_dev.grid(row = 1, column = 2)        
        
        self.ent_dev = tk.Entry(font = BUTTON_FONT)
        self.ent_dev.grid(row = 1, column = 3)        
        
        self.lbl_pub = tk.Label(text = "Publisher:", font = TITLE_FONT)
        self.lbl_pub.grid(row = 2, column = 0)        
        
        self.ent_pub = tk.Entry(font = BUTTON_FONT)
        self.ent_pub.grid(row = 2, column = 1)        
        
        self.lbl_year = tk.Label(text = "Year Released:", font = TITLE_FONT)
        self.lbl_year.grid(row = 2, column = 2)        
        
        self.ent_year = tk.Entry(font = BUTTON_FONT)
        self.ent_year.grid(row = 2, column = 3)        
        
        self.lbl_game_title = tk.Label(text = "Title:", font = TITLE_FONT)
        self.lbl_game_title.grid(row = 3, column = 0)        
        
        self.ent_game_title = tk.Entry(font = BUTTON_FONT)
        self.ent_game_title.grid(row = 3, column = 1)
        
class Remove_Choice_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        options = ['0', '1']
        
        self.lbl_title = tk.Label(text = "Choose file to remove!", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_remove_file = tk.Label(self, text = "File To Remove:", font = TITLE_FONT)
        self.lbl_remove_file.grid(row = 1, column = 0)
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options)
        self.dbx_remove_file = tk.OptionMenu(self, set, *options)
        self.dbx_remove_file.grid(row = 1, column = 0)        
        
        self.btn_cancel = tk.Button(text = "Cancel", font = BUTTON_FONT)
        self.btn_cancel.grid(row = 1, column = 0)
        self.btn_remove = tk.Button(text = "Remove", font = BUTTON_FONT)
        self.btn_remove.grid(row = 1, column = 1)

class Remove_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Edit Menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_back = tk.Button(text = "Back", font = BUTTON_FONT)
        self.btn_back.grid(row = 1, column = 0)
        self.btn_confirm = tk.Button(text = "Confirm", font = BUTTON_FONT)
        self.btn_confirm.grid(row = 1, column = 1)

class SubFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.chk_title = tk.Checkbutton(self, text = "Title")
        self.chk_title.grid(row = 0, column = 0)
        
        self.chk_genre = tk.Checkbutton(self, text = "Genre")
        self.chk_genre.grid(row = 0, column = 1)
        
        self.chk_developer = tk.Checkbutton(self, text = "Developer")
        self.chk_developer.grid(row = 0 , column = 2)
        
        self.chk_publisher = tk.Checkbutton(self, text = "Publisher")
        self.chk_publisher.grid(row = 1, column = 0)
        
        self.chk_year = tk.Checkbutton(self, text = "Year")
        self.chk_year.grid(row = 1, column = 1)
        
        self.chk_price = tk.Checkbutton(self, text = "Price")
        self.chk_price.grid(row = 1, column = 2)
        
        self.chk_console = tk.Checkbutton(self, text = "Console")
        self.chk_console.grid(row = 2, column = 0)
        
        self.chk_gamemode = tk.Checkbutton(self, text = "Gamemode")
        self.chk_gamemode.grid(row = 2, column = 1)
        
        self.chk_notes = tk.Checkbutton(self, text = "Notes")
        self.chk_notes.grid(row = 2, column = 2)
        
        #self.grid_rowconfigure(0, weight = 1)
        #self.grid_rowconfigure(1, weight = 1)
        #self.grid_rowconfigure(2, weight = 1)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)

#Functions go here


##MAIN
if __name__ == "__main__":
    pickle_file = open("game_lib.pickle", "rb")
    root = tk.Tk()
    root.title("Game Library")
    root.geometry("750x750")
    
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    
    search_menu = Search_Menu()
    search_menu.grid(row = 0, column = 0, sticky = "news")
    
    save_menu = Save_Menu()
    save_menu.grid(row = 0, column = 0, sticky = "news")
    
    edit_choice_menu = Edit_Choice_Menu()
    edit_choice_menu.grid(row = 0, column = 0, sticky = "news")
    
    edit_menu = Edit_Menu()
    edit_menu.grid(row = 0, column = 0, sticky = "news")
    
    remove_choice_menu = Remove_Choice_Menu()
    remove_choice_menu.grid(row = 0, column = 0, sticky = "news")
    
    remove_menu = Remove_Menu()
    remove_menu.grid(row = 0, column = 0, sticky = "news")
    
    main_menu.tkraise()
    root.mainloop()