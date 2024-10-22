import csv
import random
from datetime import datetime

def salvar_dados(registros):
    with open('treinos_competicoes.csv', mode='w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Data', 'Tipo', 'Distância', 'Tempo', 'Localização', 'Condições'])
        for registro in registros:
            escritor.writerow(registro)

def carregar_dados():
    try:
        with open('treinos_competicoes.csv', mode='r') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            return [linha for linha in leitor]
    except FileNotFoundError:
        return []