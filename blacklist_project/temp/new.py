import customtkinter
from customtkinter import CTkButton, CTkImage
from tkinterdnd2 import TkinterDnD, DND_FILES
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pyglet
from PIL import Image
import random
import subprocess
import os
from enum import Enum

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
pyglet.font.add_file(f"./fonts/HackGlitch-DOlY9.otf")
pyglet.font.add_file(f"./fonts/Hackout-Eaw5j.otf")


class CharacterType(Enum):
    ZERO = 0
    ONE = 1
    SPACE = 2
    SPECIAL = 3
    MATRIX = 4


class MatrixScreen:
    def __init__(self, parent, update_interval=100, line_length=189):
        self.label_matrix = tk.Label(parent, background="#1d2125")
        self.label_matrix.pack(expand=True, fill="both")

        self.special_characters = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]

        self.matrix_display = tk.Text(
            self.label_matrix,
            bg="black",
            fg="red",
            font=("Courier", 12),
            wrap=tk.WORD,
            padx=10,
            pady=10,
        )
        self.matrix_display.pack(expand=True, fill=tk.BOTH)

        self.update_interval = update_interval
        self.line_length = line_length

    def random_char(self):
        matrix_character = ['日', 'ﾊ', 'ﾐ', 'ﾋ', 'ｰ', 'ｳ', 'ｼ', 'ﾅ', 'ﾓ', 'ﾆ', 'ｻ', 'ﾜ', 'ﾂ', 'ｵ', 'ﾘ',
                            'ｱ', 'ﾎ', 'ﾃ', 'ﾏ', 'ｹ', 'ﾒ', 'ｴ', 'ｶ', 'ｷ', 'ﾑ', 'ﾕ', 'ﾗ', 'ｾ', 'ﾈ', 'ｽ',
                            'ﾀ', 'ﾇ', 'ﾍ', 'ｦ', 'ｲ', 'ｸ', 'ｺ', 'ｿ', 'ﾁ', 'ﾄ', 'ﾉ', 'ﾌ', 'ﾔ', 'ﾖ', 'ﾙ',
                            'ﾚ', 'ﾛ', 'ﾝ', ':', '・', '.', '"', '=', '*', '+', '.', '<', '>', '¦', '｜',
                            ' FSOCIETY ']
        weights = [1] * len(matrix_character)
        weights[-1] = 0.1
        choice = CharacterType(random.randint(0, 4))
        if choice == CharacterType.ZERO:
            return '0'
        elif choice == CharacterType.ONE:
            return '1'
        elif choice == CharacterType.SPACE:
            return ' '
        elif choice == CharacterType.MATRIX:
            return random.choices(matrix_character, weights, k=1)[0]
        else:
            return random.choice(self.special_characters)

    def update_matrix(self):
        new_line = ''.join([self.random_char() for _ in range(self.line_length)])
        self.matrix_display.insert(tk.END, new_line + '\n')
        self.matrix_display.see(tk.END)
        self.label_matrix.after(self.update_interval, self.update_matrix)


class TabApp:
    def __init__(self, parent):
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent, style='TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=1)

        self.tabs = {
            'compiletheexecutable': CompileExecutableTab(self.notebook),
            'createawinrarsfxarchive': CreateWinRarSfxArchiveTab(self.notebook),
            'openservers': OpenServersTab(self.notebook),
        }

        for tab_name, tab in self.tabs.items():
            self.notebook.add(tab.frame, text=tab_name.replace("_", " ").title())

        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def on_tab_change(self, event=None):
        selected_tab_index = self.notebook.index(self.notebook.select())
        selected_tab_name = self.notebook.tab(selected_tab_index, "text").lower().replace(" ", "")
        print(f"Switched to tab: {selected_tab_name}")


class CompileExecutableTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#1d2125")
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.frame, text="Pass from .ps1 to .exe", font=("Hack Glitch", 24),
                         anchor='center', justify='center', background="#292e32", foreground="white")
        title.pack(pady=30)

        # Additional widgets can be added here

class CreateWinRarSfxArchiveTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#1d2125")
        self.checkbox_var = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.frame, text="Sfx Archive", font=("Hack Glitch", 24),
                         anchor='center', justify='center', background="#292e32", foreground="white")
        title.pack(pady=30)

        help_button = tk.Button(self.frame, text="?", command=self.show_shell_help,
                                background="#1d2125", foreground="white")
        help_button.pack(pady=(20, 5))

        # Add labels and input fields
        self.add_input_fields()

    def add_input_fields(self):
        image_label = tk.Label(self.frame, text="Path of the file to show:", anchor='w',
                               background="#292e32", foreground="white")
        image_label.pack(padx=20, pady=(20, 5))

        self.image_entry = tk.Entry(self.frame, width=40)
        self.image_entry.pack(padx=20, pady=(5, 10))

        shell_label = tk.Label(self.frame, text="Path of the program to execute:", anchor='w',
                                background="#292e32", foreground="white")
        shell_label.pack(padx=20, pady=(10, 5))

        self.shell_entry = tk.Entry(self.frame, width=40)
        self.shell_entry.pack(padx=20, pady=(5, 10))

        # Checkbox examples
        checkboxes = ["IMG", "WORD", "PDF", "EXCEL", "P.P"]
        for i, text in enumerate(checkboxes):
            checkbox = tk.Checkbutton(self.frame, text=text, variable=self.checkbox_var,
                                      onvalue=i + 1, offvalue=0, background="#1d2125", foreground="white")
            checkbox.pack(anchor='w', padx=20, pady=(2, 10))

        save_button = tk.Button(self.frame, text="Save", command=self.save_info,
                                width=40, background="#1d2125", foreground="white")
        save_button.pack(pady=(10, 20))

    def save_info(self):
        image_path = self.image_entry.get()
        shell_path = self.shell_entry.get()
        print(f"Image: {image_path}, Shell: {shell_path}, Checkbox Value: {self.checkbox_var.get()}")

    def show_shell_help(self):
        messagebox.showinfo("Help", "You need to put the 2 files in the same folder as main.py. (Or copy the full path)")

class OpenServersTab:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#1d2125")
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.frame, text="External connections", font=("Hack Glitch", 24),
                         anchor='center', justify='center', background="#292e32", foreground="white")
        title.pack(pady=30)

        self.add_input_fields()

    def add_input_fields(self):
        dir_label = tk.Label(self.frame, text="Directory to start the python3 server:", anchor='w',
                              background="#292e32", foreground="white")
        dir_label.pack(padx=20, pady=(20, 5))

        self.dir_entry = tk.Entry(self.frame, width=40)
        self.dir_entry.pack(padx=20, pady=(5, 10))

        ip_label = tk.Label(self.frame, text="Your public IP address:", anchor='w',
                            background="#292e32", foreground="white")
        ip_label.pack(padx=20, pady=(10, 5))

        self.ip_entry = tk.Entry(self.frame, width=40)
        self.ip_entry.pack(padx=20, pady=(5, 10))
                
        save_button = tk.Button(self.frame, text="Save", command=self.save_info,
                                width=40, background="#1d2125", foreground="white")
        save_button.pack(pady=(10, 20))

    def save_info(self):
        directory = self.dir_entry.get()
        public_ip = self.ip_entry.get()
        print(f"Directory: {directory}, Public IP: {public_ip}")
        # Here you can add the logic to handle the server setup or any other required action.


def dashboard():
    label = tk.Label(root, background="#1d2125")
    navigation = tk.Label(label, background="#292e32")
    header = tk.Label(label, text="Choose a selection", background="#292e32", font=("Hack Glitch", 25))
    main = tk.Label(label, background="#1d2125")
    
    label.columnconfigure(0, weight=1)
    label.columnconfigure(1, weight=6)
    label.rowconfigure(0, weight=1)
    label.rowconfigure(1, weight=6)
    label.grid(row=0, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))
    navigation.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    for i in range(9):
        navigation.rowconfigure(i, weight=1)
    navigation.columnconfigure(0, weight=1)

    # Navigation buttons
    btn_nav_1 = CTkButton(navigation, text="Reverse-Shell", command=lambda: page_1(header, main))
    btn_nav_1.grid(row=0, column=0, sticky="nsew")
    
    btn_nav_2 = CTkButton(navigation, text="Account Generator", command=lambda: page_2(header, main))
    btn_nav_2.grid(row=1, column=0, sticky="nsew")

    # Additional navigation buttons can be added here...

    header.grid(row=0, column=0, columnspan=3, sticky="nswe", padx=5, pady=5)
    main.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)


def destroy_matrix():
    global matrix
    for children in matrix.label_matrix.winfo_children():
        children.destroy()
    matrix.label_matrix.destroy()
    matrix = None

def hide_me():
    global matrix
    btn.place_forget()  # Hide the launch button
    destroy_matrix()    # Destroy the matrix screen
    dashboard()         # Show the main dashboard

# Main application setup
root = TkinterDnD.Tk()
root.geometry("1000x700")
root.title("6LACKL1ST")
root.iconbitmap("logo.ico")
root.configure(background="#1c1c1c")
root.resizable(width=True, height=True)

# Initialize the MatrixScreen
matrix = MatrixScreen(root)
matrix.update_matrix()

# Launch button
img = Image.open("./hack.ico")
btn = CTkButton(root, text="Launch", corner_radius=32, fg_color="#6a040f",
                 hover_color="#8c0715", border_color="#fffcf2",
                 border_width=2, image=CTkImage(dark_image=img), command=hide_me)
btn.place(relx=0.5, rely=0.5, anchor="center")

# Initialize the dashboard
dashboard()

# Start the main loop
root.mainloop()
                                                 