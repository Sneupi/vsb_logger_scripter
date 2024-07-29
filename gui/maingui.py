import tkinter as tk
from .statpanel import StatPanel

class MainGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VSB Logger")
        self.geometry("300x200")
        
        self.stat_panel = StatPanel(self)
        self.stat_panel.pack(fill=tk.BOTH, expand=True)
        
        self.label = tk.Label(self, text="ENTER A COMMAND:")
        self.label.pack(fill=tk.BOTH, expand=True)
        
        self.cli = tk.Entry(self)
        self.cli.pack(fill=tk.BOTH, expand=True)
        
    def set_send_func(self, send_func):
        self.cli.bind("<Return>", send_func)
    
    def get_cli_entry(self):
        entry = self.cli.get() + '\n'
        self.cli.delete(0, tk.END)
        return entry
    
    def insert_cli(self, msg):
        self.cli.insert(msg)
        
    def set_led(self, name, state):
        self.stat_panel.set_led(name, state)
    
    def set_stat(self, name, text):
        self.stat_panel.set_stat(name, text)
        