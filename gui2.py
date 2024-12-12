import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title("FRAME")
Label=tk.Label(window,text="HII").pack()
Entry=tk.Entry(window).pack()
Spin=tk.Spinbox(window,from_=-45,to=80).pack()
Button=tk.Button(window,text="Click").pack()
Frame=tk.Frame(master=window,width=400,height=200,bg="pink").pack()
Frame=tk.Frame(master=window,width=400,height=200,bg="yellow").pack()
messagebox.showinfo("R U GAY?","R U GAY?")
messagebox.showinfo("R U GAY?","R U GAY?")
messagebox.showinfo("R U GAY?","R U GAY?")
messagebox.showinfo("R U GAY?","R U GAY?")


window.mainloop()
