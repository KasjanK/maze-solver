from window import Window, Line, Point, Cell

def main():
    print("main function started")
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(30, 30, 60, 60)
    cell.draw(60, 30, 90, 60)

    #win.draw_line(cell, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()