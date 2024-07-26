from .graph import Graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import datetime

class TkGraph(tk.Frame):
    """Generic tkinter.Frame LiveGraph using graph.LiveGraph.
    
    NOTE: Enforces datetime units of width."""
        
    def append(self, line_name, y):
        x = datetime.datetime.now()
        self.graph.append(line_name, x, y)
        
    def draw(self):
        self.graph.draw()
    
    def autoscale(self):
        self.graph.autoscale()
        
    def __init__(self, master, interval):
        super().__init__(master)
        
        def manual_scroll(event):
            self.graph.set_xlim_to_relx(self.scroll_slider.get()/100)
            
        def update_width(event=None):
            time_units = {
                "Seconds": 1,
                "Minutes": 60,
                "Hours": 3600,
                "Days": 86400
            }
            unit = self.unit_var.get()
            width = self.width_slider.get() * time_units[unit]
            self.graph.set_width(datetime.timedelta(seconds=width))
        default_seconds = 10
        self.graph = Graph(width=datetime.timedelta(seconds=default_seconds), interval=interval)
        self.canvas = FigureCanvasTkAgg(self.graph.fig, master=self)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=10, sticky=tk.NSEW)
        
        self.scroll_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scroll_slider.set(100)
        self.scroll_slider.bind("<B1-Motion>", manual_scroll)
        self.scroll_slider.grid(row=1, column=2, columnspan=8, sticky=tk.NSEW)
        
        time_units = ["Seconds", "Minutes", "Hours", "Days"]
        self.unit_var = tk.StringVar(self)
        self.unit_var.set(time_units[0])
        self.unit_menu = tk.OptionMenu(self, self.unit_var, *time_units)
        self.unit_menu.grid(row=2, column=0, sticky=tk.NSEW)
        
        self.unit_updater_button = tk.Button(self, text="Update Units", 
                                             command=update_width)
        self.unit_updater_button.grid(row=2, column=1, sticky=tk.NSEW)
        
        self.width_slider = tk.Scale(self, from_=1, to=100, orient=tk.HORIZONTAL)
        self.width_slider.grid(row=2, column=2, columnspan=8, sticky=tk.NSEW)
        self.width_slider.bind("<B1-Motion>", update_width)
        self.width_slider.set(default_seconds)
    
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=4, column=0, columnspan=10, sticky=tk.NSEW)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)
        self.grid_columnconfigure(8, weight=1)
        self.grid_columnconfigure(9, weight=1)
        
