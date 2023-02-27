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
    draw_shape('triangle')
    basic.image.show()