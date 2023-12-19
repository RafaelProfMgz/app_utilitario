
from tkcalendar import Calendar
from datetime import date

class CalendarioController:
    def __init__(self, root):
        self.root = root
        
        # Obtém a data atual do sistema
        data_atual = date.today()
        
        # Cria o objeto de calendário com a data atual
        self.calendario = Calendar(self.root, selectmode='day', year=data_atual.year, month=data_atual.month, day=data_atual.day)
        self.calendario.pack(padx=10, pady=10)  # Ajuste os valores de padx e pady conforme necessário
