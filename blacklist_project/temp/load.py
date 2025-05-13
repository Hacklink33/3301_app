import customtkinter 
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from customtkinter import CTkButton
from tkinter import *
from tkinter import font as tkfont
from customtkinter import *
import pyglet, tkinter
from PIL import Image, ImageTk
from CTkTable import *
from time import sleep
from enum import Enum
import random
import subprocess
import os

def animation_bar():
    container = Label(root, bg="#1d2125")
    container.grid(row=0, column=0, sticky="nsew")
    container.rowconfigure(0, weight=1)
    container.rowconfigure(1, weight=1)
    container.columnconfigure(0, weight=1)
    container.columnconfigure(1, weight=1)
    container.columnconfigure(2, weight=1)

    # Loading text 
    text_animation = Label(container, text="Loading...", font="Banschrift 15", bg="black", fg="#FFBD09")
    text_animation.grid(row=0, column=1, sticky="sw")
    main_bar = Label(container, bg="#1d2125")
    main_bar.grid(row=1, column=1, sticky="nsew")
    main_bar.rowconfigure(1, weight=1)
    main_bar.rowconfigure(2, weight=20)
    for i in range(22):
        main_bar.columnconfigure(i, weight=1)
    # Loading blocs
    for i in range (22):
        square_bar = Label(main_bar, bg="#1F2732", width=2, height=1) 
        #square_bar.place(x=(i+(27))*22, y=(screen_height/2))
        square_bar.grid(row=1, column=i, sticky="nsew", padx=(5,5))
    root.update()

    # Animation
    for x in range(2):
        for j in range(22):
            squares1 = Label(main_bar, bg="#6a040f", width=2, height=1)
            squares1.grid(row=1, column=j, sticky="nsew", padx=(5,5))
            sleep(0.06)
            root.update_idletasks()
            squares2 = Label(main_bar, bg="#1F2732", width=2, height=1)
            squares2.grid(row=1, column=j, sticky="nsew", padx=(5,5))
    for child in container.winfo_children():
        child.destroy()
    container.destroy()
    return


root = Tk()
root.geometry("1000x700")
root.title("6LACKL1ST")
root.iconbitmap("logo.ico")
root.configure(background="#1c1c1c")
root.resizable(width=True, height=True)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
path_image = tk.StringVar()
path_reverse_shell = tk.StringVar()