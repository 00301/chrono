from clock import Clock
from digit_code import DigitCode

import tkinter as tk

class MainWindow:
    def __init__(self) -> None:
        self.is_alive = True
        self.window = tk.Tk()
        self.window.title("chrono")
        self.window.geometry("1080x720")
        self.window.minsize(1080, 720)
        self.window.config(bg= '#000000')

        self.clock = Clock(self.window, 40, 10)
        self.code = DigitCode(self.window, 60, 200, self.handle_Ok)

        self.txt_end: tk.Label= tk.Label(self.window, text= "FIN", font= ("Helvetica", 60), bg= "#000000", fg= "#FFFFFF")

    def toggle_play(self):
        return self.clock.toggle_play()

    def update(self):
        self.clock.update()
        self.code.update()
        self.window.update()

    def handle_Ok(self):
        self.clock.toggle_play()
        self.txt_end.pack(anchor= "center")

    def reset(self):
        self.txt_end.pack_forget()
#        self.clock.reset()

    def destroy(self):
        self.is_alive = False
        self.window.destroy()
