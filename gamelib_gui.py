#!/usr/bin/python3
#Alex Cardin
#2/10/2020

'''Game_Library_1.py done through GUI'''

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

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
        
    def go_remove(self):
        pop_up = tk.Tk()
        pop_up.title("Remove")
        frm_remove_list = Remove_Choice_Menu_Choice_Menu(pop_up)
        frm_remove_list.grid(row=0,column=0)
        
    #def go_remove(self):
        #Screen.current = 3
        #Screen.switch_frame()
        
    def go_add(self):
        Screen.current = 4
        Screen.switch_frame()

class Search_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
        self.grid_columnconfigure(5, weight = 1)
        self.grid_columnconfigure(6, weight = 1)
        self.grid_columnconfigure(7, weight = 1)
        
        options = ['None', 'Genre', 'Title', 'Year', 'Developer', 'Publisher', 'Price', 'Gamemode', 'Console', 'Rating', 'Progress', 'Date Purchased']
        
        self.lbl_title = tk.Label(self, text = "Search Menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT, command = self.back_search)
        self.btn_back.grid(row = 7, column = 0, columnspan = 2, sticky = "news")
        
        self.btn_clear = tk.Button(self, text = "Clear", font = BUTTON_FONT, command = self.clear)
        self.btn_clear.grid(row = 7, column = 2, columnspan = 2, sticky = "news")
        
        self.btn_submit = tk.Button(self, text = "Submit", font = BUTTON_FONT, command = self.sumbit_search)
        self.btn_submit.grid(row = 7, column = 4, columnspan = 2, sticky = "news")
        
        self.lbl_search_by = tk.Label(self, text = "Search By:", font = TITLE_FONT)
        self.lbl_search_by.grid(row = 1, column = 0, columnspan = 2, sticky = "news")
        
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.dbx_search_by = tk.OptionMenu(self, self.tkvar, *options)
        self.dbx_search_by.grid(row = 2, column = 0, columnspan = 2, sticky = "news")
        
        self.lbl_search_for = tk.Label(self, text = "Search For:", font = TITLE_FONT)
        self.lbl_search_for.grid(row = 3, column = 0, columnspan = 2, sticky = "news")
        
        self.ent_for = tk.Entry(self, font = BUTTON_FONT)
        self.ent_for.grid(row = 4, column = 0, columnspan = 2, sticky = "news")
        
        self.lbl_filters = tk.Label(self, text = "Filters", font = TITLE_FONT)
        self.lbl_filters.grid(row = 0, column = 3, columnspan = 4, sticky = "news")
        
        self.frm_filters = SubFrame(self)
        self.frm_filters.grid(row = 1, column = 3, rowspan = 4, columnspan = 4, sticky = "news")
        
        self.scr_results = ScrolledText(self, font = BUTTON_FONT, width = 100, height = 8)
        self.scr_results.grid(row = 6, column = 0, columnspan = 6, sticky = "news")
        
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)
            
    def sumbit_search(self):
        self.scr_results.delete(0.0, "end")
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)
            
    def clear(self):
        self.frm_filters.genre_var.set(False)
        self.frm_filters.title_var.set(False)
        self.frm_filters.dev_var.set(False)
        self.frm_filters.pub_var.set(False)
        self.frm_filters.console_var.set(False)
        self.frm_filters.price_var.set(False)
        self.frm_filters.gamemode_var.set(False)
        self.frm_filters.year_var.set(False)
        self.frm_filters.notes_var.set(False)
        self.frm_filters.progress_var.set(False)
        self.frm_filters.date_purchased_var.set(False)
        self.frm_filters.rating_var.set(False)
        
        self.scr_results.delete(0.0, "end")
        
    def filter_print(self, entry):
        if self.frm_filters.genre_var.get() == True:
            msg = entry[0] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_filters.title_var.get() == True:
            msg = entry[1] + "\n"
            self.scr_results.insert("insert", msg)
        
        if self.frm_filters.dev_var.get() == True:
            msg = entry[2] + "\n"
            self.scr_results.insert("insert", msg)        
        
        if self.frm_filters.pub_var.get() == True:
            msg = entry[3] + "\n"
            self.scr_results.insert("insert", msg)        
        
        if self.frm_filters.console_var.get() == True:
            msg = entry[4] + "\n"
            self.scr_results.insert("insert", msg)
        
        if self.frm_filters.price_var.get() == True:
            msg = entry[5] + "\n"
            self.scr_results.insert("insert", msg)
        
        if self.frm_filters.gamemode_var.get() == True:
            msg = entry[6] + "\n"
            self.scr_results.insert("insert", msg)        
        
        if self.frm_filters.year_var.get() == True:
            msg = entry[7] + "\n"
            self.scr_results.insert("insert", msg)        
        
        if self.frm_filters.notes_var.get() == True:
            msg = entry[8] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_filters.progress_var.get() == True:
            msg = entry[9] + "\n"
            self.scr_results.insert("insert", msg)        
        
        if self.frm_filters.date_purchased_var.get() == True:
            msg = entry[10] + "\n"
            self.scr_results.insert("insert", msg)        
        
        if self.frm_filters.rating_var.get() == True:
            msg = entry[11] + "\n"
            self.scr_results.insert("insert", msg)        
        
        msg = "*****************\n"
        self.scr_results.insert("insert", msg)

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
        
        self.options = ['Select An Item']
        
        for key in games.keys():
            self.options.append(games[key][1])
        
        self.lbl_title = tk.Label(self, text = "Which file to edit?", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
            
        self.lbl_edit_file = tk.Label(self, text = "File To Edit:", font = TITLE_FONT)
        self.lbl_edit_file.grid(row = 1, column = 0)
            
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        self.dbx_edit_file = tk.OptionMenu(self, self.tkvar, *self.options)
        self.dbx_edit_file.grid(row = 2, column = 0)        
            
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.cancel)
        self.btn_cancel.grid(row = 3, column = 0)
            
        self.btn_ok = tk.Button(self, text = "OK", font = BUTTON_FONT,command = self.raise_edit)
        self.btn_ok.grid(row = 3, column = 1)
        
        
    def cancel(self):
        self.parent.destroy()
        
    def raise_edit(self):
        if self.tkvar.get() == self.options[0]:
            pass
        else:
            for i in range(len(self.options)):
                if self.tkvar.get() == self.options[i]:
                    Screens[2].edit_key = i
                    break        
            Screen.current = 2
            Screens[Screen.current].update()
            Screen.switch_frame()
            self.parent.destroy()
        
