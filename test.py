import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("All Files", "*.*")]  # You can change this to filter specific file types
    )
    if file_path:
        file_label.config(text=file_path)
        # Optional: Do something with the file (e.g., show a message or process it)
        # messagebox.showinfo("Selected File", f"You selected:\n{file_path}")
    else:
        file_label.config(text="No file selected.")

# GUI Setup
root = tk.Tk()
root.title("Choose a File")
root.geometry("500x150")

# Instructions Label
instruction = tk.Label(root, text="Click Browse to select a file:", font=("Arial", 12))
instruction.pack(pady=10)

# File path display
file_label = tk.Label(root, text="No file selected.", wraplength=450, fg="blue")
file_label.pack()

# Browse Button
browse_button = tk.Button(root, text="Browse", command=browse_file, width=15)
browse_button.pack(pady=10)

root.mainloop()
