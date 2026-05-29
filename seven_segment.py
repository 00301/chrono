import tkinter as tk

class SevenSeg:
    def __init__(self, parent: tk.Misc, relx: float = .5, rely: float = .5, length: float = 100, width: float = 8,
    precision: float | int = 2, value: int = 0, color = "#FFFFFF"):
        self.canvas = tk.Canvas(parent, bg= "#000000", highlightthickness= 0)
        self.canvas.place(anchor= "center", relx= relx, rely= rely, width= length, height= 2 * length)
        self.value = 8
        self.color = color
        self.segs = [
            self.canvas.create_polygon(precision, 0,        length - precision, 0,          length - precision - width, width,              precision + width, width,
                fill= color),
            self.canvas.create_polygon(0, precision,        width, precision + width,       width, length - precision - width,              0, length - precision,
                fill= color),
            self.canvas.create_polygon(length, precision,   length, length - precision,     length - width, length - precision - width,     length - width, precision + width,
                fill= color),
            self.canvas.create_polygon(
                precision + width, length - width,              length - precision - width, length - width,
                length - precision, length,
                length - precision - width, length + width,     precision + width, length + width,
                precision, length,
                fill= color
            ),
            self.canvas.create_polygon(0, length + precision,                   width, length + precision + width,              width, 2 * length - precision - width,          0, 2 * length - precision,
                fill= color),
            self.canvas.create_polygon(length, length + precision,              length, 2 * length - precision,                 length - width, 2 * length - precision - width, length - width, length + precision + width,
                fill= color),
            self.canvas.create_polygon(precision + width, 2 * length - width,   length - precision - width, 2 * length - width, length - precision, 2 * length,                 precision, 2 * length,
                fill= color),
        ]
        self.set(value)
        self.canvas.update()

    def get(self) -> int:
        return self.value

    def set(self, value):
        if self.value == value:
            return
        self.value = value
        decode = value_to_bin(value)
        for i in range(7):
            self.canvas.itemconfig(self.segs[i], state= "normal" if (decode >> i) & 1 else "hidden")
        self.canvas.update()

    def incr(self) -> bool:
        self.set((self.value + 1) % 10)
        return self.value == 0

    def decr(self) -> bool:
        self.set((self.value - 1) % 10)
        return self.value == 9

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
