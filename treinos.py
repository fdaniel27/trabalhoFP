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

def exibir_menu():
    print("\nMenu de Treinos e Competições")
    print("1. Adicionar registro")
    print("2. Visualizar registros")
    print("3. Atualizar registro")
    print("4. Excluir registro")
    print("5. Sair")
    return input("Escolha uma opção: ")

def adicionar_registro(registros):
    print("\nAdicionar Novo Registro:")
    data = input("Data (dd/mm/aaaa): ")
    tipo = input("Tipo (treino ou competição): ").capitalize()
    distancia = input("Distância (km): ")
    tempo = input("Tempo (minutos): ")
    localizacao = input("Localização: ")
    condicoes = input("Condições (ex.: ensolarado, nublado): ")
    
    novo_registro = [data, tipo, distancia, tempo, localizacao, condicoes]
    registros.append(novo_registro)
    salvar_dados(registros)
    print("\nRegistro adicionado com sucesso!")