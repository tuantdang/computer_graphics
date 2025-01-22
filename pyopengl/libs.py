from math import pi, sin, cos
import numpy as np

def rad(deg):
    return (deg/180.0)*pi

def rotation_matrix_x(theta):
    return np.array([
        [1, 0, 0],
        [0, cos(theta), -sin(theta)],
        [0, sin(theta), cos(theta)]
    ])

def rotation_matrix_y(theta):
    return np.array([
        [cos(theta), 0, sin(theta)],
        [0, 1, 0],
        [-sin(theta), 0, cos(theta)]
    ])
    