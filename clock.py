from seven_segment import SevenSeg
import time
import tkinter as tk

class Clock:
    def __init__(self, parent: tk.Misc, cb_fin, m = 45, s = 0, relx = .5, rely = .3, size = 800, color = "#FFFFFF"):
        length = size / 5
        self.canvas = tk.Canvas(parent, bg= "#000000", highlightthickness= 0)
        self.canvas.place(anchor= "center", relx= relx, rely= rely, width= size, height= length * 2)
        self.cb_fin = cb_fin
        self.t0 = None
        self.t_pause = None
        self.duration = 60 * m + s
        self.sec_u = SevenSeg(self.canvas, .9, .5, length, length / 12, length / 20, s % 10, color)
        self.sec_d = SevenSeg(self.canvas, .65, .5, length, length / 12, length / 20, s // 10, color)
        self.min_u = SevenSeg(self.canvas, .35, .5, length, length / 12, length / 20, m % 10, color)
        self.min_d = SevenSeg(self.canvas, .1, .5, length, length / 12, length / 20, m // 10, color)
        dots_radius = 15
        dots_half_distance = 40
        self.dots = (
            self.canvas.create_polygon(
                size / 2, length - dots_half_distance - dots_radius,    size / 2 + dots_radius, length - dots_half_distance,
                size / 2, length - dots_half_distance + dots_radius,    size / 2 - dots_radius, length - dots_half_distance,
            fill= color),
            self.canvas.create_polygon(
                size / 2, length + dots_half_distance - dots_radius,    size / 2 + dots_radius, length + dots_half_distance,
                size / 2, length + dots_half_distance + dots_radius,    size / 2 - dots_radius, length + dots_half_distance,
            fill= color),
        )

    @property
    def m_s(self) -> tuple[int, int]:
        if self.t0 is None:
            return self.duration.__divmod__(60)
        elif self.t_pause is None:
            return int(self.duration - time.monotonic() + self.t0).__divmod__(60)
        return int(self.duration - self.t_pause + self.t0).__divmod__(60)

    def update(self):
        m, s = self.m_s
        if m < 0:
            self.pause()
            self.cb_fin()
            return
        self.sec_u.set(s % 10)
        self.sec_d.set(s // 10)
        self.min_u.set(m % 10)
        self.min_d.set(m // 10)
        self.canvas.update()

    def reset(self):
        self.t0 = None
        self.t_pause = None

    def is_paused(self):
        return self.t_pause is None

    def start(self):
        self.t0 = time.monotonic()
        self.t_pause = None

    def pause(self):
        if self.t0 is not None and self.t_pause is None:
            self.t_pause = time.monotonic()

    def toggle_play(self):
        if self.t0 is None:
            self.start()
        elif self.t_pause is None:
            self.t_pause = time.monotonic()
        else:
            self.t0 += time.monotonic() - self.t_pause
            self.t_pause = None
        return self.t0 is not None and self.t_pause is None
