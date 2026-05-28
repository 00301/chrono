from seven_segment import SevenSeg
import time
import tkinter as tk

class Clock:
    def __init__(self, parent: tk.Misc, x = 0, y = 0, size = 960, m = 45, s = 0):
        self.parent = parent
        self.canvas = tk.Canvas(parent, bg= "#000000")
        self.t0 = None
        self.t_pause = None
        self.x = x
        self.y = y
        self.size = size
        self.min_d = SevenSeg(self.canvas, m // 10)
        self.min_u = SevenSeg(self.canvas, m % 10)
        self.sec_d = SevenSeg(self.canvas, s // 10)
        self.sec_u = SevenSeg(self.canvas, s % 10)
        self.dots = (self.canvas.create_polygon(1, 3, 1, 1), self.canvas.create_polygon(1, 3, 1, 1))

    def update(self, m, s):
        self.min_d.update(m // 10)
        self.min_u.update(m % 10)
        self.sec_d.update(s // 10)
        self.sec_u.update(s % 10)

    def destroy(self):
        if self.parent is not None :
            self.parent.destroy()
        if self.canvas is not None :
            self.canvas.destroy()

    def start(self):
        self.t0 = time.monotonic()

    def toggle_play(self):
        if self.t0 is None:
            return self.start()
        if self.t_pause is not None:
            self.t0 += time.monotonic() - self.t_pause
        else:
            self.t_pause = time.monotonic()
