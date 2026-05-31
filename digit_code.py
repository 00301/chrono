import tkinter as tk

class DigitCode:
    def __init__(self, parent: tk.Misc, relx = .5, rely = .8, width = 600, height = 100, cb_Ok = None, code = "0000") -> None:
        self.frame = tk.Frame(parent, bg= "#000000", highlightthickness= 0)
        self.frame.place(anchor= "center", relx= relx, rely= rely, width= width, height= height)
        self.code = code
        self.cb_Ok = cb_Ok
        self.btn_Ok: tk.Button = tk.Button(self.frame, justify= "center", font= ("TkDefaultFont", 40), text= "Ok", command= self.handle_Ok)
        self.btn_Ok.place(anchor= "ne", relx= 1, width= width / 6, height= height)
        self.entries: list[tuple[tk.StringVar, tk.Entry]] = []
        for i in range(3, -1, -1):
            (text, entry) = make_entry(self.frame, self.btn_Ok if i == 3 else self.entries[0][1])
            entry.place(anchor= "nw", x= width * i / 5, width= width / 6, height= height)
            self.entries.insert(0, (text, entry))

    def get_entry(self) -> str:
        text = ""
        for (entry, _) in self.entries:
            text += entry.get()
        return text

    def handle_Ok(self):
        if self.cb_Ok is not None and self.get_entry() == self.code:
            self.cb_Ok()
        else:
            self.reset()

    def reset(self):
        for (txt, _) in self.entries:
            txt.set("")

    def update(self):
        self.frame.update()

def make_entry(parent, next):
    def handle_new(new):
        if new == "":
            return True
        if len(new) == 1 and new.isdigit():
            next.focus_set()
            return True
        return False
    text = tk.StringVar(parent)
    return text, tk.Entry(parent, textvariable= text, font= ("Helvetica", 60), bg= "#FFFFFF", fg= "#000000", width= 1, justify= "center",
        validate= "key", validatecommand= (parent.register(handle_new), "%P"))
