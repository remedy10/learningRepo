"""Main window setting to display with my comments"""
from tkinter import Tk,BOTH,Canvas
class Window():
    """
    Creates a window and displays on the screen.
    """
    def __init__(self,width,height,title=None):
        self.root = Tk()
        #!The root widget, which is the main window and our parent window,
        #!has to be created before any other windows. Also, there can be only one root.
        self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.root.title(title)
        self.canvas=Canvas(width=width,height=height)
        self.canvas.pack()
        self.runnig=False
    def redraw(self):
        """
        this method will redraw all the graphics in the windows
        we need to tell the window when it should render to visuals
        """
        self.root.update_idletasks()
        self.root.update()
    def wait_for_close(self):
        """
        set runnig to True and execute as long as runnig state is True
        """
        self.runnig=True
        while self.runnig:
            self.redraw()
    def close(self):
        """
        close the window uses close protocol inside the constructor
        """
        self.runnig=False
