from Maze import Maze
from Window import Window


def main():
    screen_x, screen_y = 800, 600
    margin = 50
    win = Window(screen_x, screen_y, "Maze Solver")
    num_row,num_col=7,7
    cell_size_x, cell_size_y =(screen_x-margin)//num_col,(screen_y-margin)//num_row
    maze = Maze(margin,margin,num_row,num_col,cell_size_x,cell_size_y,win,10)
    win.redraw()

    win.wait_for_close()


main()

