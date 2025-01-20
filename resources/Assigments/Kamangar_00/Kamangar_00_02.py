# Kamangar, Farhad
# 1000_123_456
# 2024_09_01
# Assignment_00_02


import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog


class cl_widgets:
    def __init__(self, ob_root_window, ob_world=[]):
        self.ob_root_window = ob_root_window
        self.ob_world = ob_world
        self.menu = cl_menu(self)
        self.toolbar = cl_toolbar(self)
        self.buttons_panel_01 = cl_buttons_panel_01(self)
        self.buttons_panel_02 = cl_buttons_panel_02(self)
        # Added status bar. Kamangar 2017_08_26
        self.statusBar_frame = cl_statusBar_frame(self.ob_root_window)
        self.statusBar_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.statusBar_frame.set('%s', 'This is the status bar')
        self.ob_canvas_frame = cl_canvas_frame(self)
        self.ob_world.add_canvas(self.ob_canvas_frame.canvas)


class cl_canvas_frame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master.ob_root_window, width=640, height=480, bg="yellow", bd=0, highlightthickness=0)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.canvas.bind('<Configure>', self.canvas_resized_callback)
        self.canvas.bind("<ButtonPress-1>", self.left_mouse_click_callback)
        self.canvas.bind("<ButtonRelease-1>", self.left_mouse_release_callback)
        self.canvas.bind("<B1-Motion>", self.left_mouse_down_motion_callback)
        self.canvas.bind("<ButtonPress-2>", self.right_mouse_click_callback)
        self.canvas.bind("<ButtonRelease-2>", self.right_mouse_release_callback)
        self.canvas.bind("<B2-Motion>", self.right_mouse_down_motion_callback)
        self.canvas.bind("<Key>", self.key_pressed_callback)
        self.canvas.bind("<Up>", self.up_arrow_pressed_callback)
        self.canvas.bind("<Down>", self.down_arrow_pressed_callback)
        self.canvas.bind("<Right>", self.right_arrow_pressed_callback)
        self.canvas.bind("<Left>", self.left_arrow_pressed_callback)
        self.canvas.bind("<Shift-Up>", self.shift_up_arrow_pressed_callback)
        self.canvas.bind("<Shift-Down>", self.shift_down_arrow_pressed_callback)
        self.canvas.bind("<Shift-Right>", self.shift_right_arrow_pressed_callback)
        self.canvas.bind("<Shift-Left>", self.shift_left_arrow_pressed_callback)
        self.canvas.bind("f", self.f_key_pressed_callback)
        self.canvas.bind("b", self.b_key_pressed_callback)

    def key_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s','Key pressed')

    def up_arrow_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"Up arrow was pressed")

    def down_arrow_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"Down arrow was pressed")

    def right_arrow_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"Right arrow was pressed")

    def left_arrow_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"Left arrow was pressed")

    def shift_up_arrow_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"Shift up arrow was pressed")

    def shift_down_arrow_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"Shift down arrow was pressed")

    def shift_right_arrow_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"Shift right arrow was pressed")

    def shift_left_arrow_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"Shift left arrow was pressed")

    def f_key_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"f key was pressed")

    def b_key_pressed_callback(self, event):
        self.master.statusBar_frame.set('%s',"b key was pressed")

    def left_mouse_click_callback(self, event):
        self.master.statusBar_frame.set('%s','Left mouse button was clicked. '+ \
                                        'x=' + str(event.x) + '   y=' + str(event.y))
        self.x = event.x
        self.y = event.y
        self.canvas.focus_set()

    def left_mouse_release_callback(self, event):
        self.master.statusBar_frame.set('%s','Left mouse button was released. '+ \
                                        'x=' + str(event.x) + '   y='+ str(event.y))
        self.x = None
        self.y = None

    def left_mouse_down_motion_callback(self, event):
        self.master.statusBar_frame.set('%s','Left mouse down motion. '+ \
                                        'x=' + str(event.x) + '   y='+ str(event.y))
        self.x = event.x
        self.y = event.y

    def right_mouse_click_callback(self, event):
        self.master.statusBar_frame.set('%s','Right mouse down motion. '+ \
                                        'x=' + str(event.x) + '   y='+ str(event.y))
        self.x = event.x
        self.y = event.y

    def right_mouse_release_callback(self, event):
        self.master.statusBar_frame.set('%s','Right mouse button was released. '+ \
                                        'x=' + str(event.x) + '   y='+ str(event.y))
        self.x = None
        self.y = None

    def right_mouse_down_motion_callback(self, event):
        self.master.statusBar_frame.set('%s','Right mouse down motion. '+ \
                                        'x=' + str(event.x) + '   y='+ str(event.y))
        self.x = event.x
        self.y = event.y

    def canvas_resized_callback(self, event):
        self.canvas.config(width=event.width, height=event.height)

        self.master.statusBar_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.master.statusBar_frame.set('%s', 'Canvas width = ' + str(event.width) + \
                                        '   Canvas height = ' + str(event.height))
        self.canvas.pack()
        self.master.ob_world.redisplay(self.master.ob_canvas_frame.canvas, event)


