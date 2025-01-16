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