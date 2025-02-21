from OpenGL.GL import *
from OpenGL.GLU import *
import math
import glfw
import time


def draw(verticies, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vi in edge:
            glVertex3fv(verticies[vi])
    glEnd()

def mymain():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], "Hello Triangle with glfw", None, None)
    glfw.make_context_current(window)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    vertices = ((-1, 0, 0), (1, 0, 0),  (0, 1, 0))
    edges = ((0, 1), (1,2), (2, 0))
    freq = 60 # hz
    while not glfw.window_should_close(window):
        alpha = (2*math.pi)/6 # Rotation resulotion
        glRotatef(alpha, 1, 1, 0) # Rotate an angle alpha (rad) around vector(0, 0, 1) 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw(vertices, edges)
        time.sleep(1.0/freq)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

mymain()