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

class Screen(tk.Frame):
    
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        Screens[Screen.current].tkraise()
            

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "Add", font = BUTTON_FONT, command = self.go_add)
        self.btn_add.grid(row = 1, column = 0)
        
        self.btn_edit = tk.Button(self, text = "Edit", font = BUTTON_FONT, command = self.go_edit)
        self.btn_edit.grid(row = 2, column = 0)
        
        self.btn_search = tk.Button(self, text = "Search", font = BUTTON_FONT, command = self.go_search)
        self.btn_search.grid(row = 3, column = 0)
        
        self.btn_remove = tk.Button(self, text = "Remove", font = BUTTON_FONT) #, command = self.go_remove)
        self.btn_remove.grid(row = 4, column = 0)
        
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT)
        self.btn_save.grid(row = 5, column = 0)
        
    def go_search(self):
        Screen.current = 1
        Screen.switch_frame()
        
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        frm_edit_list = Edit_Choice_Menu(pop_up)
        frm_edit_list.grid(row=0,column=0)
        
    #def go_remove(self):
        #Screen.current = 3
        #Screen.switch_frame()
        
    def go_add(self):
        Screen.current = 4
        Screen.switch_frame()

class Search_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        options = ['None', 'Genre', 'Title', 'Year', 'Developer', 'Publisher', 'Price', 'Gamemode', 'Console']
        
        self.lbl_title = tk.Label(self, text = "Search Menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT, command = self.back_search)
        self.btn_back.grid(row = 5, column = 0)
        
        self.btn_clear = tk.Button(self, text = "Clear", font = BUTTON_FONT)
        self.btn_clear.grid(row = 5, column = 1)
        
        self.btn_submit = tk.Button(self, text = "Submit", font = BUTTON_FONT, command = self.confirm_search)
        self.btn_submit.grid(row = 5, column = 2)
        
        self.grid_rowconfigure(5, weight = 1)
        
        self.lbl_search_by = tk.Label(self, text = "Search By:", font = TITLE_FONT)
        self.lbl_search_by.grid(row = 1, column = 0)
        
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.dbx_search_by = tk.OptionMenu(self, self.tkvar, *options)
        self.dbx_search_by.grid(row = 2, column = 0)
        
        self.grid_rowconfigure(1, weight = 1)
        
        self.lbl_search_for = tk.Label(self, text = "Search For:", font = TITLE_FONT)
        self.lbl_search_for.grid(row = 3, column = 0)
        
        self.ent_for = tk.Entry(self, font = BUTTON_FONT)
        self.ent_for.grid(row = 4, column = 0)
        
        self.lbl_filters = tk.Label(self, text = "Filters", font = TITLE_FONT)
        self.lbl_filters.grid(row = 1, column = 2)
        
        self.frm_filters = SubFrame(self)
        self.frm_filters.grid(row = 2, column = 2)

    def back_search(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def confirm_search(self):
        Screen.current = 0
        Screen.switch_frame()

"""class Save_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Save Notice", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT, command = self.back_save)
        self.btn_save.grid(row = 1, column = 0)

    def back_save(self):
        Screen.current = 0
        Screen.switch_frame()"""

class Edit_Choice_Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        options = ['0', '1']
        
        self.lbl_title = tk.Label(self, text = "Which file to edit?", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_edit_file = tk.Label(self, text = "File To Edit:", font = TITLE_FONT)
        self.lbl_edit_file.grid(row = 1, column = 0)
        
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.dbx_edit_file = tk.OptionMenu(self, self.tkvar, *options)
        self.dbx_edit_file.grid(row = 2, column = 0)        
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.cancel)
        self.btn_cancel.grid(row = 3, column = 0)
        
        self.btn_ok = tk.Button(self, text = "OK", font = BUTTON_FONT,command = self.raise_edit)
        self.btn_ok.grid(row = 3, column = 1)
        
        self.grid_rowconfigure(3,weight=1)
        
        
        
    def cancel(self):
        self.parent.destroy()
        
    def raise_edit(self):
        Screen.current = 2
        Screen.switch_frame()
        self.parent.destroy()
        
class Edit_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Edit Menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.back_main)
        self.btn_cancel.grid(row = 6, column = 0)
        
        self.btn_reset = tk.Button(self, text = "Reset", font = BUTTON_FONT)
        self.btn_reset.grid(row = 6, column = 1)
        
        self.btn_confirm = tk.Button(self, text = "Confirm", font = BUTTON_FONT, command = self.confirm_main)
        self.btn_confirm.grid(row = 6, column = 2)
        
        self.lbl_genre = tk.Label(self, text = "Genre:", font = TITLE_FONT)
        self.lbl_genre.grid(row = 1, column = 0)
        
        self.ent_genre = tk.Entry(self, font = BUTTON_FONT)
        self.ent_genre.grid(row = 1, column = 1)        
        
        self.lbl_dev = tk.Label(self, text = "Developer:", font = TITLE_FONT)
        self.lbl_dev.grid(row = 1, column = 2)        
        
        self.ent_dev = tk.Entry(self, font = BUTTON_FONT)
        self.ent_dev.grid(row = 1, column = 3)        
        
        self.lbl_pub = tk.Label(self, text = "Publisher:", font = TITLE_FONT)
        self.lbl_pub.grid(row = 2, column = 0)        
        
        self.ent_pub = tk.Entry(self, font = BUTTON_FONT)
        self.ent_pub.grid(row = 2, column = 1)        
        
        self.lbl_year = tk.Label(self, text = "Year Released:", font = TITLE_FONT)
        self.lbl_year.grid(row = 2, column = 2)        
        
        self.ent_year = tk.Entry(self, font = BUTTON_FONT)
        self.ent_year.grid(row = 2, column = 3)        
        
        self.lbl_game_title = tk.Label(self, text = "Title:", font = TITLE_FONT)
        self.lbl_game_title.grid(row = 3, column = 0)        
        
        self.ent_game_title = tk.Entry(self, font = BUTTON_FONT)
        self.ent_game_title.grid(row = 3, column = 1)
        
    def back_choice_edit(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def confirm_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
class Remove_Choice_Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        options = ['0', '1']
        
        self.lbl_title = tk.Label(self, text = "Choose file to remove!", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_remove_file = tk.Label(self, text = "File To Remove:", font = TITLE_FONT)
        self.lbl_remove_file.grid(row = 1, column = 0)
        
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.dbx_remove_file = tk.OptionMenu(self, self.tkvar, *options)
        self.dbx_remove_file.grid(row = 2, column = 0)        
        
        self.btn_cancel = tk.Button(self,text = "Cancel", font = BUTTON_FONT, command = self.back_main)
        self.btn_cancel.grid(row = 3, column = 0)
        
        self.btn_remove = tk.Button(self,text = "Remove", font = BUTTON_FONT, command = self.go_remove)
        self.btn_remove.grid(row = 3, column = 1)

    def back_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def go_remove(self):
        Screen.current = 6
        Screen.switch_frame()

class Remove_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self,text = "Remove Menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_back = tk.Button(self,text = "Back", font = BUTTON_FONT, command = self.back_main)
        self.btn_back.grid(row = 1, column = 0)
        
        self.btn_confirm = tk.Button(self,text = "Confirm", font = BUTTON_FONT, command = self.confirm_main)
        self.btn_confirm.grid(row = 1, column = 1)

    def back_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def confirm_main(self):
        Screen.current = 0
        Screen.switch_frame()

class Add_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        options = ['0', '1']
        
        self.lbl_title = tk.Label(self, text = "Save menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_add_file = tk.Label(self, text = "File To Add:", font = TITLE_FONT)
        self.lbl_add_file.grid(row = 1, column = 0)
        
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.dbx_add_file = tk.OptionMenu(self, self.tkvar, *options)
        self.dbx_add_file.grid(row = 2, column = 0)
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.back_main)
        self.btn_cancel.grid(row = 3, column = 0)
        
        self.btn_confirm = tk.Button(self, text = "Confirm", font = BUTTON_FONT, command = self.return_main)
        self.btn_confirm.grid(row = 4, column = 0)

    def back_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def return_main(self):
        Screen.current = 0
        Screen.switch_frame()

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
    
    Screens = [MainMenu(), Search_Menu(), Edit_Menu(), Remove_Menu(), Add_Menu()]
    Screens[0].grid(row=0,column=0,sticky="news")
    Screens[1].grid(row=0,column=0,sticky="news")
    Screens[2].grid(row=0,column=0,sticky="news")
    Screens[3].grid(row=0,column=0,sticky="news")
    Screens[4].grid(row=0,column=0,sticky="news")
    
    root.grid_columnconfigure(0,weight=1)
    
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    
    search_menu = Search_Menu()
    search_menu.grid(row = 0, column = 0, sticky = "news")
    
    #save_menu = Save_Menu()
    #save_menu.grid(row = 0, column = 0, sticky = "news")
    
    edit_choice_menu = Edit_Choice_Menu(None)
    edit_choice_menu.grid(row = 0, column = 0, sticky = "news")
    
    edit_menu = Edit_Menu()
    edit_menu.grid(row = 0, column = 0, sticky = "news")
    
    remove_choice_menu = Remove_Choice_Menu(None)
    remove_choice_menu.grid(row = 0, column = 0, sticky = "news")
    
    remove_menu = Remove_Menu()
    remove_menu.grid(row = 0, column = 0, sticky = "news")
    
    add_menu = Add_Menu()
    add_menu.grid(row = 0, column = 0, sticky = "news")
    
    Screens[0].tkraise()
    
    root.mainloop()