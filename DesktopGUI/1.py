import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")  # Set window size

# Add a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Add a button
def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the application
root.mainloop()

