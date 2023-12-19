import tkinter as tk
from controller_clima import ClimaController

class ClimaView:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")
        
    def open_clima(self):
        clima_window = tk.Toplevel(self.root)
        clima_window.title("Previsão do Tempo")
        clima_window.geometry("1080x720")
        controller = ClimaController(clima_window)
