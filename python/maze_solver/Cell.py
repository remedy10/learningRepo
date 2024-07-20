"""Manipulating the single cell """

from Line import Line
from Point import Point


class Cell:
    """
    Manipulating the single cell
    """

    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False
    def draw(self, x1, y1, x2, y2):
        """Draw a cell"""
        self._x1, self._y1 = x1, y1
        self._x2, self._y2 = x2, y2
        if self.has_left_wall:
            Line(canvas=self._win.canvas, point1=Point(x1, y1), point2=Point(x1, y2)).draw()
        else:
            Line(canvas=self._win.canvas, point1=Point(x1, y1), point2=Point(x1, y2)).draw()
        if self.has_top_wall:
            Line(canvas=self._win.canvas, point1=Point(x1, y1), point2=Point(x2, y1)).draw()
        else:
            Line(canvas=self._win.canvas, point1=Point(x1, y1), point2=Point(x2, y1)).draw()
        if self.has_right_wall:
            Line(canvas=self._win.canvas, point1=Point(x2, y1), point2=Point(x2, y2)).draw()
        else:
            Line(canvas=self._win.canvas, point1=Point(x2, y1), point2=Point(x2, y2)).draw()
        if self.has_bottom_wall:
            Line(canvas=self._win.canvas, point1=Point(x1, y2), point2=Point(x2, y2)).draw()
        else:
            Line(canvas=self._win.canvas, point1=Point(x1, y2), point2=Point(x2, y2)).draw()

    def get_middle(self):
        """
        returns the middle point of the cell.
        """
        return ((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)

    def draw_move(self, to_cell, undo=False):
        """
        draw a line base cell to target cell.
        """
        (x_mid, y_mid) = self.get_middle()
        (to_x_mid, to_y_mid) = to_cell.get_middle()
        line_color = "red"
        if undo:
            line_color = "gray"
        # left
        if self._x1 > to_cell._x1:
            Line(self._win.canvas,Point(self._x1, y_mid),Point(x_mid, y_mid)).draw()
            Line(self._win.canvas,Point(to_x_mid, to_y_mid),Point(to_cell.x2, to_y_mid)).draw()
        # right
        elif self._x1 < to_cell._x1:
            Line(self._win.canvas,Point(x_mid, y_mid),Point(self.x2, y_mid)).draw()
            Line(self._win.canvas,Point(to_cell.x1, to_y_mid),Point(to_x_mid, to_y_mid)).draw()
            
        # up
        elif self._y1 < to_cell._y2:
            Line(self._win.canvas,Point(x_mid, y_mid),Point(x_mid, self.y1)).draw()
            Line(self._win.canvas,Point(to_x_mid, to_cell.y2),Point(to_x_mid, to_y_mid)).draw()
            
        # down
        elif self._y1 < to_cell._y1:
            Line(self._win.canvas,Point(x_mid, y_mid),Point(x_mid, self.y2)).draw()
            Line(self._win.canvas,Point(to_x_mid, to_y_mid),Point(to_x_mid, to_cell.y1)).draw()

