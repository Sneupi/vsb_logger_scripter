import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def on_close(self):
        self.quit()
        self.destroy()
        