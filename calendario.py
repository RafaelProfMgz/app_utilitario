import tkinter as tk
from controller_calendario import CalendarioController

class CalendarioView:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")
        
    def open_calendario(self):
        calendario_window = tk.Toplevel(self.root)
        calendario_window.title("Calendario")
        controller = CalendarioController(calendario_window)
