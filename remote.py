import tkinter as tk
from window import MainWindow

class Remote:
    def __init__(self, window: MainWindow) -> None:
        self.cb_play = window.toggle_play
        self.cb_reset = window.reset
        self.cb_quit = window.destroy

        self.remote = tk.Tk()
        self.remote.title("remote")
        self.remote.geometry("100x50")
        self.remote.minsize(100, 50)
        self.remote.config(bg= '#000000')
        self.remote.bind("<Key>", self.handle_key)

        self.btn_quit:tk.Button=tk.Button(self.remote, text= "Quit", command= self.cb_quit)
        self.btn_quit.pack(pady= 40, side= "bottom")

        self.txt_btn_play:tk.StringVar=tk.StringVar(value= "Play")
        
        self.btn_play:tk.Button=tk.Button(self.remote, textvariable= self.txt_btn_play, command= self.handle_play)
        self.btn_play.pack()
        
        self.btn_reset:tk.Button=tk.Button(self.remote, text= "Reset", command= self.cb_reset)
        self.btn_reset.pack(pady= 0)

    def handle_play(self):
        if self.cb_play():
            if self.txt_btn_play.get() == "Play":
                self.txt_btn_play.set("Pause")
            else:
                self.txt_btn_play.set("Play")

    def handle_key(self, key: tk.Event[tk.Misc]):
        if key.keysym == "Escape":
            self.cb_quit()
            self.destroy()

    def update(self):
        self.remote.update()

    def destroy(self):
        self.remote.destroy()
