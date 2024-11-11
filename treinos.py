from datetime import datetime

def salvar_dados(registros):
    with open('treinos_competicoes.txt', mode='w') as arquivo:
        for registro in registros:
            arquivo.write(','.join(registro) + '\n')

def carregar_dados():
    try:
        with open('treinos_competicoes.txt', mode='r') as arquivo:
            return [linha.strip().split(',') for linha in arquivo.readlines()]
    except FileNotFoundError:
        return []