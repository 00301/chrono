from seven_segment import SevenSeg
import tkinter as tk

class App:
    def __init__(self):
        self.remote = tk.Tk()
        self.remote.geometry("1080x720")
        self.remote.minsize(1080, 720)
        self.remote.config(bg= '#000000')
        self.remote.bind("<Destroy>", self.quit)
        self.is_alive = True

        self.txt_btn_play = tk.StringVar(value="Play")
        self.btn_play = tk.Button(self.remote, textvariable= self.txt_btn_play, command= self.handle_play)
        self.btn_play.pack()

        self.digit = SevenSeg(self.remote, value=4)

        self.state = False

    def quit(self, _):
        self.is_alive = False

    def update(self):
        self.remote.update()

    def cb_play(self):
        self.state = not self.state
        return self.state

    def handle_play(self):
        print("handle play")
        if self.cb_play():
            print("set pause")
            self.txt_btn_play.set("Pause")
            self.digit.set(6)
        else:
            print("set play")
            self.txt_btn_play.set("Play")
            self.digit.set(4)

if __name__ == "__main__":
    root = App()
    while root.is_alive:
        root.update()
