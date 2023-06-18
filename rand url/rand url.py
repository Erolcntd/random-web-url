import tkinter as tk
from tkinter import ttk
import random
import string
import tkinter.messagebox as messagebox

links = []

def generate_link():
    link_length = random.randint(10, 50)  # Generate a random length between 10 and 50
    letters = string.ascii_letters + string.digits + "-_"
    link = "https://www." + ''.join(random.choice(letters) for _ in range(link_length)) + ".com"
    links.append(link)
    link_listbox.delete(0, tk.END)
    for link in links:
        link_listbox.insert(tk.END, link)

def copy_link():
    selected_link = link_listbox.get(tk.ACTIVE)
    if selected_link:
        window.clipboard_clear()
        window.clipboard_append(selected_link)
        messagebox.showinfo("Copied", "The selected link has been copied.")

def clear_links():
    links.clear()
    link_listbox.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Random Link Generator")

# Update style properties
style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", background="black", foreground="black")
style.configure("TLabel", padding=10, background="black")
style.configure("TFrame", background="black")
style.configure("TListbox", padding=10)

# Create the content frame
content_frame = ttk.Frame(window)
content_frame.pack(pady=20)

# Add the link generation button
generate_button = ttk.Button(content_frame, text="Create Link", command=generate_link)
generate_button.pack(pady=10)

# Create the ListBox to display generated links
link_listbox = tk.Listbox(content_frame, width=100)
link_listbox.pack()

# Add the link copy button
copy_button = ttk.Button(content_frame, text="Copy Link", command=copy_link)
copy_button.pack(pady=10)

# Add the clear list button
clear_button = ttk.Button(content_frame, text="Clear List", command=clear_links)
clear_button.pack(pady=10)

# Set the window size
window.geometry("600x400")

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.mainloop()
