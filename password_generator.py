import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# -----------------------------
# Generate Password Function
# -----------------------------
def generate_password():
    chars = ""

    if uppercase_var.get():
        chars += string.ascii_uppercase

    if lowercase_var.get():
        chars += string.ascii_lowercase

    if numbers_var.get():
        chars += string.digits

    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    length = length_var.get()

    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():
    if password_var.get() == "":
        return

    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()

    messagebox.showinfo("Copied!", "Password copied to clipboard.")


# -----------------------------
# Window
# -----------------------------
root = tk.Tk()
root.title("Modern Password Generator")
root.geometry("450x520")
root.configure(bg="#1f1f1f")
root.resizable(False, False)

password_var = tk.StringVar()

length_var = tk.IntVar(value=16)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="🔐 Modern Password Generator",
    font=("Segoe UI", 18, "bold"),
    bg="#1f1f1f",
    fg="white"
)
title.pack(pady=20)

# -----------------------------
# Length
# -----------------------------
tk.Label(
    root,
    text="Password Length",
    bg="#1f1f1f",
    fg="white",
    font=("Segoe UI", 11)
).pack()

length_spin = ttk.Spinbox(
    root,
    from_=4,
    to=64,
    textvariable=length_var,
    width=8
)
length_spin.pack(pady=10)

# -----------------------------
# Options
# -----------------------------
frame = tk.Frame(root, bg="#1f1f1f")
frame.pack(pady=10)

tk.Checkbutton(
    frame,
    text="Uppercase Letters",
    variable=uppercase_var,
    bg="#1f1f1f",
    fg="white",
    selectcolor="#2b2b2b"
).pack(anchor="w")

tk.Checkbutton(
    frame,
    text="Lowercase Letters",
    variable=lowercase_var,
    bg="#1f1f1f",
    fg="white",
    selectcolor="#2b2b2b"
).pack(anchor="w")

tk.Checkbutton(
    frame,
    text="Numbers",
    variable=numbers_var,
    bg="#1f1f1f",
    fg="white",
    selectcolor="#2b2b2b"
).pack(anchor="w")

tk.Checkbutton(
    frame,
    text="Symbols",
    variable=symbols_var,
    bg="#1f1f1f",
    fg="white",
    selectcolor="#2b2b2b"
).pack(anchor="w")

# -----------------------------
# Generate Button
# -----------------------------
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#3B82F6",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    bd=0,
    padx=20,
    pady=10
)
generate_btn.pack(pady=20)

# -----------------------------
# Password Box
# -----------------------------
entry = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 14),
    justify="center",
    width=30
)
entry.pack()

# -----------------------------
# Copy Button
# -----------------------------
copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="#16A34A",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    bd=0,
    padx=20,
    pady=10
)
copy_btn.pack(pady=20)

root.mainloop()