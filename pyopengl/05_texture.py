from OpenGL.GL import *
from OpenGL.GLU import *
import math
import glfw
import time
import numpy as np
from libs import rotation_matrix_x, rotation_matrix_y, rad
from PIL import Image

prog_name = 'Example 04'
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)] 
cam_x, cam_y, cam_z = 0, 0, 10

def setup(w, h):
    glLoadIdentity() # Reset the projection matrix
    gluPerspective(45, w*1.0/h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW) # Switch back to the model-view matrix
    gluLookAt(cam_x, cam_y, cam_z, # Camera position
              0.0, 0.0, 0.0, # Look-at point
              0.0, 1.0, 0.0) # Up direction

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
                setup(w,h)
               
    elif button == glfw.MOUSE_BUTTON_RIGHT:
        if action == glfw.PRESS:
            print("Right mouse button pressed")
        elif action == glfw.RELEASE:
            print("Right mouse button released")

def scroll_callback(window, xoffset, yoffset):
    global cam_x, cam_y, cam_z 
    if yoffset > 0:
        print("Scrolled Up")
        cam_z -= 1
    else:
        cam_z += 1
        print("Scrolled Down")
    w, h = glfw.get_window_size(window)
    setup(w,h)

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
    setup(w, h) # Re-setup projection and camera



def rand():
    return np.random.randint(0, 100)

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



def scale(vertices, s):
    sx, sy, sz = s
    T = np.eye(4)  
    T[:3,:3] = np.diag([sx, sy, sz])
    homo = np.vstack([vertices.T, np.ones(8)]) # 4x8 homonegeous coordinate
    new_vertices = T@homo # 4x8
    new_vertices = new_vertices.T  # 8x4
    new_vertices = new_vertices[:,:3] # 8x3
    return new_vertices 

def translate(vertices, v):
    x, y, z = v
    T = np.eye(4)  
    T[:3,3] = np.array([x, y, z])
    homo = np.vstack([vertices.T, np.ones(8)]) # 4x8 homonegeous coordinate
    new_vertices = T@homo # 4x8
    new_vertices = new_vertices.T  # 8x4
    new_vertices = new_vertices[:,:3] # 8x3
    return new_vertices


def load_texture(path):
    image = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM).convert("RGBA")
    img_data = np.array(image, dtype=np.uint8)
    width, height = image.size

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)  # Bilinear
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)  # Bilinear

    return texture_id

def draw_texture(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(-0.8, -0.8)
    glTexCoord2f(1, 0); glVertex2f( 0.8, -0.8)
    glTexCoord2f(1, 1); glVertex2f( 0.8,  0.8)
    glTexCoord2f(0, 1); glVertex2f(-0.8,  0.8)
    glEnd()

def draw_box(quads, vertices, c):
    glBegin(GL_QUADS)
    for quad in quads:
        for vi in quad:
            glColor3f(c[0], c[1], c[2])
            glVertex3fv(vertices[vi])
    glEnd()

def draw_box_texture(quads, vertices, texture_id):
    coords = [(0, 0), (1, 0), (1, 1), (0, 1)]
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    for quad in quads:
        i = 0
        for vi in quad:
            coord = coords[i]
            glTexCoord2f(coord[0], coord[1])
            glVertex3fv(vertices[vi])
            i += 1
    glEnd()

def draw_scene(quads, vertices, texture_id):
    # draw_texture(texture_id) 
    # draw_box(quads, translate(vertices, [0, 0, 1]), colors[rand()%6])
    draw_box_texture(quads, vertices, texture_id)
  
def mymain():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], prog_name, None, None)
    glfw.make_context_current(window)

    # Event handlers
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_scroll_callback(window, scroll_callback)
    glfw.set_key_callback(window, key_callback)
    
    setup(display[0], display[1])
    
    vertices = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]]) # 8x3

    quads = [ # two triangles per face
        [0, 1, 2, 3],  # bottom
        [4,5,6,7], # top
        [0, 1, 5, 4],  # front
        [2,3,7,6], # back
        [0,3,7,4], # left
        [1,2,6,7], # right
    ]

    glEnable(GL_DEPTH_TEST)  # Enable 3D depth testing
    glEnable(GL_TEXTURE_2D)

    texture_id = load_texture("image.png")
    while not glfw.window_should_close(window):
        np.random.seed(1) # keep color fixed
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1, 1, 1, 1)
        draw_origin()
        draw_grid(5,1)
        draw_scene(quads, vertices, texture_id)
        # time.sleep(0.1)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

mymain()