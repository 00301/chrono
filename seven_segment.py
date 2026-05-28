import tkinter as tk

class SevenSeg:
    def __init__(self, canvas: tk.Canvas, value = 0, lenght = 100, width = 5, precision = 1, color = "#FFFFFF"):
        self.canvas = canvas
        self.value = value
        self.color = color
        self.segs = [
            self.canvas.create_polygon(precision, 0,        lenght - precision, 0,          lenght - precision - width, width,              precision + width, width),
            self.canvas.create_polygon(0, precision,        width, precision + width,       width, lenght - precision - width,              0, lenght - precision),
            self.canvas.create_polygon(lenght, precision,   lenght, lenght - precision,     lenght - width, lenght - precision - width,     lenght - width, precision + width),

            self.canvas.create_polygon(
                precision + width, lenght - width,              lenght - precision - width, lenght - width,
                lenght - precision, lenght,
                lenght - precision - width, lenght + width,     precision + width, lenght + width,
                precision, lenght,
            ),

            self.canvas.create_polygon(0, lenght + precision,                   width, lenght + precision + width,              width, 2 * lenght - precision - width,          0, 2 * lenght - precision),
            self.canvas.create_polygon(lenght, lenght + precision,              lenght, 2 * lenght - precision,                 lenght - width, 2 * lenght - precision - width, lenght - width, lenght + precision + width),
            self.canvas.create_polygon(precision + width, 2 * lenght - width,   lenght - precision - width, 2 * lenght - width, lenght - precision, 2 * lenght,                 precision, 2 * lenght),
        ]

    def update(self, value):
        if self.value == value:
            return
        self.value = value
        decode = value_to_bin(value)
        for i in range(7):
            self.canvas.itemconfig(self.segs[i], state= "normal" if (decode >> i) & 1 else "hidden")

#  0-
#1|  2|
#  3-
#4|  5|
#  6-

def value_to_bin(value: int) -> int:
    return (
           0b1110111,
           0b0100100,
           0b1011101,
           0b1101101,
           0b0101110,
           0b1101011,
           0b1111011,
           0b0100101,
           0b1111111,
           0b1101111,
       )[value] if 0 <= value <= 9 else 0