class Edit_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.edit_key = 0
        
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

        self.lbl_console = tk.Label(self, text = "Console:", font = TITLE_FONT)
        self.lbl_console.grid(row = 3, column = 2)        
        
        self.ent_console = tk.Entry(self, font = BUTTON_FONT)
        self.ent_console.grid(row = 3, column = 3)
        
    def update(self):
        entry = games[self.edit_key]
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[0])
        self.ent_game_title.delete(0, "end")
        self.ent_game_title.insert(0, entry[1])
        self.ent_dev.delete(0, "end")
        self.ent_dev.insert(0, entry[2])
        self.ent_pub.delete(0, "end")
        self.ent_pub.insert(0, entry[3])
        self.ent_year.delete(0, "end")
        self.ent_year.insert(0, entry[5])
        self.ent_console.delete(0, "end")
        self.ent_console.insert(0, entry[4])
    def back_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def confirm_main(self):
        entry = []
        entry.append(self.ent_genre.get())
        entry.append(self.ent_game_title.get())
        entry.append(self.ent_dev.get())
        entry.append(self.ent_pub.get())
        entry.append(self.ent_year.get())
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        #entry.append(self.scr_rotes.get(0.0,"end")) scroll wheel, which I don't have
        games[self.edit_key] = entry
        Screen.current = 0
        Screen.switch_frame()
        
