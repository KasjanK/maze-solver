from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        
        if seed is None:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

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

    def __break_entrance_and_exit(self):
        entrance = self.__cells[0][0]
        entrance.has_top_wall = False
        self.__draw_cell(0, 0)
        exit = self.__cells[-1][-1]
        exit.has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
    
    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []

            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return

            random_direction = random.randrange(len(to_visit))
            chosen_cell = to_visit[random_direction]

            if chosen_cell[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            if chosen_cell[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            if chosen_cell[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            if chosen_cell[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False

            self.__break_walls_r(chosen_cell[0], chosen_cell[1])
            
    def __reset_cells_visited(self):
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[i])):
                self.__cells[i][j].visited = False

    def solve(self):
        solved = self._solve_r(i=0, j=0)
        if solved:
            return True
        return False
    
    def _solve_r(self, i, j):
        self.animate()
        self.__cells[i][j].visited = True

        if self.__cells[i][j] == self.__cells[self.__num_cols - 1][self.__num_rows - 1]:
            return True
        
        if i < self.__num_cols - 1 and self.__cells[i][j].has_right_wall == False and self.__cells[i + 1][j].has_left_wall == False and not self.__cells[i + 1][j].visited:
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            next_cell = self._solve_r(i + 1, j)
            if next_cell:
                return True
            self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        if i > 0 and self.__cells[i][j].has_left_wall == False and self.__cells[i - 1][j].has_right_wall == False and not self.__cells[i - 1][j].visited:
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            next_cell = self._solve_r(i - 1, j)
            if next_cell:
                return True
            self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        if j < self.__num_rows - 1 and self.__cells[i][j].has_bottom_wall == False and self.__cells[i][j + 1].has_top_wall == False and not self.__cells[i][j + 1].visited:
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            next_cell = self._solve_r(i, j + 1)
            if next_cell:
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        if j > 0 and self.__cells[i][j].has_top_wall == False and self.__cells[i][j - 1].has_bottom_wall == False and not self.__cells[i][j - 1].visited:
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            next_cell = self._solve_r(i, j - 1)
            if next_cell:
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)
        return False