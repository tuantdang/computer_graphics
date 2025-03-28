from OpenGL.GL import *
from OpenGL.GLU import *
import math
import glfw
import time
import numpy as np
from libs import rotation_matrix_x, rotation_matrix_y, rad

prog_name = 'Example 03'
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)] 
cam_x, cam_y, cam_z = 5, 5, 5

def mouse_button_callback(window, button, action, mods):
    global btn_down, pos1
    global cam_x, cam_y, cam_z 
    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            btn_down = True
            pos1 = glfw.get_cursor_pos(window)
            print(f"Left mouse button pressed at {pos1}")
            pass
        elif action == glfw.RELEASE:
            if btn_down and pos1 is not None:
                btn_down = False
                pos2 = glfw.get_cursor_pos(window)
                delta_x = (pos2[0]-pos1[0])/10.0
                delta_y = (pos2[1]-pos1[1])/10.0
                cam_pos = np.array([cam_x, cam_y, cam_z]).reshape([3,1]) # 3x1
                cam_x, cam_y, cam_z = rotation_matrix_x(rad(-delta_y))@rotation_matrix_y(rad(-delta_x))@cam_pos
                print("   > Mouse Event: Camera pos : ", cam_x, cam_y, cam_z)
                
                w, h = glfw.get_window_size(window)
                glLoadIdentity() # Reset the projection matrix
                gluPerspective(45, w*1.0/h, 0.1, 100.0)
                glMatrixMode(GL_MODELVIEW) 
                gluLookAt(cam_x, cam_y, cam_z, # Camera position
                0.0, 0.0, 0.0, # Look-at point
                0.0, 1.0, 0.0) # Up direction
    elif button == glfw.MOUSE_BUTTON_RIGHT:
        if action == glfw.PRESS:
            print("Right mouse button pressed")
        elif action == glfw.RELEASE:
            print("Right mouse button released")

def key_callback(window, key, scancode, action, mods):
    global cam_x, cam_y, cam_z 
    if action == glfw.PRESS:
        # print(f"Key pressed: {key}")
        pass
    elif action == glfw.RELEASE:
        # print(f"Key released: {key}")
        pass
    elif action == glfw.REPEAT:
        # print(f"Key repeated: {key}")
        pass

    # Example: Press 'Escape' to close the window
    rotation_x, rotation_y = 0, 0
    if key == glfw.KEY_LEFT and action == glfw.PRESS:
        rotation_y = 10
    elif key == glfw.KEY_RIGHT and action == glfw.PRESS:
        rotation_y = -10
    elif key == glfw.KEY_DOWN and action == glfw.PRESS:
        rotation_x = 10
    elif key == glfw.KEY_UP and action == glfw.PRESS:
        rotation_x = -10
        
    cam_pos = np.array([cam_x, cam_y, cam_z]).reshape([3,1]) # 3x1
    cam_x, cam_y, cam_z = rotation_matrix_x(rad(-rotation_x))@rotation_matrix_y(rad(-rotation_y))@cam_pos
    print("   > Key Event: Camera pos : ", cam_x, cam_y, cam_z)
    
    w, h = glfw.get_window_size(window)
    setup(w, h, [cam_x, cam_y, cam_z]) # Re-setup projection and camera

def setup(w, h, cam_pos):
   
    glLoadIdentity() # Reset the projection matrix
    gluPerspective(45, w*1.0/h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW) # Switch back to the model-view matrix
    gluLookAt(cam_x, cam_y, cam_z, # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction

def rand():
    return np.random.randint(0, 100)


def draw_scene(triangles, vertices):
    glBegin(GL_TRIANGLES)
    i = 0
    for triangle in triangles:
        for vertex in triangle:
            c = colors[i%6]
            glColor3f(c[0], c[1], c[2])
            glVertex3fv(vertices[vertex])
            i += 1
    glEnd()

def mymain():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], prog_name, None, None)
    glfw.make_context_current(window)

    # Event handlers
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_key_callback(window, key_callback)
    

    gluPerspective(45, (display[0]/display[1]), 0.1, 60.0)
    gluLookAt(cam_x, cam_y, cam_z, # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction
    glEnable(GL_DEPTH_TEST)

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
        np.random.seed(1) # keep color fixed
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_scene(triangles, vertices) # 8x3
        # time.sleep(0.1)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

mymain()