import math

# Scientific computing library for Python
# Used for matrix multiplication operator @
import numpy as np

"""
This program contains functions that can perform 2D line
transformations. Calculations are used by multiplying matrices.
"""

def basic_translate(Tx, Ty):
    """
    Returns a translation matrix, where:
        Tx : horizontal displacement
        Ty : vertical displacement
    """
    return ([1,  0,  0],
            [0,  1,  0],
            [Tx, Ty, 1])

def basic_scale(Sx, Sy):
    """
    Returns a scale matrix, where:
        Sx : horizontal scale
        Sy : vertical scale

    Assumes the center of the scale is at the origin of
    the coordinate system (0, 0).
    """
    return ([Sx, 0,  0],
            [0,  Sy, 0],
            [0,  0,  1])

def basic_rotate(angle):
    """
    Returns a rotation matix, where:
        angle : degrees to rotate clockwise

    Assumes the center of rotation is at the origin of
    the coordinate system (0, 0).
    """
    theta = math.radians(angle)
    cos0 = math.cos(theta)
    sin0 = math.sin(theta)

    return ([cos0, -sin0,  0],
            [sin0,  cos0,  0],
            [0,     0,     1])

def scale(Sx, Sy, Cx, Cy):
    """
    Returns a scale matrix, where:
        Sx : horizontal scale
        Sy : vertical scale
        Cx : x-coordinate of center of scale
        Cy : y-coordinate of center of scale
    
    Returned matrix is the product of three matrices:
    (1) a translation matrix moving toward the
    origin (Cx, Cy), (2) a basic scale matrix, and (3) 
    another translation matrix moving object back to its
    original coordinates.

          (1)              (2)             (3)

    [1,    0,  0]     [Sx, 0,  0]     [1,  0,  0]
    [0,    1,  0]  X  [0,  Sy, 0]  X  [0,  1,  0]
    [-Cx, -Cy, 1]     [0,  0,  1]     [Cx, Cy, 1]

    """
    t1_matrix = basic_translate(-Cx, -Cy)
    s_matrix = basic_scale(Sx, Sy)
    t2_matrix = basic_translate(Cx, Cy)

    return t1_matrix @ s_matrix @ t2_matrix

def rotate(angle, Cx, Cy):
    """
    Returns a rotation matrix, where:
        angle : degrees
        Cx : x-coordinate of center of rotation
        Cy : y-coordinate of center of rotation

    Returned matrix is the product of three matrices:
    (1) a translation matrix moving toward the
    origin (Cx, Cy), (2) a basic rotation matrix, and (3) 
    another translation matrix moving object back to its
    original coordinates.

          (1)                  (2)             (3)

    [1,    0,  0]     [cos0, -sin0, 0]     [1,  0,  0]
    [0,    1,  0]  X  [sin0,  cos0, 0]  X  [0,  1,  0]
    [-Cx, -Cy, 1]     [0,     0,    1]     [Cx, Cy, 1]

    """
    t1_matrix = basic_translate(-Cx, -Cy)
    r_matrix = basic_rotate(angle)
    t2_matrix = basic_translate(Cx, Cy)

    return t1_matrix @ r_matrix @ t2_matrix