import tkinter as tk
from controller_moeda import MoedaController

class MoedaView:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")


    def open_moeda(self):
        moeda_window = tk.Toplevel(self.root)
        moeda_window.title("Seleção de Moedas")
        moeda_window.geometry("1080x720")
        controller = MoedaController(moeda_window)
