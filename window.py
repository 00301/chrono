import tkinter as tk
from clock import Clock

class MainWindow:
    def __init__(self) -> None:
        self.window = tk.Tk()
        #self.window.title("chrono")
        #self.window.geometry("1080x720")
        #self.window.minsize(1080, 720)
        #self.window.config(bg = '#000000')

        self.clock = Clock(self.window, None)
        self.entries: list[tuple[tk.StringVar, tk.Entry]] = []
        for i in range(4):
            text = tk.StringVar()
            entry = tk.Entry(self.window, textvariable= text, font= ("Helvetica", 15), bg= "#FFFFFF", fg= "#000000", width= 1, justify= "center")
            entry.pack(padx= 50 + 25 * i, pady= 20, side= "bottom")
            self.entries.append((text, entry))
        
        boutton_valid: tk.Button = tk.Button(self.window, text= "Ok", command= lambda: self.validate)
        boutton_valid.pack(pady= 40, side= "top")

    def toggle_play(self):
        self.clock.toggle_play()

    def update(self):
        self.window.update()

    def validate(self):
        pass

    def get_entry(self) -> str:
        text = ""
        for (entry, _) in self.entries:
            text += entry.get()
        return text

    def destroy(self):
        self.window.destroy()
