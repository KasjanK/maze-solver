from tkinter import Tk, BOTH, Canvas
import time

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack()

        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        x1 = self.point1.x
        y1 = self.point1.y
        x2 = self.point2.x
        y2 = self.point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
    
    def draw_move(self, to_cell, undo=False):
        self_x_center = (self.__x1 + self.__x2) // 2
        self_y_center = (self.__y1 + self.__y2) // 2

        to_cell_x_center = (to_cell.__x1 + to_cell.__x2) // 2
        to_cell_y_center = (to_cell.__y1 + to_cell.__y2) // 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        self.__win.draw_line(Line(Point(self_x_center, self_y_center), Point(to_cell_x_center, to_cell_y_center)), fill_color)

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
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
        cell = self.__cells[i][j]
        x_top_left = self.__x1 + self.__cell_size_x * i
        y_top_left = self.__y1 + self.__cell_size_y * j
        cell.draw(x_top_left, y_top_left, x_top_left + self.__cell_size_x, y_top_left + self.__cell_size_y)
        self.animate()

    def animate(self):
        self.__win.redraw()
        time.sleep(0.05)

