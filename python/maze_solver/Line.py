"""Module for line"""
from Point import Point


class Line:
    """
    Creates a line from a point to a point. Additional arguments are width and color. and canvas
    """
    def __init__(self, canvas, point1:Point,point2:Point, width=3, color="black"):
        self.canvas = canvas
        self.x1, self.y1 = point1.return_coords()
        self.x2, self.y2 = point2.return_coords()
        self.width = width
        self.color = color

    def draw(self):
        """
        Draw a line given coordinates to given canvas
        """
        self.canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=self.color, width=self.width
        )
        self.canvas.pack()
