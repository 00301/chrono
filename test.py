from digit_code import DigitCode
import tkinter as tk

class App:
    def __init__(self):
        self.remote = tk.Tk()
        self.remote.geometry("1080x720")
        self.remote.minsize(1080, 720)
        self.remote.config(bg= '#000000')
        self.remote.bind("<Destroy>", self.quit)
        self.is_alive = True

        self.digit = DigitCode(self.remote)

        self.state = False

    def quit(self, _):
        self.is_alive = False

    def update(self):
        self.remote.update()

    def cb_play(self):
        self.state = not self.state
        return self.state

if __name__ == "__main__":
    root = App()
    while root.is_alive:
        root.update()
