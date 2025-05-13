import tkinter as tk
from tkinter import ttk

class TabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabbed Interface Example")

        # Create the style for the tabs
        style = ttk.Style()
        style.theme_use('default')
        
        # Customize the TNotebook Tab style
        style.configure('TNotebook.Tab', background="#3a3f44", foreground="white", padding=[10, 5])
        style.map('TNotebook.Tab', background=[('selected', '#1d2125')])

        # Create the main notebook
        self.notebook = ttk.Notebook(root, style='TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=1)

        # Dictionary to hold references to tab frames
        self.tab_frames = {}

        # Create content frames for each tab
        self.tab_frames['tab1'] = self.create_content_frame("Content of Tab 1", "tab1")
        self.tab_frames['tab2'] = self.create_content_frame("Content of Tab 2", "tab2")
        self.tab_frames['tab3'] = self.create_content_frame("Content of Tab 3", "tab3")

        # Add tabs to the notebook
        self.notebook.add(self.tab_frames['tab1'], text='Tab 1')
        self.notebook.add(self.tab_frames['tab2'], text='Tab 2')
        self.notebook.add(self.tab_frames['tab3'], text='Tab 3')

        # Track current tab
        self.current_tab = None

        # Bind tab change event
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        # Set initial tab
        self.on_tab_change()

    def create_content_frame(self, content_text, tab_name):
        frame = tk.Frame(self.notebook, bg="#1d2125")
        label = tk.Label(frame, text=content_text, bg="#1d2125", fg="white", font=("Arial", 16))
        label.pack(pady=20)

        # Create bottom button
        button = tk.Button(frame, text=tab_name.capitalize(), command=lambda: self.on_button_click(tab_name), bg="#3a3f44", fg="white", font=("Arial", 12), bd=0)
        button.pack(side=tk.BOTTOM, pady=10)

        return frame

    def on_button_click(self, tab_name):
        print(f"Button in {tab_name} clicked")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = TabApp(root)
    root.mainloop()
