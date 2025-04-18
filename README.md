# Computer Graphics CSE-4303
## Course Content
- Introduction 
- 2D concepts: [Prensetation](https://docs.google.com/presentation/d/1MGNEji7kmpE-0jM3T6DxQ9CYCXuhZqKqRJTtthco2Rg/edit?usp=sharing), [Colab](https://drive.google.com/file/d/1-xK6s2QdkULekYM8QJHcPT3pVwUFGwiM/view?usp=sharing), [Github](./lectures/w01_transformation_2D.ipynb)
    - Translation, Rotation, and Scaling
    - Homogeneouse coordinate systems
    - Parameteric equations
    - Matrix Representations
    - Window to viewport mapping
- Mathematics for 3D computer graphics [Prensetation](https://docs.google.com/presentation/d/1MWN8l9k9yp7jfqrLcmu_S6ZBk4wUV6mJsrQU2QlmYLg/edit?usp=sharing), [Github](./lectures/w02_transformations_3d.ipynb)
    - Translation, Rotation, Scaling, and Shear
    - Parametric equations
    - Plane equations
- Ray Tracing in 3D [Presentation](https://docs.google.com/presentation/d/1KEyEC6XwHQQ4_4_4CPQQZYsCvhDZ_KVZredCO5qUJcc/edit?usp=sharing)
- Viewing in 3D [Presentation](https://docs.google.com/presentation/d/1PX-xB3Dq85WCFlGrUqTcU7vpUSrcpdWnWYD3mtZt_sc/edit?usp=sharing)
    - Orthographic parallel projections
    - Oblique parallel projections
    - Persective projections
    - Mathematics of 3D projections
- OpenGL [Presentation](https://docs.google.com/presentation/d/1WPaBRilkudP9_lZu-ZzdKDV9RXrC7PcDIJAiCUflW1M/edit?usp=sharing), [Github](https://github.com/tuantdang/computer_graphics/tree/main/pyopengl)
    - Facts and concepts
    - Naming convention
    - Installation
    - Primitives
    - Lighting and Shading
    - Texture
    - Display Lists
    - Packages
    - Vertex Shader
    - Fragment Shader

- Color [Presentation](https://docs.google.com/presentation/d/1FHPablbHqjgxAHElu0Qdc26aEVnKZXK2P_wxs0reYWY/edit?usp=sharing)
    - Color Spectrum
    - CIE Choromaticity
    - Color space (RGB, HSV,..)
    - Color convention

- Representations of curves and surfaces [Presentation](https://docs.google.com/presentation/d/16PCGXMSTZYRbRHy1DjQa3qLRYwip3Crklj5XEUCdhCc/edit?usp=sharing)
    - Polygon meshes
    - Beizer curves and surfaces
    - Hermite curves and surfaces

## Notes
- Explanation and Code posted at Colab can help you quickly to understand concepts and try out them for deeper understanding.
- Code in Github sometimes take extra steps (i.e, eviroment setup, library installations, boostrap code,..) to run since it aims to compensate functionalities that cannot be done in Colab environments. 

## Tools
- Google Colab
- Python Jupiter Notebook
- Libraries: numpy, sympy, OpenGL

## PyOpenGL: Python wraper for C/C++ OpenGL
### Installation:
```
pip install PyOpenGL PyOpenGL_accelerate
```

###  Python bindings for GLFW
Installation
```
pip install PyOpenGL glfw
```

``` python
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

def main():
    glfw.init()
    display = (800,600)
    window = glfw.create_window(display[0], display[1], "Hello Triangle with glfw", None, None)
    glfw.make_context_current(window)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    vertices = ((-1, 0, 0), (1, 0, 0),  (0, 1, 0))
    edges = ((0, 1), (1,2), (2, 0))
    freq = 10 # hz
    while not glfw.window_should_close(window):
        alpha = (2*math.pi)/6 # Rotation resulotion
        glRotatef(alpha, 0, 0, 1) # Rotate an angle alpha (rad) around vector(0, 0, 1) 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw(vertices, edges)
        time.sleep(1.0/freq)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()
main()
```

#### Another Example:
```
python .\pyopengl\cube.py
```
![](./images/3dcube_lines.png)

```
cd pyopengl
python ground.py
```
![](./images/ground3d.png)

## Alernative Window System: PyGame: Screen/Window Management
### Installation:
```
python3 -m pip install -U pygame==2.6.0
```
More [https://www.pygame.org/docs/](https://www.pygame.org/docs/)

## Simple Example using PyGame and OpenGL
### Rotate a triangle
``` python
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw(verticies, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vi in edge:
            glVertex3fv(verticies[vi])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    
    vertices = ((-1, 0, 0), (1, 0, 0),  (0, 1, 0))
    edges = ((0, 1), (1,2), (2, 0))
    freq = 10 # hz
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        alpha = (2*math.pi)/6 # Rotation resulotion
        glRotatef(alpha, 0, 0, 1) # Rotate an angle alpha (rad) around vector(0, 0, 1) 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw(vertices, edges)
        pygame.display.flip()   # Output to screen
        pygame.time.wait(int(1000/freq)) # milisecond T=1/freq

main()
```