class cl_buttons_panel_01:
    def __init__(self, master):
        self.master = master
        frame = tk.Frame(master.ob_root_window)
        frame.pack()

        self.var_filename = tk.StringVar()
        self.var_filename.set('')
        self.button = tk.Button(frame, text="Hello", fg="red", command=self.say_hi)
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Ask for a string", command=self.ask_for_string)
        self.hi_there.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Ask for a float", command=self.ask_for_float)
        self.hi_there.pack(side=tk.LEFT)
        self.file_dialog_button = tk.Button(frame, text="Open File Dialog", fg="blue", command=self.browse_file)
        self.file_dialog_button.pack(side=tk.LEFT)

    def say_hi(self):
        self.master.statusBar_frame.set('%s',"hi there, everyone!")

    def ask_for_string(self):
        s = simpledialog.askstring('My Dialog', 'Please enter a string')
        self.master.statusBar_frame.set('%s',s)

    def ask_for_float(self):
        f = float(simpledialog.askfloat('My Dialog', 'Please enter a float'))

        self.master.statusBar_frame.set('%s',str(f))

    def browse_file(self):
        self.var_filename.set(tk.filedialog.askopenfilename(filetypes=[("allfiles", "*"), ("pythonfiles", "*.txt")]))
        filename = self.var_filename.get()
        self.master.statusBar_frame.set('%s',filename)


class cl_buttons_panel_02:
    def __init__(self, master):
        self.master = master
        frame = tk.Frame(master.ob_root_window)
        frame.pack()
        self.button = tk.Button(frame, text="Open Dialog", fg="blue", command=self.open_dialog_callback)
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="button 2", command=self.button2_callback)
        self.hi_there.pack(side=tk.LEFT)

    def open_dialog_callback(self):
        d = MyDialog(self.master.ob_root_window)
        self.master.statusBar_frame.set('%s',"mydialog_callback pressed. Returned results: "+str(d.result))

    def button2_callback(self):
        self.master.statusBar_frame.set('%s','button2 pressed.')


class MyDialog(tk.simpledialog.Dialog):
    def body(self, master):

        tk.Label(master, text="Integer:").grid(row=0, sticky=tk.W)
        tk.Label(master, text="Float:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(master, text="String:").grid(row=1, column=2, sticky=tk.W)
        self.e1 = tk.Entry(master)
        self.e1.insert(0, 0)
        self.e2 = tk.Entry(master)
        self.e2.insert(0, 4.2)
        self.e3 = tk.Entry(master)
        self.e3.insert(0, 'Default text')

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=1, column=3)

        self.cb = tk.Checkbutton(master, text="Hardcopy")
        self.cb.grid(row=3, columnspan=2, sticky=tk.W)

    def apply(self):
        try:
            first = int(self.e1.get())
            second = float(self.e2.get())
            third = self.e3.get()
            self.result = first, second, third
        except ValueError:
            tk.tkMessageBox.showwarning(
                "Bad input",
                "Illegal values, please try again"
            )

class cl_statusBar_frame(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()




class cl_menu:
    def __init__(self, master):
        self.master = master
        self.menu = tk.Menu(master.ob_root_window)
        master.ob_root_window.config(menu=self.menu)
        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.menu_callback)
        self.filemenu.add_command(label="Open...", command=self.menu_callback)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.menu_callback)
        self.dummymenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Dummy", menu=self.dummymenu)
        self.dummymenu.add_command(label="Item1", command=self.menu_item1_callback)
        self.dummymenu.add_command(label="Item2", command=self.menu_item2_callback)
        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.menu_help_callback)

    def menu_callback(self):
        self.master.statusBar_frame.set('%s',"called the menu callback!")

    def menu_help_callback(self):
        self.master.statusBar_frame.set('%s',"called the help menu callback!")

    def menu_item1_callback(self):
        self.master.statusBar_frame.set('%s',"called item1 callback!")

    def menu_item2_callback(self):
        self.master.statusBar_frame.set('%s',"called item2 callback!")

class cl_toolbar:
    def __init__(self, master):
        self.master = master
        self.toolbar = tk.Frame(master.ob_root_window)
        self.button = tk.Button(self.toolbar, text="Draw", width=16, command=self.toolbar_draw_callback)
        self.button.pack(side=tk.LEFT, padx=2, pady=2)
        self.button = tk.Button(self.toolbar, text="Toolbar Button 2", width=16, command=self.toolbar_callback)
        self.button.pack(side=tk.RIGHT, padx=2, pady=2)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

    def toolbar_draw_callback(self):
        self.master.ob_world.create_graphic_objects(self.master.ob_canvas_frame.canvas)
        self.master.statusBar_frame.set('%s',"called the draw callback!")

    def toolbar_callback(self):
        self.master.statusBar_frame.set('%s',"called the toolbar callback!")

