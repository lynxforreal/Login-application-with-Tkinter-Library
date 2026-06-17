import sqlite3


import os
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect("king.db")

cursor = conn.cursor()



cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT , text TEXT )")

conn.commit()

def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        print("Lutfen bos alanlari doldurunuz!")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?,?) ", (username,password))
        conn.commit()
        messagebox.showinfo("Tebrikler", "basariyla kaydiniz olusturuldu.")

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Bu kullanici adi zaten mevcut.")

# --- GUI olusturma kismi 


root = tk.Tk()
root.title("Register page")
root.geometry("500x450")

#Kullanici adi alani

tk.Label(root, text = "Kullanici adi").pack()
entry_username = tk.Entry(root)
entry_username.pack()

#Sifre girme alanlari


tk.Label(root, text= "Sifre").pack()
entry_password = tk.Entry(root, show = "*")

entry_password.pack()

tk.Button(root, text="Kayıt Ol", command=register_user).pack()

root.mainloop()

