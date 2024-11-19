os.system("clear")
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

def visualizar_registros(registros):
    if not registros:
        print("\nNenhum registro encontrado.")
    else:
        print("\nRegistros de Treinos e Competições:")
        for i in range(len(registros)):
            print(f"\nRegistro {i + 1}: {', '.join(registros[i])}")

def atualizar_registro(registros):
    visualizar_registros(registros)
    try:
        indice = int(input("\nDigite o número do registro que deseja atualizar: ")) - 1
        if 0 <= indice < len(registros):
            campos = ['Data', 'Tipo', 'Distância', 'Tempo', 'Localização', 'Condições']
            for i in range(len(campos)):
                novo_valor = input(f"{campos[i]} (atual: {registros[indice][i]}): ") or registros[indice][i]
                registros[indice][i] = novo_valor
            salvar_dados(registros)
            print("\nRegistro atualizado com sucesso!")
        else:
            print("\nRegistro não encontrado.")
    except (ValueError, IndexError):
        print("\nEntrada inválida.")

def excluir_registro(registros):
    visualizar_registros(registros)
    try:
        indice = int(input("\nDigite o número do registro que deseja excluir: ")) - 1
        if 0 <= indice < len(registros):
            registros.pop(indice)
            salvar_dados(registros)
            print("\nRegistro excluído com sucesso!")
        else:
            print("\nRegistro não encontrado.")
    except (ValueError, IndexError):
        print("\nEntrada inválida.")

def main():
    registros = carregar_dados()
    
    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            adicionar_registro(registros)
        elif opcao == '2':
            visualizar_registros(registros)
        elif opcao == '3':
            atualizar_registro(registros)
        elif opcao == '4':
            excluir_registro(registros)
        elif opcao == '5':
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()


#Funcionalidade Extra Jogo das Palavar
def jogo_palavras():

    perguntas = [
        ("cachorro", "Um animal doméstico que late."),
        ("c++", "Uma linguagem de programação que já vimos."),
        ("praia", "Um lugar com areia e mar."),
        ("livro", "Algo que você lê."),
        ("onibus", "Um meio de transporte muito usado."),
    ]
    print("Bem-vindo ao jogo das palavras!")
    print("Escolha um número entre 0 e 4 para ver qual e sua frase do jogo.")
    
    while True:
        try:
            indice = int(input("Digite o numero: "))
            if 0 <= indice < len(perguntas):
                palavra, dica = perguntas[indice]
                break
            else:
                print("Escolha um numero entre 0 e 4.")
        except ValueError:
            print("Numero invalido! Digite um numero valido.")
    

    print(f"Dica: {dica}")
    tentativas = 5
    while tentativas > 0:
        tentativa = input(f"Você tem {tentativas} tentativas. Qual é a palavra? ").lower()
        if tentativa == palavra:
            print("Parabéns! Você acertou!")
            return
        else:
            print("Errado! Tente novamente.")
            tentativas -= 1


    print(f"Que pena! A palavra era '{palavra}'. Tente novamente.")


if __name__ == "Nome":
    while True:
        jogo_palavras()
        jogar = input("Quer jogar novamente? (0 para sim e 1 para não): ")
        
        if jogar != "0":
            print("Obrigado por jogar! Até a próxima.")
            break
