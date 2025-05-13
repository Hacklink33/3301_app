import tkinter as tk
from tkinter import ttk
import hashlib
from tkinter import messagebox

root = tk.Tk()
root.title("Dark Themed Interface")
root.geometry("400x300")
root.configure(bg='#1e1e1e')

style = ttk.Style()
style.theme_use('clam')  
style.configure("TLabel", background='#1e1e1e', foreground='#ffffff')
style.configure("TEntry", fieldbackground='#333333', foreground='#ffffff')
style.configure("TRadiobutton", background='#1e1e1e', foreground='#ffffff', font=('Arial', 12))
style.configure("TButton", background='#333333', foreground='#ffffff')

label = ttk.Label(root, text="Enter the path of the file to encrypt:")
label.pack(pady=10)

entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

radio_var = tk.StringVar(value="Option 1")

radio1 = ttk.Radiobutton(root, text="MD5", variable=radio_var, value="1")
radio1.pack(pady=5)

radio2 = ttk.Radiobutton(root, text="SHA-256", variable=radio_var, value="2")
radio2.pack(pady=5)

radio3 = ttk.Radiobutton(root, text="SHA-512", variable=radio_var, value="3")
radio3.pack(pady=5)

submit_btn = ttk.Button(root, text="Submit", command=lambda: hash(entry.get(), radio_var.get()))
submit_btn.pack(pady=20)

def hash(file, protocol):
    with open(file, "r") as f:
        hash_string = str(f)

    match protocol:
        case '1':
            sha_signature = hashlib.md5(hash_string.encode()).hexdigest()
        case '2':
            sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        case '3':
            sha_signature = hashlib.sha512(hash_string.encode()).hexdigest()

    messagebox.showinfo("Hash Result", sha_signature)


root.mainloop()
