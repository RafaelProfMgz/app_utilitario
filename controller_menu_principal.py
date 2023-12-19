import tkinter as tk
from moeda import MoedaView
from clima import ClimaView
from calendario import CalendarioView
from ttkthemes import ThemedStyle

class MenuPrincipalController:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Principal")
        self.root.geometry("1080x720")  # Define o tamanho da tela
        
        self.style = ThemedStyle(self.root)
        self.setup_menu()
        
        self.moeda_button = tk.Button(self.root, text="Moedas", command=self.open_moeda)
        self.moeda_button.pack(padx=20, pady=10)
        
        self.clima_button = tk.Button(self.root, text="Clima", command=self.open_clima)
        self.clima_button.pack(padx=20, pady=10)
        
        self.calendario_button = tk.Button(self.root, text="Calendario", command=self.open_calendario)
        self.calendario_button.pack(padx=20, pady=10)
        
    def setup_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Temas", menu=self.theme_menu)

        self.themes = self.style.theme_names()
        for theme in self.themes:
            self.theme_menu.add_command(label=theme, command=lambda t=theme: self.change_theme(t))
    
    def change_theme(self, theme):
        self.style.set_theme(theme)
        self.root.configure(background=self.style.lookup(theme, 'background'))
        self.style = ThemedStyle(self.root)
        self.themes = self.style.theme_names()
        
    def open_moeda(self):
        moeda_view = MoedaView(self.root)
        moeda_view.open_moeda()
        
    def open_clima(self):
        clima_view = ClimaView(self.root)
        clima_view.open_clima()
        
    def open_calendario(self):
        calendario_view = CalendarioView(self.root)
        calendario_view.open_calendario()

