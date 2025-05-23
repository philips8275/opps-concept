import tkinter as tk

# Function to display user input
def show_text():
    user_input = entry.get()
    label_output.config(text="You entered: " + user_input)

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")

# Create widgets
label = tk.Label(root, text="Enter something:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_text)
button.pack(pady=5)

label_output = tk.Label(root, text="")
label_output.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
