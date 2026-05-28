import time
import tkinter as tk
from remote import Remote
from window import MainWindow

class App:
    def __init__(self):
        self.window = MainWindow()
        self.window.update()
        self.remote = Remote(self.window.)
        self.remote.update()
        
    def play(self):
        while :
            self.window.update()
            time.sleep(0.9)

    def destroy(self):
        self.clock.destroy()
        self.remote.destroy()
        self.window.destroy()

    def valider_pressed(self) -> None:
        if self.get_entry() == self.code:
            find: tk.Label= tk.Label(self.window, text= "trouvé", font= ("Helvetica", 50), bg= "#000000", fg= "#FFFFFF")
            find.pack(pady=0)
        self.window.update()

if __name__=="__main__":
    App().play()
