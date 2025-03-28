from OpenGL.GL import *
from OpenGL.GLU import *
import math
import glfw
import time

prog_name = 'Example 02'
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)] 

 # for edge in edges:
        # for vi in edge:
            # glVertex3fv(verticies[vi])

def draw(verticies, edges):
    glBegin(GL_LINE_LOOP)
    # glBegin(GL_TRIANGLES)
    i = 0
    for v in verticies:
        glColor(colors[i])
        glVertex3fv(v)
        i += 1
    glEnd()


def mymain():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], prog_name, None, None)
    glfw.make_context_current(window)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    gluLookAt(5, 5, 5, # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction
    
    vertices = ((0, 0, 0), (0, 1, 0), (1,1, 0))
    edges = ((0, 1), (1,2), (2, 0))
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw(vertices, edges)
        # time.sleep(0.1)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

mymain()