from cell import Cell
import time
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            inner_list = []
            for j in range(self.__num_rows):
                inner_list.append(Cell(self.__win))
            self.__cells.append(inner_list)
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        cell = self.__cells[i][j]
        x_top_left = self.__x1 + self.__cell_size_x * i
        y_top_left = self.__y1 + self.__cell_size_y * j
        cell.draw(x_top_left, y_top_left, x_top_left + self.__cell_size_x, y_top_left + self.__cell_size_y)
        self.animate()

    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
