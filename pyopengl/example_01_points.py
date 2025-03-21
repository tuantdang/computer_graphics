from OpenGL.GL import *
from OpenGL.GLU import *
import math
import glfw
import time

prog_name = 'Example 01'
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)] 

def draw(verticies):
    glBegin(GL_POINTS)
    i = 0
    for vi in verticies:
        c = colors[i]
        glColor(c[0], c[1], c[2])
        # glPointSize(1)
        glVertex3fv(vi)
        i += 1
    glEnd()

def mymain():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], prog_name, None, None)
    glfw.make_context_current(window)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    gluLookAt(0, 3, 3, # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction
    
    vertices = ((0, 0, 0), (0, 1, 0), (1,1, 0))
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw(vertices)
        # time.sleep(0.1)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

mymain()