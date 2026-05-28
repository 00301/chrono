import tkinter as tk

class DigitCode:
    def __init__(self, parent, x, y, cb_Ok) -> None:
        self.frame = tk.Frame(parent, padx= x, pady= y)
        self.frame.bind("<key>", self.handle_key)
        self.x = x
        self.y = y

        self.code = "0944"
        self.cb_Ok = cb_Ok
        self.entries: list[tuple[tk.StringVar, tk.Entry]] = []
        for i in range(4):
            text = tk.StringVar()
            entry = tk.Entry(self.frame, textvariable= text, font= ("Helvetica", 15), bg= "#FFFFFF", fg= "#000000", width= 1, justify= "center")
            entry.pack(padx= 50 + 25 * i, pady= 20, side= "bottom")
            self.entries.append((text, entry))
        
        self.btn_Ok: tk.Button = tk.Button(self.frame, text= "Ok", command= self.handle_Ok)
        self.btn_Ok.pack(pady= 40, side= "top")

    def handle_key(self, key: tk.Event[tk.Misc]):
        if "0" <= key.keysym <= "9" :
            pass

    def get_entry(self) -> str:
        text = ""
        for (entry, _) in self.entries:
            text += entry.get()
        return text

    def handle_Ok(self):
        if self.get_entry() == self.code:
            self.cb_Ok()
