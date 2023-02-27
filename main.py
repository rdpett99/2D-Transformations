import numpy as np

from shape import Shape
import transformations as tf
import basic_line_algorithm as basic

def draw_coord_system():
    """
    Draws the coordinate system on the image, with the center
    of the system being at (250, 250) since the image is
    500 x 500.
    """
    basic.draw_line(1, 250, 499, 250, True)
    basic.draw_line(250, 1, 250, 499, True)

def draw_shape(shape: str):
    """
    Draws either a square or a triangle, determined by the
    user. 
    
    NOTE: The center of the square is (350, 100) and the center 
    of the triangle is (330, 125)
    """
    if shape == 'square':
        basic.draw_line(300, 50, 300, 150)
        basic.draw_line(300, 50, 400, 50)
        basic.draw_line(300, 150, 400, 150)
        basic.draw_line(400, 50, 400, 150)
    elif shape == 'triangle':
        basic.draw_line(330, 100, 360, 150)
        basic.draw_line(330, 100, 300, 150)
        basic.draw_line(300, 150, 360, 150)


if __name__ == '__main__':
    draw_coord_system()
    prompt = 'What shape would you like to draw?\n'
    prompt += 'Type 1 for Square, or 2 for Triangle: '
    answer = int(input(prompt))
    if answer == 1:
        shape = Shape('square')
    elif answer == 2:
        shape = Shape('triangle')
    draw_shape(shape.shape_name)

    vertices = shape.get_vertices()
    rotation_matrix = tf.rotate(180, 330, 125)

    p1 = [vertices[0][0], vertices[0][1], 1] @ rotation_matrix
    p2 = [vertices[1][0], vertices[1][1], 1] @ rotation_matrix
    p3 = [vertices[2][0], vertices[2][1], 1] @ rotation_matrix

    basic.draw_line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
    basic.draw_line(int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]))
    basic.draw_line(int(p3[0]), int(p3[1]), int(p1[0]), int(p1[1]))

    basic.image.show()