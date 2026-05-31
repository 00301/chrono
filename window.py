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
        self.window.bind("<Key>", self.handle_key)
        self.window.bind("<Destroy>", self.destroy, True)

        self.clock = Clock(self.window, self.handle_lose, m= 45, s= 0)
        self.code = DigitCode(self.window, cb_Ok= self.handle_win, code= "0944")

        self.txt_end = tk.StringVar()
        self.lbl_end: tk.Label= tk.Label(self.window, textvariable= self.txt_end, font= ("Helvetica", 180), bg= "#000000", fg= "#FFFFFF")

    def handle_key(self,  key: tk.Event[tk.Misc]):
        if key.keysym == "space":
            self.toggle_play()
        if key.keysym == "Escape":
            self.destroy()

    def toggle_play(self):
        self.clock.toggle_play()

    def is_paused(self):
        return self.clock.is_paused()

    def update(self):
        self.clock.update()
        self.code.update()
        self.window.update()

    def handle_win(self):
        self.clock.pause()
        self.txt_end.set("BRAVO !")
        self.lbl_end.place(anchor= "center", relx= .5, rely= .5, relwidth= 1, relheight= 1)

    def handle_lose(self):
        self.clock.pause()
        self.txt_end.set("VOUS AVEZ\nPERDU")
        self.lbl_end.place(anchor= "center", relx= .5, rely= .5, relwidth= 1, relheight= 1)

    def reset(self):
        self.lbl_end.place_forget()
        self.clock.reset()
        self.code.reset()

    def destroy(self, _ = None):
        self.is_alive = False
