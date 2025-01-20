# Kamangar, Farhad
# 1000_123_456
# 2024_09_22
# Assignment_01_01

import numpy as np
import tkinter as tk
from tkinter import simpledialog, filedialog

class cl_world:
    def __init__(self):
        ################## Main Window ########################
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title("Resizable Window")
        # Set the window gemetry (Size) and Make it resizable
        self.root.geometry("400x600")
        self.root.resizable(True, True)
        ################### Top Pnael ##########################
        # Create a top frame for the button
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        # Create a button in the top panel
        self.brwose_button = tk.Button(self.top_frame, text="Browse", fg="blue", command=self.browse_file_clicked)
        self.brwose_button.pack(side=tk.LEFT)
        self.draw_button = tk.Button(self.top_frame, text="Draw", command=self.draw_button_clicked)
        self.draw_button.pack(side=tk.LEFT, padx=10, pady=10)
        ################### Canvas #############################
        # Create a canvas to draw on
        self.canvas = tk.Canvas(self.root, bg="light goldenrod")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        # Bind the resize event to redraw the canvas when window is resized
        self.canvas.bind("<Configure>", self.canvas_resized)
        #################### Bottom Panel #######################
        # Create a bottom frame for displaying messages
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        # Create a lebel for showing messages
        self.message_label = tk.Label(self.bottom_frame, text="")
        self.message_label.pack(padx=10, pady=10)

    def browse_file_clicked(self):
        self.file_path = tk.filedialog.askopenfilename(filetypes=[("allfiles", "*"), ("pythonfiles", "*.txt")])
        self.message_label.config(text=self.file_path)
        self.load_file(self.file_path)

    def draw_button_clicked(self):
        self.draw_objects()

    def canvas_resized(self,event=None):
        if self.canvas.find_all():
            self.draw_objects(event)

    def load_file(self,filename):
        # Modify this file to complete your assignment
        pass

    def draw_objects(self,event=None):
        # Modify this file to complete your assignment
        pass
    def draw_button_clicked(self):
        self.draw_objects()
    def canvas_resized(self,event=None):
        if self.canvas.find_all():
            self.draw_objects(event)

# Run the tkinter main loop
world=cl_world()
world.root.mainloop()
