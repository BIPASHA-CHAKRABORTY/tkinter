import tkinter as tk
window=tk.Tk()
window.title("GUI_1")
label=tk.Label(window,text="HIIII").pack()
Entry=tk.Entry(window).pack()
spin=tk.Spinbox(window,from_=0,to=100).pack()
button=tk.Button(window,text="SUBMIT").pack()
window.mainloop()

