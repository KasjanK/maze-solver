from window import Line, Point

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return 
        
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")

    
    def draw_move(self, to_cell, undo=False):
        self_x_center = (self.__x1 + self.__x2) // 2
        self_y_center = (self.__y1 + self.__y2) // 2

        to_cell_x_center = (to_cell.__x1 + to_cell.__x2) // 2
        to_cell_y_center = (to_cell.__y1 + to_cell.__y2) // 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        if self.__win is None:
            return

        self.__win.draw_line(Line(Point(self_x_center, self_y_center), Point(to_cell_x_center, to_cell_y_center)), fill_color)