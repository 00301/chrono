import time
from remote import Remote
from window import MainWindow

class App:
    def __init__(self):
        self.window = MainWindow()
        self.window.update()
        self.remote = Remote(self.window)
        self.remote.update()
        
    def play(self):
        while self.window.is_alive:
            self.window.update()
            self.remote.update()
            time.sleep(0.1)

if __name__=="__main__":
    App().play()
