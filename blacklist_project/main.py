import customtkinter
from customtkinter import CTkButton, CTkImage
from tkinterdnd2 import TkinterDnD, DND_FILES
from customtkinter import *
from CTkTable import *
import tkinter as tk
from tkinter import PhotoImage, ttk, font as tkfont, messagebox, filedialog
from tkinter import *
import pyglet
from PIL import Image, ImageTk
from time import sleep
from enum import Enum
import random
import subprocess
import os
from connectors import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
pyglet.font.add_file(f"./fonts/HackGlitch-DOlY9.otf")
pyglet.font.add_file(f"./fonts/Hackout-Eaw5j.otf")


def show_popup(parent, message):
    # Create a new Toplevel window
    popup = tk.Toplevel(parent)
    popup.title("Message")
    popup.geometry("300x200")  # Set the size of the pop-up window
    popup.config(background="#1d2125")

    # Get the position of the parent window
    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    # Center the pop-up window on the same screen as the parent window
    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = parent_x + (parent_width // 2) - (width // 2)
    y = parent_y + (parent_height // 2) - (height // 2)
    popup.geometry(f'{width}x{height}+{x}+{y}')

    # Add a label to the pop-up window
    label = tk.Label(popup, text=f'Message:\n{message}', font=("h Hackout", 22), background="#1d2125", foreground="white")
    label.pack(pady=20)

    # Add the OK button to the pop-up window
    ok_button = tk.Button(popup, text="OK", width=25, background="#1d2125", foreground="white", command=popup.destroy)
    ok_button.pack(pady=10)

def destroy_matrix():
    global matrix
    for children in matrix.label_matrix.winfo_children():
        children.destroy()
    matrix.label_matrix.destroy()
    matrix = None

def hide_me():
    global matrix
    btn.place_forget()
    destroy_matrix()
    # animation_bar()
    dashboard()

def clear_main_frame(main):
    # Loop through all children of the 'main' frame and destroy them
    for widget in main.winfo_children():
        widget.destroy()


def page_1(header, nav, main):
    clear_main_frame(main)
    clear_main_frame(header)
    TabsApp = TabApp(main)
    # TabsApp.add_tab("Tab 1")
    header.config(text="Reverse-Shell in Powershell", background="#292e32", font=("h Hackout", 25))

    main_box = TkinterDnD.Tk()

    def drop_inside_list_box(event):
        listb.insert("end", event.data)

    def drop_inside_textbox(event):
        tbox.delete("1.0", "end")
        with open(event.data, "r") as file:
            for line in file:
                line = line.strip()
                tbox.insert("end", f"{line}\n")

    def open_file_dialog(event=None):
    
        file_paths = filedialog.askopenfilenames(title="Select Files")

    listb = tk.Listbox(main_box, selectmode=tk.SINGLE, background="white")
    listb.pack(fill=tk.X)
    listb.drop_target_register(DND_FILES)
    listb.dnd_bind("<<DROP>>", drop_inside_list_box)
    listb.bind("<Button-1>", open_file_dialog)

    tbox = tk.Text(main_box)
    tbox.pack()
    tbox.drop_target_register(DND_FILES)
    tbox.dnd_bind("<<DROP>>", drop_inside_textbox)

    

def page_2(header, nav, main):
    clear_main_frame(main)
    clear_main_frame(header)
    TabsApp = TabApp(main)
    header.config(text="Account Generator", background="#292e32", font=("h Hackout", 25))
#     # main.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
#     # header.grid(row=0, column=0, columnspan=3, sticky="nswe", padx=5, pady=5)
#     return


#def  print_dashboard(label, navigation, header, main)

def dashboard():
    label = Label(root, background="#1d2125")
    navigation = Label(label, background="#292e32")
    header = Label(label, text="Choose a selection", background="#292e32", font=("h Hackout", 25))
    main = Label(label, background="#1d2125")
    label.columnconfigure(0, weight=1)
    label.columnconfigure(1, weight=6)
    label.rowconfigure(0, weight=1)
    label.rowconfigure(1, weight=6)
    label.grid(row=0, column=0, sticky="nsew", padx=(10,10), pady=(10,10))
    navigation.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    for i in range(9):
        navigation.rowconfigure(i, weight=1)
    navigation.columnconfigure(0, weight=1)
    btn_nav_1 = CTkButton(navigation, text="Reverse-Shell", fg_color="#1c1c1c",
                hover_color="#1d2125", border_color="#292e32",
                border_width=3, command=lambda: page_1(header, navigation, main))
    btn_nav_1.grid(row=0, column=0, sticky="nsew")
    btn_nav_2 = CTkButton(navigation, text="Account Generator", fg_color="#1c1c1c",
                hover_color="#1d2125", border_color="#292e32",
                border_width=3, command=lambda: page_2(header, navigation, main))
    btn_nav_2.grid(row=1, column=0, sticky="nsew")
    btn_nav_3 = CTkButton(navigation, text="Page 3", fg_color="#1c1c1c",
                hover_color="#1d2125", border_color="#292e32",
                border_width=3, command=lambda: show_popup(root,''))
    btn_nav_3.grid(row=2, column=0, sticky="nsew")
    btn_nav_4 = CTkButton(navigation, text="Page 4", fg_color="#1c1c1c",
                hover_color="#1d2125", border_color="#292e32",
                border_width=3)
    btn_nav_4.grid(row=3, column=0, sticky="nsew")
    btn_nav_5 = CTkButton(navigation, text="Page 5", fg_color="#1c1c1c",
                hover_color="#1d2125", border_color="#292e32",
                border_width=3)
    btn_nav_5.grid(row=4, column=0, sticky="nsew")
    btn_nav_6 = CTkButton(navigation, text="Page 6", fg_color="#1c1c1c",
                hover_color="#1d2125", border_color="#292e32",
                border_width=3)
    btn_nav_6.grid(row=5, column=0, sticky="nsew")
    btn_nav_7 = CTkButton(navigation, text="Page 7", fg_color="#1c1c1c",
                hover_color="#1d2125", border_color="#292e32",
                border_width=3)
    btn_nav_7.grid(row=6, column=0, sticky="nsew")
    btn_nav_8 = CTkButton(navigation, text="Security", fg_color="#1c1c1c",
                hover_color="#1d2125", border_color="#292e32",
                border_width=3)
    btn_nav_8.grid(row=7, column=0, sticky="nsew")
    header.grid(row=0, column=0, columnspan=3, sticky="nswe", padx=5, pady=5)
    main.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    return

# root
root = TkinterDnD.Tk()
root.geometry("1000x700")
root.title("6LACKL1ST")
root.iconbitmap("logo.ico")
root.configure(background="#1c1c1c")
root.resizable(width=True, height=True)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
path_image = tk.StringVar()
path_reverse_shell = tk.StringVar()
extension = tk.StringVar()

matrix = MatrixScreen(root)
matrix.update_matrix()

# image launch button 
img = Image.open("./hack.ico")

# button 
btn = CTkButton(root, text="Launch", corner_radius=32, fg_color="#6a040f",
                hover_color="#8c0715", border_color="#fffcf2",
                border_width=2, image=CTkImage(dark_image=img), command=hide_me)
btn.place(relx=0.5, rely=0.5, anchor="center")

# main window 
animation = Label(root, text="Loading...", font="Banschrift 15", bg="black", fg="#FFBD09")
root.update()

#Setup a library to new additionnal extension
ext = {
    1: "gnp",
    2: "xcod",
    3: "fdp",
    4: "slx",
    5: "xtpp"
}

# launch root 
root.mainloop()