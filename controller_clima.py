import tkinter as tk
from tkinter import ttk
import requests

class ClimaController:
    def __init__(self, root):
        self.root = root


        self.paises = {'Brasil': {'São Paulo': ['São Paulo', 'Campinas'], 'Rio de Janeiro': ['Rio de Janeiro', 'Niterói']},
                       'EUA': {'New York': ['New York', 'Buffalo'], 'California': ['Los Angeles', 'San Francisco']}}

        self.pais_label = tk.Label(root, text="Selecione o país:")
        self.pais_label.pack()

        self.pais_var = tk.StringVar()
        self.pais_combobox = ttk.Combobox(root, textvariable=self.pais_var, values=list(self.paises.keys()))
        self.pais_combobox.pack()

        self.estado_label = tk.Label(root, text="Selecione o estado:")
        self.estado_label.pack()

        self.estado_var = tk.StringVar()
        self.estado_combobox = ttk.Combobox(root, textvariable=self.estado_var, state="readonly")
        self.estado_combobox.pack()

        self.cidade_label = tk.Label(root, text="Selecione a cidade:")
        self.cidade_label.pack()

        self.cidade_var = tk.StringVar()
        self.cidade_combobox = ttk.Combobox(root, textvariable=self.cidade_var, state="readonly")
        self.cidade_combobox.pack()

        self.search_button = tk.Button(root, text="Buscar Clima", command=self.get_weather)
        self.search_button.pack()

        # Vincula a função de preencher estados ao evento de seleção de país
        self.pais_combobox.bind("<<ComboboxSelected>>", self.populate_estados)
        self.estado_combobox.bind("<<ComboboxSelected>>", self.populate_cidades)

    def populate_estados(self, event):
        pais_selecionado = self.pais_var.get()
        estados = list(self.paises[pais_selecionado].keys())
        self.estado_combobox['values'] = estados

    def populate_cidades(self, event):
        pais_selecionado = self.pais_var.get()
        estado_selecionado = self.estado_var.get()
        cidades = self.paises[pais_selecionado][estado_selecionado]
        self.cidade_combobox['values'] = cidades

    def show_message(self, message):
        top = tk.Toplevel()
        top.title("Resultado da Busca")
        label = tk.Label(top, text=message)
        label.pack(padx=20, pady=10)
        button = tk.Button(top, text="Fechar", command=top.destroy)
        button.pack(pady=5)

    def get_weather(self):
        pais_selecionado = self.pais_var.get()
        estado_selecionado = self.estado_var.get()
        cidade_selecionada = self.cidade_var.get()

        api_key = "2fca4808e935991dfc7bb18f168a72a4"
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade_selecionada}&appid={api_key}&units=metric&lang=pt_br"

        try:
            response = requests.get(base_url)
            weather_data = response.json()

            if weather_data['cod'] == 200:
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                city = weather_data['name']
                country = weather_data['sys']['country']

                weather_info = f"City: {city}, {country}\nTemperature: {temperature}°C\nDescription: {description}"

                self.show_message(weather_info)
            else:
                self.show_message("Location not found")
        except requests.RequestException as e:
            self.show_message(f"Error fetching weather: {e}")

    def show_message(self, message):
        top = tk.Toplevel()
        top.title("Weather Forecast")
        label = tk.Label(top, text=message)
        label.pack(padx=20, pady=10)
        button = tk.Button(top, text="Close", command=top.destroy)
        button.pack(pady=5)


