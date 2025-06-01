from window import Window
from maze import Maze

def main():
    print("main function started")
    win = Window(800, 600)
    # cell = Cell(win)
    # cell2 = Cell(win)
    # cell.draw(30, 30, 60, 60)
    # cell2.draw(500, 400, 530, 430)
    # cell.draw_move(cell2)

    maze = Maze(50, 50, 5, 5, 30, 30, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()