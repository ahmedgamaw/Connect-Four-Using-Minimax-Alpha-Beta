import tkinter as tk
from tkinter import filedialog
import os

# Specify the paths to the Python files
python_files_path = "C:/Users/HP/Desktop/python/"
connect4_file = "connect4.py"
connect4_with_ai_file = "connect4_with_ai.py"
difficulty_section_file = "difficulty_section.py"  # New file for difficulty selection

def open_connect4():
    os.system(f"C:/Users/HP/AppData/Local/Programs/Python/Python312/Scripts/python.exe {python_files_path}{connect4_file}")

def open_difficulty_section():
    os.system(f"C:/Users/HP/AppData/Local/Programs/Python/Python312/Scripts/python.exe {python_files_path}{difficulty_section_file}")

def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Connect Four Menu")

# Set window size and position
window_width = 800
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a canvas for background color gradient
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Define colors for linear gradient
start_color = "#0000FF"  # Blue
end_color = "#FF0000"    # Yellow

# Create linear gradient
for i in range(window_height):
    r = int((1 - i / window_height) * int(start_color[1:3], 16) + (i / window_height) * int(end_color[1:3], 16))
    g = int((1 - i / window_height) * int(start_color[3:5], 16) + (i / window_height) * int(end_color[3:5], 16))
    b = int((1 - i / window_height) * int(start_color[5:7], 16) + (i / window_height) * int(end_color[5:7], 16))
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    canvas.create_line(0, i, window_width, i, fill=color)

# Create a frame to contain the buttons

# Create the buttons with custom style
button_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 14), "bd": 0}


button_connect4 = tk.Button(text="Open Connect4", command=open_connect4, **button_style)
button_connect4.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.2, anchor="n")

button_connect4_with_ai = tk.Button(text="Open Connect4 with AI", command=open_difficulty_section, **button_style)
button_connect4_with_ai.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.2, anchor="n")

button_exit = tk.Button(text="Exit", command=exit_program, **button_style)
button_exit.place(relx=0.5, rely=0.7, relwidth=0.8, relheight=0.2, anchor="n")

# Run the main event loop
root.mainloop()
