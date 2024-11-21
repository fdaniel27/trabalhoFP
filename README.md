Descrição
Este é um projeto de python passado pela professora Carol que permite gerenciar treinos e competições de corrida.
Ele fornece funcionalidades para registrar informações sobre treinos e competições, acompanhar metas, filtrar registros e obter sugestões de treinos baseados no histórico.


Principais funções:

Adicionar Registro: Permite incluir novos registros com informações como data, tipo, distância, tempo, localização e condições climáticas.
Visualizar Registros: Lista todos os registros armazenados.
Atualizar Registro: Atualiza os dados de um registro existente.
Excluir Registro: Remove um registro específico.
Filtrar Registros por Distância ou Tempo: Filtra os registros com base na distância percorrida ou no tempo gasto.
Definir e Acompanhar Metas: Permite definir metas de distância total e acompanhar o progresso.
Sugestões de Treinos: Sugere treinos com base no último registro adicionado.
Armazenamento Persistente: Todos os dados são armazenados em um arquivo de texto (treinos_competicoes.txt), garantindo a persistência das informações.


Funções dentro do código:

salvar_dados: Salva os registros no arquivo treinos_competicoes.txt.
carregar_dados: Carrega os registros do arquivo.
exibir_menu: Exibe o menu de opções interativas.
validar_data: Valida o formato de data inserido pelo usuário.
adicionar_registro: Adiciona um novo registro ao sistema.
visualizar_registros: Exibe todos os registros.
atualizar_registro: Permite a edição de registros existentes.
excluir_registro: Remove registros do sistema.
filtrar_registros: Filtra registros com base em critérios de distância ou tempo.
definir_meta: Define uma meta de distância a ser alcançada.
acompanhar_meta: Mostra o progresso em relação à meta definida.
sugestao_treino: Gera uma sugestão de treino baseado no último registro.
main: Função principal que gerencia o fluxo do programa
