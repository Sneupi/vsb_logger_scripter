
import tkinter as tk
from .selector import FileSelector
from .connector import SerialConnector

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.selector = FileSelector(self, text="Logfile")
        self.selector.pack()
        self.connector = SerialConnector(self)
        self.connector.pack()
        self.protocol("WM_DELETE_WINDOW", lambda: quit())
    
    def set_connect_button(self, command):
        self.connector.set_connect_button(command)
    def get_port(self):
        return self.connector.get_port()
    def get_baud(self):
        return self.connector.get_baud()
    def get_path(self):
        return self.selector.get_path()