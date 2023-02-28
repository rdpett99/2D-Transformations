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

def draw_shape(shape):
    """
    Draws either a square or a triangle, determined by the
    user. 
    
    NOTE: The center of the square is (350, 100) and the center 
    of the triangle is (330, 125)
    """
    if shape.shape_name == 'square':
        basic.draw_line(300, 50, 300, 150)
        basic.draw_line(300, 50, 400, 50)
        basic.draw_line(300, 150, 400, 150)
        basic.draw_line(400, 50, 400, 150)
    elif shape.shape_name == 'triangle':
        basic.draw_line(330, 100, 360, 150)
        basic.draw_line(330, 100, 300, 150)
        basic.draw_line(300, 150, 360, 150)

    # Sets the shape's vertices
    shape.set_vertices()

def reset():
    """
    Resets the image and redraws the coordinate system.
    """
    basic.reset_image()
    draw_coord_system()

def prompt_user():
    """
    Prompts the user for input.
    """
    prompt = '\nWould you like to draw a singular line or a shape?\n'
    prompt += 'Type 1 for drawing your own line, or 2 for a pre-drawn shape: '
    answer = int(input(prompt))

    # Line
    if answer == 1:
        x0 = int(input('Enter coordinate for x0: '))
        y0 = int(input('Enter coordinate for y0: '))
        x1 = int(input('Enter coordinate for x1: '))
        y1 = int(input('Enter coordinate for y1: '))

        # Shows the line and prompts transformation
        basic.draw_line(x0, y0, x1, y1)
        basic.image.show()
        apply_line_tf(x0, y0, x1, y1)

    # Shape
    elif answer == 2:
        prompt = '\nWhat shape would you like to draw?\n'
        prompt += 'Type 1 for Square, or 2 for Triangle: '
        answer = int(input(prompt))
        if answer == 1:
            shape = Shape('square')
        elif answer == 2:
            shape = Shape('triangle')

        # Shows the starting image and applies the transformation
        draw_shape(shape)
        basic.image.show()
        apply_shape_tf(shape)

def apply_line_tf(x0, y0, x1, y1):
    """
    This function prompts the user for information regarding
    which transformation the user wishes to perform. The function
    then calculates the new vertices, draws the new line onto the
    screen.
    """
    prompt = '\nWhich transformation would you like to perform?\n'
    prompt += 'Type 1 for Translate, 2 for Scale, or 3 for Rotate: '
    answer = int(input(prompt))

    # Placeholder for final matrix
    matrix = tf.basic_translate(0, 0)

    # Translation
    if answer == 1:
        Tx = int(input('\nEnter x-displacement: '))
        Ty = int(input('Enter y-displacement: '))
        matrix = tf.basic_translate(Tx, Ty)

    # Basic Scale
    elif answer == 2:
        Sx = float(input('\nEnter x scaling factor: '))
        Sy = float(input('Enter y scaling factor: '))
        Cx, Cy = 0, 0
        matrix = tf.basic_scale(Sx, Sy)
        prompt = '\nWould you like to perform a basic scale (centered at the origin)\n'
        prompt += 'or a general scale (around specified point)?\n'
        prompt += 'Type 1 for basic scale, or 2 for general scale: '
        choice = int(input(prompt))

        # General Scale
        if choice == 2:
            print(f'\nNOTE: Center of line is ({int((x0 + x1) / 2)}, {int((y0 + y1) /2)})\n')
            Cx = int(input('Enter x-coordinate for center of scale: '))
            Cy = int(input('Enter y-coordinate for center of scale: '))
            matrix = tf.scale(Sx, Sy, Cx, Cy)
            
    # Basic Rotation
    elif answer == 3:
        angle = int(input('\nHow many degrees clockwise do you wish to rotate the line? '))
        Cx, Cy = 0, 0
        matrix = tf.basic_rotate(angle)
        prompt = '\nWould you like to perform a basic rotation (around the origin)\n'
        prompt += 'or a general rotation (around specified point)?\n'
        prompt += 'Type 1 for basic rotation, or 2 for general rotation: '
        choice = int(input(prompt))

        # General Rotation
        if choice == 2:
            print(f'\nNOTE: Center of line is ({int((x0 + x1) / 2)}, {int((y0 + y1) /2)})\n')
            Cx = int(input('Enter x-coordinate for center of rotation: '))
            Cy = int(input('Enter y-coordinate for center of rotation: '))
            matrix = tf.rotate(angle, Cx, Cy)
    
    # Calculates new vertices
    p1 = [x0, y0, 1] @ matrix
    p2 = [x1, y1, 1] @ matrix

    reset()

    # Draws new line
    basic.draw_line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))

    basic.image.show()

    prompt = '\nWould you like to perform another transformation?\n'
    prompt += 'Type 1 for yes, or 2 for no: '
    ans = int(input(prompt))
    if ans == 1:
        apply_line_tf(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))

