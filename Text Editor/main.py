import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.font as tkFont
import textwrap

def new_file():
    text.delete("1.0", tk.END)
    root.title("Untitled - Text Editor")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
        root.title(file_path + " - Text Editor")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))
        root.title(file_path + " - Text Editor")

def save_file_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))
        root.title(file_path + " - Text Editor")

def exit_app():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def undo():
    text.event_generate("<<Undo>>")

def redo():
    text.event_generate("<<Redo>>")

def find():
    target = simpledialog.askstring("Find", "Enter text to find:")
    if target:
        start = text.search(target, "1.0", stopindex=tk.END)
        if start:
            end = f"{start}+{len(target)}c"
            text.tag_remove("sel", "1.0", tk.END)
            text.tag_add("sel", start, end)
            text.mark_set("insert", end)
            text.see("insert")

def replace():
    target = simpledialog.askstring("Replace", "Enter text to replace:")
    if target:
        with_text = simpledialog.askstring("Replace", "Replace with:")
        if with_text:
            start = text.search(target, "1.0", stopindex=tk.END)
            while start:
                end = f"{start}+{len(target)}c"
                text.delete(start, end)
                text.insert(start, with_text)
                start = text.search(target, start, stopindex=tk.END)

def wrap_text():
    wrap_value = word_wrap_var.get()
    text.config(wrap=tk.CHAR if wrap_value else tk.NONE)

def change_font():
    font_family = font_family_var.get()
    font_size = font_size_var.get()
    text.config(font=(font_family, font_size))

root = tk.Tk()
root.title("Untitled - Text Editor")
root.geometry("800x600")

text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH)

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find)
edit_menu.add_command(label="Replace", command=replace)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

format_menu = tk.Menu(menu_bar, tearoff=0)
word_wrap_var = tk.BooleanVar()
format_menu.add_checkbutton(label="Word Wrap", variable=word_wrap_var, command=wrap_text)

font_family_var = tk.StringVar()
font_family_var.set("Arial")
font_size_var = tk.IntVar()
font_size_var.set(12)
font_menu = tk.Menu(format_menu, tearoff=0)
font_menu.add_radiobutton(label="Arial", variable=font_family_var, value="Arial", command=change_font)
font_menu.add_radiobutton(label="Courier", variable=font_family_var, value="Courier", command=change_font)
font_menu.add_radiobutton(label="Verdana", variable=font_family_var, value="Verdana", command=change_font)
font_menu.add_separator()
font_menu.add_radiobutton(label="10", variable=font_size_var, value=10, command=change_font)
font_menu.add_radiobutton(label="12", variable=font_size_var, value=12, command=change_font)
font_menu.add_radiobutton(label="14", variable=font_size_var, value=14, command=change_font)
format_menu.add_cascade(label="Font", menu=font_menu)

menu_bar.add_cascade(label="Format", menu=format_menu)

root.config(menu=menu_bar)
root.mainloop()
