# Computer Graphics CSE-4303
## Course Content
- Introduction 
- 2D concepts: [Slide](https://docs.google.com/presentation/d/1MGNEji7kmpE-0jM3T6DxQ9CYCXuhZqKqRJTtthco2Rg/edit?usp=sharing), [Colab](https://drive.google.com/file/d/1-xK6s2QdkULekYM8QJHcPT3pVwUFGwiM/view?usp=sharing), [Github](./lectures/w01_transformation_2D.ipynb)
    - Translation, Rotation, and Scaling
    - Homogeneouse coordinate systems
    - Plane equations
    - Parameteric equations
    - Matrix Representations
    - Window to viewport mapping
- Mathematics for 3D computer graphics [Colab](), [Github]()
    - Parametric equations
    - Plane equations
- 3D tranformations  [Colab](), [Github]()
    - Translation, Rotation, Scaling, and Shear
    - Composite transformations
- Viewing in 3D [Colab](), [Github]()
    - Orthographic parallel projections
    - Oblique parallel projections
    - Persective projections
    - Mathematics of 3D projections
- Representations of curves and surfaces [Colab](), [Github]()
    - Polygon meshes
    - Beizer curves and surfaces
    - Hermite curves
    - Spline curves and surfaces
- Color [Colab](), [Github]()
    - Color Spectrum
    - CIE Choromaticity
    - Color space (RGB, HSV, YIQ, YCbCr,..)
    - Color convention
- OpenGL [Colab](), [Github]()
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
- Illumination and Shading [Colab](), [Github]()
    - Illumnination models
    - Shading models for polygons
    - Shadows
    - Reflection
    - Ray tracing

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

## PyGame: Screen/Window Management
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
    
    verticies = ((-1, 0, 0), (1, 0, 0),  (0, 1, 0))
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
        draw(verticies, edges)
        pygame.display.flip()   # Output to screen
        pygame.time.wait(int(1000/freq)) # milisecond T=1/freq

main()
```
