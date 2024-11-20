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

def validar_data(data):
    partes = data.split('/')
    if len(partes) != 3:
        return False
    dia, mes, ano = partes
    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
        return False
    dia, mes, ano = int(dia), int(mes), int(ano)
    if not (1 <= mes <= 12 and 1 <= dia <= 31 and ano > 0):
        return False
    if mes in {4, 6, 9, 11} and dia > 30:
        return False
    if mes == 2:
        bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
        if dia > (29 if bissexto else 28):
            return False
    return True

def adicionar_registro(registros):
    print("\nAdicionar Novo Registro:")
    while True:
        data = input("Data (dd/mm/aaaa): ")
        if validar_data(data):
            break
        print("Data inválida. Tente novamente.")
    
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
        for i, registro in enumerate(registros):
            print(f"\nRegistro {i + 1}: {', '.join(registro)}")

def atualizar_registro(registros):
    visualizar_registros(registros)
    try:
        indice = int(input("\nDigite o número do registro que deseja atualizar: ")) - 1
        if 0 <= indice < len(registros):
            campos = ['Data', 'Tipo', 'Distância', 'Tempo', 'Localização', 'Condições']
            for i in range(len(campos)):
                valor_atual = registros[indice][i]
                if campos[i] == "Data":
                    while True:
                        novo_valor = input(f"{campos[i]} (atual: {valor_atual}): ") or valor_atual
                        if validar_data(novo_valor):
                            registros[indice][i] = novo_valor
                            break
                        print("Data inválida. Tente novamente.")
                else:
                    registros[indice][i] = input(f"{campos[i]} (atual: {valor_atual}): ") or valor_atual
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
