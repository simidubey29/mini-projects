import tkinter as tk
from tkinter import messagebox
import random
import string

passwords = {}

# Load existing passwords
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":", 1)
            passwords[website] = pwd
except FileNotFoundError:
    pass

# Generate password
def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Save password
def save_password():
    site = website_entry.get()
    pwd = password_entry.get()

    if site == "" or pwd == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    passwords[site] = pwd

    with open("passwords.txt", "a") as file:
        file.write(f"{site}:{pwd}\n")

    messagebox.showinfo("Success", f"Password saved for {site}")

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# View passwords
def view_passwords():
    if not passwords:
        messagebox.showinfo("Info", "No passwords stored")
        return

    result = ""
    for site, pwd in passwords.items():
        result += f"{site} : {pwd}\n"

    messagebox.showinfo("Saved Passwords", result)

# GUI setup
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")

# Labels
tk.Label(root, text="Website").pack(pady=5)
website_entry = tk.Entry(root, width=30)
website_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
tk.Button(root, text="Save Password", command=save_password).pack(pady=5)
tk.Button(root, text="View Passwords", command=view_passwords).pack(pady=5)

# Run app
root.mainloop()
