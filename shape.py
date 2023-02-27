class Shape:
    """
    Defines a shape. In this case, a square or a triangle.
    """

    def __init__(self, shape: str):
        """
        Initializes shape.
        """
        self.shape_name = shape
        self.vertices = []

    def set_vertices(self):
        """
        Sets the default vertices.
        """
        if self.shape_name == 'square':
            self.vertices = [(300, 50), (300, 150), (400, 150), (400, 50)]
        elif self.shape_name == 'triangle':
            self.vertices = [(330, 100), (360, 150), (300, 150)]

    def get_vertices(self):
        """
        Returns the vertices for computation.
        """
        return self.vertices

    def update_vertices(self, points):
        """
        Updates the vertices after transformation has occured.
        """
        if self.shape_name == 'square':
            self.vertices = [(points[0], points[1]), (points[2], points[3]),
                             (points[4], points[5]), (points[6], points[7])]
        elif self.shape_name == 'triangle':
            self.vertices = [(points[0], points[1]), (points[2], points[3]),
                             (points[4], points[5])]