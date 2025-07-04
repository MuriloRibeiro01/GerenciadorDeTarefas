# Gerenciador de tarefas.

import os

# A lista agora vai armazenar DICIONÁRIOS, não mais strings simples
tarefas = []

continuarExecutando = True

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
    print("4. Concluir Tarefa.") # Nova opção!
    print("5. Sair.")
    print("==================\n")

    # Garante que a escolha do usuário seja um número inteiro para comparações futuras
    try:
        escolhaUsuario = int(input("Escolha uma opção: \n"))
    except ValueError:
        print("Entrada inválida! Por favor, digite um NÚMERO da opção.")
        input("Pressione <enter> para continuar...")
        continue # Volta para o início do loop sem processar o resto

    # Opção 1: Adicionar Tarefa
    if escolhaUsuario == 1: # Comparando com int
        descricaoTarefa = input("Qual a sua tarefa: \n")
        prioridadeTarefa = input("Qual a prioridade da sua tarefa (Ex: Alta, Média, Baixa): \n")

        # Cria um dicionário para a nova tarefa
        nova_tarefa = {
            "descricao": descricaoTarefa, # A descrição da tarefa
            "concluida": False,         # Status inicial: não concluída
            "prioridade": prioridadeTarefa
        }
        tarefas.append(nova_tarefa) # Adiciona o dicionário à lista
        print("Tarefa adicionada com sucesso!")
        input("\nPressione <enter> para continuar...")

    # Opção 2: Listar Tarefas
    elif escolhaUsuario == 2: # Comparando com int
        if not tarefas:
            print("Lista de tarefas vazia.\n")
            input("Pressione <enter> para continuar...")
        else:
            print("--- Lista de Tarefas ---")
            for i, tarefa_dic in enumerate(tarefas): # 'tarefa_dic' agora é o dicionário de cada tarefa
                # Define o símbolo de status baseado na chave 'concluida' do dicionário
                simboloStatus = "[X]" if tarefa_dic["concluida"] else "[ ]"

                # Imprime a tarefa usando as chaves do dicionário 'tarefa_dic'
                print(f"{i + 1}. {simboloStatus} {tarefa_dic['descricao']} (Prioridade: {tarefa_dic['prioridade']})")
            print("------------------------")
            input("Pressione <enter> para continuar...")

    # Opção 3: Remover Tarefas
    elif escolhaUsuario == 3: # Comparando com int
        if not tarefas:
            print("Nenhuma tarefa para remover.\n")
            input("Pressione <enter> para continuar...")
        else:
            print("--- Tarefas para Remover ---")
            # Lista as tarefas para o usuário escolher, usando o novo formato de exibição
            for i, tarefa_dic in enumerate(tarefas):
                simboloStatus = "[X]" if tarefa_dic["concluida"] else "[ ]"
                print(f"{i + 1}. {simboloStatus} {tarefa_dic['descricao']} (Prioridade: {tarefa_dic['prioridade']})")
            print("---------------------------")

            try:
                escolhaRemocao_numero = int(input("Digite o NÚMERO da tarefa a ser deletada: \n"))
                indiceDoPython = escolhaRemocao_numero - 1

                if 0 <= indiceDoPython < len(tarefas):
                    # Remove o dicionário da tarefa e guarda a tarefa removida para a mensagem
                    tarefa_removida_dic = tarefas.pop(indiceDoPython)
                    print(f"Tarefa '{tarefa_removida_dic['descricao']}' deletada com sucesso!")
                else:
                    print("Número inválido. Não existe tarefa com esse número.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

            input("\nPressione <enter> para continuar...")

    # Opção 4: Concluir Tarefa
    elif escolhaUsuario == 4: # Comparando com int
        if not tarefas:
            print("Nenhuma tarefa para concluir.\n")
            input("Pressione <enter> para continuar...")
        else:
            print("--- Tarefas para Concluir ---")
            # Lista as tarefas para o usuário escolher (com o status atual)
            for i, tarefa_dic in enumerate(tarefas):
                simboloStatus = "[X]" if tarefa_dic["concluida"] else "[ ]"
                print(f"{i + 1}. {simboloStatus} {tarefa_dic['descricao']} (Prioridade: {tarefa_dic['prioridade']})")
            print("----------------------------")

            try:
                escolhaConclusao_numero = int(input("Digite o NÚMERO da tarefa a ser concluída: \n"))
                indiceDoPython = escolhaConclusao_numero - 1

                if 0 <= indiceDoPython < len(tarefas):
                    # Acessa o dicionário da tarefa e altera o valor da chave 'concluida'
                    tarefa_a_concluir = tarefas[indiceDoPython]
                    if tarefa_a_concluir["concluida"]:
                        print(f"A tarefa '{tarefa_a_concluir['descricao']}' já estava concluída!")
                    else:
                        tarefa_a_concluir["concluida"] = True # Marca como True!
                        print(f"Tarefa '{tarefa_a_concluir['descricao']}' marcada como concluída com sucesso!")
                else:
                    print("Número inválido. Não existe tarefa com esse número.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

            input("\nPressione <enter> para continuar...")

    # Opção 5: Sair do Programa
    elif escolhaUsuario == 5: # Comparando com int
        print("Programa finalizado com sucesso! Até a próxima!")
        continuarExecutando = False # Altera a condição para sair do loop

    # Caso a opção digitada não seja válida (agora pega qualquer int fora do range)
    else:
        print("Opção inválida. Por favor, escolha entre 1, 2, 3, 4 ou 5.\n")
        input("Pressione <enter> para continuar...")

print("Obrigado por usar o Gerenciador de Tarefas!")
