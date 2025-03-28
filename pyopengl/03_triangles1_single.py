from OpenGL.GL import *
from OpenGL.GLU import *
import math
import glfw
import time


prog_name = 'Example 03'
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)] 

def draw_box(triangles, vertices):
    glBegin(GL_TRIANGLES)
    i = 0
    for triangle in triangles:
        c = colors[int(i/2)]
        for vi in triangle: # vi: vertex index
            glColor3f(c[0], c[1], c[2])
            glVertex3fv(vertices[vi])
        i += 1
    glEnd()


def mymain():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], prog_name, None, None)
    glfw.make_context_current(window)
    gluPerspective(30, (display[0]/display[1]), 0.1, 50.0)
    gluLookAt(15, 15, 15, # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction
    glEnable(GL_DEPTH_TEST)
    vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]]

    triangles = [
    [0, 1, 2], [2, 3, 0],  # Back face
    [4, 5, 6], [6, 7, 4],  # Front face
    [0, 4, 7], [7, 3, 0],  # Left face
    [1, 5, 6], [6, 2, 1],  # Right face
    [3, 2, 6], [6, 7, 3],  # Top face
    [0, 1, 5], [5, 4, 0]   # Bottom face
]
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_box(triangles, vertices)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

mymain()