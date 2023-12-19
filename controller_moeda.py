import tkinter as tk
from tkinter import ttk
import requests

class MoedaController:
    def __init__(self, root):
        self.root = root

        # Listas de moedas para os ComboBoxes
        self.moedas = ['CAD','CHF','USD','EUR','JPY', 'GBP', 'BRL','MXN','RUB','NZD']  # Lista de moedas
        self.moeda_base = tk.StringVar(root)
        self.moeda_destino = tk.StringVar(root)
        self.moeda_base.set(self.moedas[0])  # Valor inicial do ComboBox base
        self.moeda_destino.set(self.moedas[1])  # Valor inicial do ComboBox destino

        # ComboBox para selecionar a moeda base
        self.moeda_base_menu = ttk.Combobox(root, textvariable=self.moeda_base, values=self.moedas)
        self.moeda_base_menu.pack()

        # ComboBox para selecionar a moeda de destino
        self.moeda_destino_menu = ttk.Combobox(root, textvariable=self.moeda_destino, values=self.moedas)
        self.moeda_destino_menu.pack()

        # Botão para solicitar a cotação da moeda selecionada
        self.btn_obter_cotacao = tk.Button(root, text="Obter Cotação", command=self.exibir_cotacao)
        self.btn_obter_cotacao.pack()

    def exibir_cotacao(self):
        moeda_base = self.moeda_base.get()
        moeda_destino = self.moeda_destino.get()
        
        # Aqui você pode fazer a requisição para obter a cotação da moeda selecionada
        # Vou simular uma requisição usando uma API de exemplo (https://api.exchangerate-api.com)
        try:
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{moeda_base}")
            data = response.json()
            cotacao = data['rates']
            if moeda_destino in cotacao:
                # Criação da nova janela (Top Level) para exibir a cotação
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title("Cotação")
                
                texto_cotacao = f"1 {moeda_base} = {cotacao[moeda_destino]} {moeda_destino}"
                label_cotacao = tk.Label(nova_janela, text=texto_cotacao)
                label_cotacao.pack()

                # Aqui você pode adicionar lógica para exibir o histórico da moeda ao longo do tempo

            else:
                tk.messagebox.showerror("Erro", "Moeda de destino inválida")
        except requests.RequestException as e:
            tk.messagebox.showerror("Erro", f"Erro ao obter cotação: {e}")
