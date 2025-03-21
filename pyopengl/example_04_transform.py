from OpenGL.GL import *
from OpenGL.GLU import *
import math
import glfw
import time
import numpy as np

prog_name = 'Example 04'
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)] 

def rand():
    return np.random.randint(0, 100)

def draw_box(triangles, vertices, c):
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        glColor3f(c[0], c[1], c[2])
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_scene(triangles, vertices):
    vertices0 = vertices
    T = np.eye(4)
    T[:3,3] = np.array([2, 0, 0])
    for i in range(10):
        homo = np.vstack([vertices0.T, np.ones(8)]) # 4x8 homonegeous coordinate
        T[:3,3] = np.array([2*i, 0,  0])
        vertices = T@homo # 4x8
        vertices = vertices.T  # 8x4
        vertices = vertices[:,:3] # 8x3
        draw_box(triangles, vertices, colors[rand()%6])
    
    # First column
    for i in range(10):
        homo = np.vstack([vertices0.T, np.ones(8)]) # 4x8 homonegeous coordinate
        T[:3,3] = np.array([0, 2*i, 0])
        vertices = T@homo # 4x8
        vertices = vertices.T  # 8x4
        vertices = vertices[:,:3] # 8x3
        draw_box(triangles, vertices, colors[rand()%6])

    # Second column (last)
    vertices1 = vertices0[:, :3] + np.array([2*10, 0, 0]) # 8x3
    for i in range(10):
        homo = np.vstack([vertices1.T, np.ones(8)]) # 4x8 homonegeous coordinate
        T[:3,3] = np.array([0, 2*i, 0])
        vertices = T@homo # 4x8
        vertices = vertices.T  # 8x4
        vertices = vertices[:,:3]
        draw_box(triangles, vertices, colors[rand()%6])

def mymain():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], prog_name, None, None)
    glfw.make_context_current(window)
    gluPerspective(45, (display[0]/display[1]), 0.1, 60.0)
    gluLookAt(30, 30, 30, # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction
    
    vertices = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]]) # 8x3

    triangles = [ # two triangles per face
        [0, 1, 2], [2, 3, 0],  # Back face
        [4, 5, 6], [6, 7, 4],  # Front face
        [0, 4, 7], [7, 3, 0],  # Left face
        [1, 5, 6], [6, 2, 1],  # Right face
        [3, 2, 6], [6, 7, 3],  # Top face
        [0, 1, 5], [5, 4, 0]   # Bottom face
    ]

    glEnable(GL_DEPTH_TEST)  # Enable 3D depth testing
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_scene(triangles, vertices) # 8x3
        # time.sleep(0.1)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

mymain()