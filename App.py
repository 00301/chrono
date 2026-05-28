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
        while not self.window.is_destroyed():
            self.window.update()
            self.remote.update()
            time.sleep(0.1)

    def destroy(self):
        self.remote.destroy()
        self.window.destroy()

if __name__=="__main__":
    App().play()