class Remove_Choice_Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.options = ['Select An Item']
        
        for key in games.keys():
            self.options.append(games[key][1])
        
        
        self.lbl_title = tk.Label(self, text = "Choose file to remove!", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_remove_file = tk.Label(self, text = "File To Remove:", font = TITLE_FONT)
        self.lbl_remove_file.grid(row = 1, column = 0)
        
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        self.dbx_remove_file = tk.OptionMenu(self, self.tkvar, *self.options)
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
        
        self.edit_key = 0
        
        options = ['0', '1']
        
        self.lbl_title = tk.Label(self, text = "Add menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.dbx_add_file = tk.OptionMenu(self, self.tkvar, *options)
        self.dbx_add_file.grid(row = 2, column = 0)
        
        self.btn_cancel = tk.Button(self, text = "Cancel", font = BUTTON_FONT, command = self.back_main)
        self.btn_cancel.grid(row = 4, column = 0)
        
        self.btn_confirm = tk.Button(self, text = "Confirm", font = BUTTON_FONT, command = self.return_main)
        self.btn_confirm.grid(row = 4, column = 1)
        
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
        
        self.lbl_console = tk.Label(self, text = "Console:", font = TITLE_FONT)
        self.lbl_console.grid(row = 3, column = 2)        
        
        self.ent_console = tk.Entry(self, font = BUTTON_FONT)
        self.ent_console.grid(row = 3, column = 3)        

    def back_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def return_main(self):
        Screen.current = 0
        Screen.switch_frame()
        entry = []
        entry.append(self.ent_genre.get())
        entry.append(self.ent_game_title.get())
        entry.append(self.ent_dev.get())
        entry.append(self.ent_pub.get())
        entry.append(self.ent_year.get())
        entry.append(self.ent_console.get())
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        entry.append(0)
        #entry.append(self.scr_rotes.get(0.0,"end")) scroll wheel, which I don't have
        games[len(games) +1] = entry
        messagebox.showinfo(message = "Entry has been added.")
        self.ent_genre.delete(0, "end")
        self.ent_game_title.delete(0, "end")
        self.ent_dev.delete(0, "end")
        self.ent_pub.delete(0, "end")
        self.ent_year.delete(0, "end")
        self.ent_console.delete(0, "end")

class SubFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)        
        
        self.title_var = tk.BooleanVar(self, True)
        self.chk_title = tk.Checkbutton(self, text = "Title", variable = self.title_var)
        self.chk_title.grid(row = 0, column = 0, sticky = "news")
        
        self.genre_var = tk.BooleanVar(self, True)
        self.chk_genre = tk.Checkbutton(self, text = "Genre", variable = self.genre_var)
        self.chk_genre.grid(row = 0, column = 1, sticky = "news")
        
        self.dev_var = tk.BooleanVar(self, True)
        self.chk_developer = tk.Checkbutton(self, text = "Developer", variable = self.dev_var)
        self.chk_developer.grid(row = 0 , column = 2, sticky = "news")
        
        self.pub_var = tk.BooleanVar(self, True)
        self.chk_publisher = tk.Checkbutton(self, text = "Publisher", variable = self.pub_var)
        self.chk_publisher.grid(row = 1, column = 0, sticky = "news")
        
        self.year_var = tk.BooleanVar(self, True)
        self.chk_year = tk.Checkbutton(self, text = "Year", variable = self.year_var)
        self.chk_year.grid(row = 1, column = 1, sticky = "news")
        
        self.price_var = tk.BooleanVar(self, True)
        self.chk_price = tk.Checkbutton(self, text = "Price", variable = self.price_var)
        self.chk_price.grid(row = 1, column = 2, sticky = "news")
        
        self.console_var = tk.BooleanVar(self, True)
        self.chk_console = tk.Checkbutton(self, text = "Console", variable = self.console_var)
        self.chk_console.grid(row = 2, column = 0, sticky = "news")
        
        self.gamemode_var = tk.BooleanVar(self, True)
        self.chk_gamemode = tk.Checkbutton(self, text = "Gamemode", variable = self.gamemode_var)
        self.chk_gamemode.grid(row = 2, column = 1, sticky = "news")
        
        self.notes_var = tk.BooleanVar(self, True)
        self.chk_notes = tk.Checkbutton(self, text = "Notes", variable = self.notes_var)
        self.chk_notes.grid(row = 2, column = 2, sticky = "news")
        
        self.date_purchased_var = tk.BooleanVar(self, True)
        self.chk_date_purchased = tk.Checkbutton(self, text = "Date Purchased", variable = self.date_purchased_var)
        self.chk_date_purchased.grid(row = 3, column = 0, sticky = "news")
        
        self.rating_var = tk.BooleanVar(self, True)
        self.chk_rating = tk.Checkbutton(self, text = "Rating", variable = self.rating_var)
        self.chk_rating.grid(row = 3, column = 1, sticky = "news")
        
        self.progress_var = tk.BooleanVar(self, True)
        self.chk_progress = tk.Checkbutton(self, text = "Progess", variable = self.progress_var)
        self.chk_progress.grid(row = 3, column = 2, sticky = "news")

#Functions go here


##MAIN
if __name__ == "__main__":
    pickle_file = open("game_lib.pickle", "rb")
    games = pickle.load(pickle_file)
    pickle_file.close()
    root = tk.Tk()
    root.title("Game Library")
    
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