import tkinter as tk

class LED(tk.Frame):
    def __init__(self, master, text="LED"):
        super().__init__(master)
        super().configure(width=100, height=27)
        self.label = tk.Label(self, text=text)
        self.label.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)
        self.led = tk.Frame(self, bg="dark grey", relief="solid", borderwidth=1)
        self.led.place(relx=0, rely=0, relwidth=0.1, relheight=1)
    def set_state(self, state):
        if state:
            self.led.config(bg="light green")
        else:
            self.led.config(bg="red")
        
class Stat(tk.Frame):
    def __init__(self, master, text):
        super().__init__(master)
        super().configure(width=200, height=27)
        self.label = tk.Label(self, text=text)
        self.label.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        self.stat = tk.Label(self, relief="solid", 
                                borderwidth=1, width=10)
        self.stat.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)  
    def set_text(self, text):
        self.stat.configure(text=text)

class StatPanel(tk.Frame):
    """For VSB stats"""
    def __init__(self, master):
        super().__init__(master)
        
        col1_leds = ["Run", "Balance", "Ext Bus", "MQ Dump", "Show DN"]
        col2_leds = ["Debug", "Debug 2", "Trace", "Error"]
        
        self.widgets = dict()
        
        self.col1 = tk.Frame(self)
        for text in col1_leds:
            led = LED(self.col1, text)
            led.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            self.widgets[text] = led
        self.col2 = tk.Frame(self)
        for text in col2_leds:
            led = LED(self.col2, text)
            led.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            self.widgets[text] = led
        self.col3 = tk.Frame(self)
            
        self.col1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.col2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
    def set_led(self, name, state):
        led = self.widgets.get(name, None)
        if isinstance(led, LED):
            led.set_state(state)
            
    def set_stat(self, name, text):
        stat = self.widgets.get(name, None)
        if isinstance(stat, Stat):
            stat.set_text(text)