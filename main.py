# Gerenciador de tarefas.

import os

tarefas = [] # Lista para armazenar as tarefas

continuarExecutando = True # Variável para controlar o loop principal

# Função para limpar o console, adaptada para Windows (nt)
def clear_console():
    if os.name == 'nt':
        _ = os.system('cls') # No Windows, usa 'cls'

# Loop principal do programa
while continuarExecutando:
    clear_console() # Limpa o console antes de exibir o menu

    # Exibe o menu de opções para o usuário
    print("==================")
    print("1. Adicionar Tarefa.")
    print("2. Listar Tarefas.")
    print("3. Remover Tarefas.")
    print("4. Sair.") 
    print("==================\n")

    escolhaUsuario = input("Escolha uma opção: \n")

    # Opção 1: Adicionar Tarefa
    if escolhaUsuario == "1":
        print("Digite sua tarefa: ")
        tarefasUsiario = input() # Pega a descrição da tarefa
        tarefas.append(tarefasUsiario) # Adiciona a string diretamente na lista
        print("Tarefa adicionada com sucesso!")
        input("\nPressione <enter> para continuar...") # Pausa para o usuário ler a mensagem

    # Opção 2: Listar Tarefas
    elif escolhaUsuario == "2":
        if not tarefas: # Verifica se a lista de tarefas está vazia
            print("Lista de tarefas vazia.\n")
            input("Pressione <enter> para continuar...")
        else:
            print("Lista de Tarefas:")
            # Percorre a lista e exibe cada tarefa com sua numeração
            for i, listagem in enumerate(tarefas):
                # Neste ponto, 'listagem' é a string da tarefa
                print(f"{i + 1}. {listagem}") # Exibe a tarefa numerada
            input("\nPressione <enter> para continuar...")

    # Opção 3: Remover Tarefas
    elif escolhaUsuario == "3":
        if not tarefas: # Verifica se a lista está vazia antes de tentar remover
            print("Nenhuma tarefa para remover.\n")
            input("Pressione <enter> para continuar...")
        else:
            print("Escolha a tarefa a ser deletada:")
            # Lista as tarefas numeradas para o usuário escolher
            for i, listagem in enumerate(tarefas):
                # Neste ponto, 'listagem' é a string da tarefa
                print(f"{i + 1}. {listagem}")

            try: # Tenta converter a entrada para inteiro, para evitar erro se digitar texto
                escolhaRemocao_numero = int(input())
                indiceDoPython = escolhaRemocao_numero - 1 # Ajusta o número do usuário para o índice Python (base 0)

                # Valida se o índice está dentro dos limites da lista
                if 0 <= indiceDoPython < len(tarefas):
                    tarefa_removida = tarefas.pop(indiceDoPython) # Remove a tarefa e guarda ela
                    print(f"Tarefa '{tarefa_removida}' deletada com sucesso!")
                else:
                    print("Número inválido. Não existe tarefa com esse número.")
            except ValueError: # Se o usuário digitar algo que não seja número
                print("Entrada inválida. Por favor, digite um número.")

            input("\nPressione <enter> para continuar...")

    # Opção 4: Sair do Programa
    elif escolhaUsuario == "4":
        print("Programa finalizado com sucesso!")
        continuarExecutando = False # Altera a condição para sair do loop

    # Caso a opção digitada não seja válida
    else:
        print("Opção inválida. Escolha entre 1, 2, 3 ou 4.\n")
        input("Pressione <enter> para continuar...")

print("Obrigado por usar o Gerenciador de Tarefas!")
