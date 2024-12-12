import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Simple GUI")

# Add a label
label = tk.Label(window, text="Enter your name:").pack()

# Add an entry field
entry = tk.Entry(window).pack()

# Add a button
def on_button_click():
    user_input = entry.get()
    print(f"Hello, {user_input}!")

button = tk.Button(window, text="Submit", command=on_button_click).pack()

frame = tk.Frame(window, bg="lightblue").pack()



window.mainloop()
