from DrawingPanel import *
import random
import time

def main():
    panel = DrawingPanel(500, 500)
    STEPS = 50
    x_pos = 250
    y_pos = 250
    panel.draw_rect(x_pos, y_pos, 5, 5)

    for i in range(STEPS):
        # time.sleep(1)
        pos = random.randrange(1, 5, 1)
        if pos == 1:
            y_pos += 5
        elif pos == 2:
            y_pos -= 5
        elif pos == 3:
            x_pos -= 5
        else:
            x_pos += 5
        panel.draw_rect(x_pos, y_pos, 5, 5)

main()