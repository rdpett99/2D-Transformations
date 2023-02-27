import transformations as tf

import basic_line_algorithm as basic

def draw_coord_system():
    basic.draw_line(1, 250, 499, 250, True)
    basic.draw_line(250, 1, 250, 499, True)

if __name__ == '__main__':
    draw_coord_system()
    basic.image.show()