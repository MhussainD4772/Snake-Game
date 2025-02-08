from settings import SPACE_SIZE, BODY_PARTS
from tkinter import Canvas

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        COLORS = ["#FFFFFF", "#DDDDDD", "#BBBBBB", "#999999", "#777777"]  # Gradient effect

        for i in range(self.body_size):
            x = (i + 1) * SPACE_SIZE
            y = SPACE_SIZE
            self.coordinates.append([x, y])

        for index, (x, y) in enumerate(self.coordinates):
            color = COLORS[min(index, len(COLORS) - 1)]  # Apply gradient color
            segment = self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                              fill=color, outline="black", width=2, tag="snake")
            self.squares.append(segment)

