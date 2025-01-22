import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from libs import rotation_matrix_x, rotation_matrix_y, rad
import numpy as np

btn_down = False
pos1 = None
cam_x, cam_y, cam_z = 10.0, -15.0, 30.0

# Callback for mouse button events
def mouse_button_callback(window, button, action, mods):
    global btn_down, pos1
    global cam_x, cam_y, cam_z 
    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            btn_down = True
            pos1 = glfw.get_cursor_pos(window)
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
                
                # Re-setup projection and camera after mouse event
                w, h = glfw.get_window_size(window)
                setup(w, h, [cam_x, cam_y, cam_z])
                
def setup(w, h, cam_pos):
    glLoadIdentity() # Reset the projection matrix
    gluPerspective(45, w*1.0/h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW) # Switch back to the model-view matrix
    gluLookAt(cam_pos[0], cam_pos[1], cam_pos[2], # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction

def draw_grid(n_lines=10, spacing=1.0):
    
    half_size = n_lines * spacing / 2.0
    glColor3f(0.7, 0.7, 0.7)  # Gray lines
    glBegin(GL_LINES)
    # Draw lines parallel to the X-axis (vary y)
    for i in range(n_lines + 1):
        y = -half_size + i * spacing
        glVertex3f(-half_size, y, 0)
        glVertex3f(+half_size, y, 0)

    # Draw lines parallel to the y-axis (vary x)
    for i in range(n_lines + 1):
        x = -half_size + i * spacing
        glVertex3f(x,  -half_size, 0)
        glVertex3f(x, +half_size, 0)
        
    glEnd()
    
def draw_origin(size=3.0):
    glBegin(GL_LINES)
    # X-axis (red)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(size, 0.0, 0.0)
    
    # Y-axis (green)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, size, 0.0)
    
    # Z-axis (blue)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, size)
    glEnd()
    

if __name__ == "__main__":
    glfw.init()
    w, h = 800, 600
    window = glfw.create_window(w, h, "PyOpenGL: Ground and Origin", None, None)
    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window, mouse_button_callback)

    # Configure basic OpenGL settings
    glEnable(GL_DEPTH_TEST)  # Enable 3D depth testing
    setup(w, h, [cam_x, cam_y, cam_z])
    
    # Main loop
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear the color and depth buffers
        draw_grid(n_lines=20, spacing=1.0)
        draw_origin(size=5)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
