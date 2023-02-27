import basic_line_algorithm as basic

class Shape:

    def __init__(self, shape: str):
        self.shape_name = shape

    def get_vertices(self):
        self.vertices = []
        if self.shape_name == 'square':
            self.vertices = [(300, 50), (300, 150), (400, 150), (400, 50)]
        elif self.shape_name == 'triangle':
            self.vertices = [(330, 100), (360, 150), (300, 150)]
        return self.vertices