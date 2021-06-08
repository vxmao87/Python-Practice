from DrawingPanel import *

# face drawing example
def draw_face():
    panel = DrawingPanel(220, 150)
    panel.draw_oval(10, 30, 100, 100, "black")
    panel.fill_oval(30, 60, 20, 20, "blue")
    panel.fill_oval(70, 60, 20, 20, "blue")
    panel.draw_line(40, 100, 80, 100, "red")

# draws a face on one panel while taking optional parameters of x and y offsets
def draw_modified_face(panel, x_offset = 0, y_offset = 0):
    panel.draw_oval(10 + x_offset, 30 + y_offset, 100, 100, "black")
    panel.fill_oval(30 + x_offset, 60 + y_offset, 20, 20, "blue")
    panel.fill_oval(70 + x_offset, 60 + y_offset, 20, 20, "blue")
    panel.draw_line(40 + x_offset, 100 + y_offset, 80 + x_offset, 100 + y_offset, "red")

# draws a row of five faces
def draw_row_of_faces(panel):
    for i in range(0, 5):
        panel.draw_oval(10 + (100 * i), 30, 100, 100, "black")
        panel.fill_oval(30 + (100 * i), 60, 20, 20, "blue")
        panel.fill_oval(70 + (100 * i), 60, 20, 20, "blue")
        panel.draw_line(40 + (100 * i), 100, 80 + (100 * i), 100, "red")

def main():
    panel_1 = DrawingPanel(320, 180)
    panel_2 = DrawingPanel(520, 180)
    # draw_face()
    draw_modified_face(panel_1)
    draw_modified_face(panel_1, 140, 20)
    draw_row_of_faces(panel_2)

main()