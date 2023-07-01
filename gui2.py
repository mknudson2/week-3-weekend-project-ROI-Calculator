import customtkinter
import tkinter as tk
# from customtkinter import Stylesheet

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Create the main window
window = customtkinter.CTk()
window.geometry("980x655")

# Define the colors
display_bg_color = "#855AE1"

# Create the top display section
top_display_frame = customtkinter.CTkFrame(window, background=display_bg_color)
top_display_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Create the left-hand column
left_column = tk.Frame(window, bg="white")
left_column.grid(row=1, column=0, rowspan=2, sticky="nsew")

# Create the middle column
middle_column = tk.Frame(window)
middle_column.grid(row=1, column=1, rowspan=2, sticky="nsew")

# Create the two sub-columns within the middle column
sub_column1 = tk.Frame(middle_column, bg="white")
sub_column1.grid(row=0, column=0, sticky="nsew")

sub_column2 = tk.Frame(middle_column, bg="white")
sub_column2.grid(row=0, column=1, sticky="nsew")

# Create the right-hand column
right_column = tk.Frame(window, bg="white")
right_column.grid(row=1, column=2, rowspan=2, sticky="nsew")

# Configure grid weights to make the widgets expand properly
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Start the main event loop
window.mainloop()
