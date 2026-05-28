from seven_segment import SevenSeg
import time
import tkinter as tk

class Clock:
    def __init__(self, parent: tk.Misc, x = 0, y = 0, width = 960, height = 200, m = 45, s = 0):
        self.parent = parent
        self.canvas = tk.Canvas(parent, bg= "#000000")
        self.t0 = None
        self.t_pause = None
        self.duration = 60 * m + s
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dots_radius = 20
        self.min_d = SevenSeg(self.canvas, m // 10)
        self.min_u = SevenSeg(self.canvas, m % 10)
        self.sec_d = SevenSeg(self.canvas, s // 10)
        self.sec_u = SevenSeg(self.canvas, s % 10)
        self.dots = (
            self.canvas.create_polygon(
                width / 2 , 1,    width / 2, 1,        width / 2, 1,      width / 2, 1,
            ),
            self.canvas.create_polygon(
                width / 2 , 1,    width / 2, 1,        width / 2, 1,      width / 2, 1,
            ),
        )

    @property
    def m_s(self) -> tuple[int, int]:
        if self.t0 is None:
            return self.duration.__divmod__(60)
        return int(self.duration - time.monotonic() + self.t0).__divmod__(60)

    def update(self):
        (m, s) = self.m_s
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
        self.t_pause = None

    def toggle_play(self):
        if self.t0 is None:
            self.start()
            return True
        if self.t_pause is None:
            self.t_pause = time.monotonic()
            return False
        else:
            self.t0 += time.monotonic() - self.t_pause
            
            return True
