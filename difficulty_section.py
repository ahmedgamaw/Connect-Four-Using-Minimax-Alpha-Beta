import tkinter as tk
import os

# Specify the paths to the Python files
python_files_path = "C:/Users/HP/Desktop/python/"
connect4_with_ai_file = "connect4_with_ai.py"
advanced = "advanced.py"
intermediate = "intermediate.py"
beginner = "beginner.py"
def open_connect4_with_ai(difficulty):
    # Command for opening Connect4 with AI based on selected difficulty
    if difficulty == "beginner":
        os.system(f"C:/Users/HP/AppData/Local/Programs/Python/Python312/Scripts/python.exe {python_files_path}{beginner} beginner")
    elif difficulty == "intermediate":
        os.system(f"C:/Users/HP/AppData/Local/Programs/Python/Python312/Scripts/python.exe {python_files_path}{intermediate} intermediate")
    elif difficulty == "advanced":
        os.system(f"C:/Users/HP/AppData/Local/Programs/Python/Python312/Scripts/python.exe {python_files_path}{advanced} advanced")

def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Difficulty Selection")

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
frame = tk.Frame(root, bg="black", bd=0)
frame.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.4, anchor="n")

# Create the buttons with custom style
button_style = {"bg": "black", "fg": "white", "font": ("Helvetica", 14), "bd": 0}

button_beginner = tk.Button(frame, text="Beginner", command=lambda: open_connect4_with_ai("beginner"), **button_style)
button_beginner.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.2, anchor="n")

button_intermediate = tk.Button(frame, text="Intermediate", command=lambda: open_connect4_with_ai("intermediate"), **button_style)
button_intermediate.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.2, anchor="n")

button_advanced = tk.Button(frame, text="Advanced", command=lambda: open_connect4_with_ai("advanced"), **button_style)
button_advanced.place(relx=0.5, rely=0.7, relwidth=0.8, relheight=0.2, anchor="n")

# Run the main event loop
root.mainloop()
