from DrawingPanel import *

def draw_face():
    panel = DrawingPanel(220, 150)
    panel.draw_oval(10, 30, 100, 100, "black")
    panel.fill_oval(30, 60, 20, 20, "blue")
    panel.fill_oval(70, 60, 20, 20, "blue")
    panel.draw_line(40, 100, 80, 100, "red")

def draw_modified_face(panel, offset = 0):
    panel.draw_oval(10 + offset, 30 + offset, 100, 100, "black")
    panel.fill_oval(30 + offset, 60 + offset, 20, 20, "blue")
    panel.fill_oval(70 + offset, 60 + offset, 20, 20, "blue")
    panel.draw_line(40 + offset, 100 + offset, 80, 100, "red")

def main():
    panel_1 = DrawingPanel(320, 180)
    # draw_face()
    draw_modified_face(panel_1)
    draw_modified_face(panel_1, 140)

main()