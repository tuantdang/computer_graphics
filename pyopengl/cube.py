from OpenGL.GL import *
from OpenGL.GLU import *
import math
import glfw
import time

def draw(verticies, edges):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    for edge in edges:
        for vi in edge:
            glVertex3fv(verticies[vi])
    glEnd()

def main():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], "Hello Cube with glfw", None, None)
    glfw.make_context_current(window)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    vertices = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
               (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1))
    edges = ((0,1), (1,2), (2,3), (3,0), 
             (4,5), (5,6), (6,7), (7,4), 
             (0, 4), (1,5), (2,6), (3,7))
    
    while not glfw.window_should_close(window):
        alpha = (2*math.pi)/6 # Rotation resulotion
        glRotatef(alpha, 0, 1, 1) # Rotate an angle alpha (rad) around vector(0, 1, 1) 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw(vertices, edges)
        time.sleep(0.1)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()
main()