def apply_shape_tf(shape):
    """
    This function prompts the user for information regarding
    which transformation the user wishes to perform. The function
    then calculates the new vertices, draws the new shape onto the
    screen, and updates the shape's vertices in memory.
    """
    
    # Placeholder for answer
    answer = 0
    while answer != 4:
        vertices = shape.get_vertices()
        prompt = '\nWhich transformation would you like to perform?\n'
        prompt += 'Type 1 for Translate, 2 for Scale, 3 for Rotate, or 4 to Quit: '
        answer = int(input(prompt))

        # Placeholder for final matrix
        matrix = tf.basic_translate(0, 0)

        # Translation
        if answer == 1:
            Tx = int(input('\nEnter x-displacement: '))
            Ty = int(input('Enter y-displacement: '))
            matrix = tf.basic_translate(Tx, Ty)

        # Basic Scale
        elif answer == 2:
            Sx = float(input('\nEnter x scaling factor: '))
            Sy = float(input('Enter y scaling factor: '))
            Cx, Cy = 0, 0
            matrix = tf.basic_scale(Sx, Sy)
            prompt = '\nWould you like to perform a basic scale (centered at the origin)\n'
            prompt += 'or a general scale (around specified point)?\n'
            prompt += 'Type 1 for basic scale, or 2 for general scale: '
            choice = int(input(prompt))

            # General Scale
            if choice == 2:
                print(f'\nNOTE: Center of {shape.shape_name} is {shape.get_center()}\n')
                Cx = int(input('Enter x-coordinate for center of scale: '))
                Cy = int(input('Enter y-coordinate for center of scale: '))
                matrix = tf.scale(Sx, Sy, Cx, Cy)
            
        # Basic Rotation
        elif answer == 3:
            angle = int(input('\nHow many degrees clockwise do you wish to rotate the shape? '))
            Cx, Cy = 0, 0
            matrix = tf.basic_rotate(angle)
            prompt = '\nWould you like to perform a basic rotation (around the origin)\n'
            prompt += 'or a general rotation (around specified point)?\n'
            prompt += 'Type 1 for basic rotation, or 2 for general rotation: '
            choice = int(input(prompt))

            # General Rotation
            if choice == 2:
                print(f'\nNOTE: Center of {shape.shape_name} is {shape.get_center()}\n')
                Cx = int(input('Enter x-coordinate for center of rotation: '))
                Cy = int(input('Enter y-coordinate for center of rotation: '))
                matrix = tf.rotate(angle, Cx, Cy)
            
        # Quit
        elif answer == 4:
            break

        if shape.shape_name == 'square':
            
            # Performs matrix multiplication on each vertex
            p1 = [vertices[0][0], vertices[0][1], 1] @ matrix
            p2 = [vertices[1][0], vertices[1][1], 1] @ matrix
            p3 = [vertices[2][0], vertices[2][1], 1] @ matrix
            p4 = [vertices[3][0], vertices[3][1], 1] @ matrix

            reset()

            # Draws new image based on new vertices
            basic.draw_line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
            basic.draw_line(int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]))
            basic.draw_line(int(p3[0]), int(p3[1]), int(p4[0]), int(p4[1]))
            basic.draw_line(int(p4[0]), int(p4[1]), int(p1[0]), int(p1[1]))

            # Updates the shape's vertices
            shape.update_vertices([int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]), 
                                int(p4[0]), int(p4[1])])

        elif shape.shape_name == 'triangle':

            # Performs matrix multiplication on each vertex
            p1 = [vertices[0][0], vertices[0][1], 1] @ matrix
            p2 = [vertices[1][0], vertices[1][1], 1] @ matrix
            p3 = [vertices[2][0], vertices[2][1], 1] @ matrix

            reset()

            # Draws new image based on new vertices
            basic.draw_line(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
            basic.draw_line(int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1]))
            basic.draw_line(int(p3[0]), int(p3[1]), int(p1[0]), int(p1[1]))

            # Updates the shape's vertices
            shape.update_vertices([int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), int(p3[0]), int(p3[1])])

        basic.image.show()


if __name__ == '__main__':
    draw_coord_system()
    prompt_user()