from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, cos, sin
import glfw
import time
import numpy as np

from libs import rotation_matrix_x, rotation_matrix_y, rad

btn_down = False
pos1 = None
cam_x, cam_y, cam_z = 3.0, 3.0, 3.0

# Callback for mouse button events
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
                gluPerspective(45, w*1.0/h, 0.1, 50.0)
                glMatrixMode(GL_MODELVIEW) 
                gluLookAt(cam_x, cam_y, cam_z, # Camera position
                0.0, 0.0, 0.0, # Look-at point
                0.0, 1.0, 0.0) # Up direction
    elif button == glfw.MOUSE_BUTTON_RIGHT:
        if action == glfw.PRESS:
            print("Right mouse button pressed")
        elif action == glfw.RELEASE:
            print("Right mouse button released")
            
# Callback for mouse movement
def cursor_position_callback(window, xpos, ypos):
    # print(f"Mouse moved to ({xpos:.1f}, {ypos:.1f})")
    pass

# Callback for mouse scroll
def scroll_callback(window, xoffset, yoffset):
    # print(f"Mouse scrolled with offsets ({xoffset:.1f}, {yoffset:.1f})")
    # Scale object
    pass

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
    gluLookAt(cam_pos[0], cam_pos[1], cam_pos[2], # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction
    
def draw_origin():
    # Draw X, Y, and Z axes
    glBegin(GL_LINES)
    
    # X-axis (red)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    
    # Y-axis (green)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    
    # Z-axis (blue)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)
    
    glEnd()


if __name__ == "__main__":
    glfw.init()
    w, h = 800, 600
    window = glfw.create_window(w, h, "Draw origin and look at it at different angles or perspective", None, None)
    glfw.make_context_current(window)
    
    # Set mouses/keyboard events
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_position_callback)
    glfw.set_scroll_callback(window, scroll_callback)
    glfw.set_key_callback(window, key_callback)
    
    setup(w, h, [cam_x, cam_y, cam_z])
    
    glClearColor(0.0, 0.0, 0.0, 1.0) # Clear screen
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear the color and depth buffers
        draw_origin()
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()