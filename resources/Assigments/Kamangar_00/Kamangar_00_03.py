# Kamangar, Farhad
# 1000_123_456
# 2017_09_01
# Assignment_00_03

class cl_world:
    def __init__(self, objects=[], canvases=[]):
        self.objects = objects
        self.canvases = canvases
        # self.display

    def add_canvas(self, canvas):
        self.canvases.append(canvas)
        canvas.world = self

    def create_graphic_objects(self, canvas):
        self.objects.append(canvas.create_line(0, 0, canvas.cget("width"), canvas.cget("height")))
        self.objects.append(canvas.create_line(canvas.cget("width"), 0, 0, canvas.cget("height")))
        self.objects.append(canvas.create_oval(int(0.25 * int(canvas.cget("width"))),
                                               int(0.25 * int(canvas.cget("height"))),
                                               int(0.75 * int(canvas.cget("width"))),
                                               int(0.75 * int(canvas.cget("height")))))

    def redisplay(self, canvas, event):
        if self.objects:
            canvas.coords(self.objects[0], 0, 0, event.width, event.height)
            canvas.coords(self.objects[1], event.width, 0, 0, event.height)
            canvas.coords(self.objects[2], int(0.25 * int(event.width)),
                          int(0.25 * int(event.height)),
                          int(0.75 * int(event.width)),
                          int(0.75 * int(event.height)))
