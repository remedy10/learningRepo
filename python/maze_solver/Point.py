"""Module for point"""
class Point:
    """
    Create a point uses given coordinates and return if you want to wherever :)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def return_coords(self):
        """Return the coordinates"""
        return self.x, self.y
