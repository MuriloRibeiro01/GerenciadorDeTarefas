# Gerenciador de tarefas.

import os

import json

# A lista agora vai armazenar DICIONÁRIOS, não mais strings simples
tarefas = []
nome_arquivo_tarefas = "minhas_tarefas.json" # Nome para o arquivo de dados

continuarExecutando = True

# Função para limpar o console, adaptada para Windows (nt)
def clear_console():
    if os.name == 'nt':
        _ = os.system('cls') # No Windows, usa 'cls'


# Função para listar as tarefas, já que o uso de copy + paste estava muito alto
def exibir_listagem(tarefas):

    if not tarefas:
        print("Nenhuma tarefa para listar.\n")
        input("Pressione <enter> para continuar...")
        return

    for i, tarefa_dic in enumerate(tarefas): # for retirado do looping while para reduzir a repetitividade de códgio
        simboloStatus = "[X]" if tarefa_dic["concluida"] else "[ ]"
        print(f"{i + 1}. {simboloStatus} {tarefa_dic['descricao']} (Prioridade: {tarefa_dic['prioridade']})")
    print("---------------------------")


# --- BLOCO DE CARREGAMENTO ---
try:
    with open(nome_arquivo_tarefas, 'r', encoding='utf-8') as json_file:
        tarefas_carregadas = json.load(json_file)
        tarefas = tarefas_carregadas # Atribui o que foi carregado à lista principal.
        print("Tarefas carregadas com sucesso!\n")
except FileNotFoundError:
    print("Arquivo não encontrado. Iniciando com lista vazia.")
    tarefas = []
except json.decoder.JSONDecodeError:
    print("Erro ao ler arquivo (pode estar corrompido). Iniciando com lista vazia.\n")
    tarefas = [] # Garante que a lista esteja vazia se o JSON estiver inválido.
except PermissionError:
    print("Erro de permissão KKKKKKKKKKKKKKKK")
except IOError:
    print("Disco rígido cheio.")
except Exception as e:
    print(f"Erro desconhecido ao salvar: {e}.")

# --- FIM DO BLOCO DE CARREGAMENTO ---

# Esse bloco só vai rodar uma vez, já que está no início do código, fora do while.


# Loop principal do programa
while continuarExecutando:

    clear_console() # Limpa o console antes de exibir o menu

    # Exibe o menu de opções para o usuário
    print("==================")
    print("1. Adicionar Tarefa.")
    print("2. Listar Tarefas.")
    print("3. Remover Tarefas.")
    print("4. Concluir Tarefa.") # Nova opção!
    print("5. Filtrar Tarefas.")
    print("6. Sair.")
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
        print("--- Lista de Tarefas ---\n")
        exibir_listagem(tarefas)
        input("\nPressione <enter> para continuar...")

    # Opção 3: Remover Tarefas
    elif escolhaUsuario == 3: # Comparando com int
        if not tarefas:
            print("Nenhuma tarefa para remover.\n")
            input("Pressione <enter> para continuar...")
        else:
            # Chamada da função de exibição
            print("--- Tarefas para Remover ---")
            exibir_listagem(tarefas)

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
            # Chamada da função de exibição
            print("--- Tarefas para Concluir ---")
            exibir_listagem(tarefas)

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

    # Opção 5: Visualizar Tarefas (Filtrar)
    elif escolhaUsuario == 5: # Comparando com int
        if not tarefas:
            print("Nenhuma tarefa para filtrar.\n")
            input("Pressione <enter> para continuar...")
        else:
            print("--- Lista de Filtragens ---")
            continuarFiltragem = True
            while continuarFiltragem:
                print("1 - Todas as tarefas\n")
                print("2 - Tarefas Pendentes\n")
                print("3 - Tarefas Concluídas\n")
                print("4 - Voltar ao Menu Principal\n")

                opcaoUsuario = int(input("Escolha uma opção: "))

                if opcaoUsuario == 1: # Comparando com int
                    # Chamada da função de exibição
                    print("--- Lista de Tarefas ---\n")
                    exibir_listagem(tarefas)

                # Utilizado compreensão de lista para fazer a filtragem
                elif opcaoUsuario == 2: # Comparando com int
                    dicionarioPendentes = [
                        tarefa_dic
                        for tarefa_dic in tarefas
                        if not tarefa_dic["concluida"]
                    ]

                    print("--- Tarefas Pendentes ---\n")
                    # Chamada da função de exibição para o dicionário criado
                    exibir_listagem(dicionarioPendentes)
                    input("Pressione <enter> para continuar...")

                # Utilizado compreensão de lista para fazer a filtragem
                elif opcaoUsuario == 3: # Comparando com int
                    dicionarioConclusao = [
                        tarefa_dic
                        for tarefa_dic in tarefas
                        if tarefa_dic["concluida"]
                    ]

                    print("--- Tarefas Conclúidas ---\n")
                    # Chamada da função de exibição para o dicionário criado
                    exibir_listagem(dicionarioConclusao)
                    input("Pressione <enter> para continuar...")

                elif opcaoUsuario == 4: # Comparando com int
                    print("Voltando ao Menu Principal...")
                    continuarFiltragem = False


    # Opção 6: Sair do Programa
    elif escolhaUsuario == 6: # Comparando com int
        with open(nome_arquivo_tarefas, 'w', encoding='utf-8') as json_file:
            json.dump(tarefas, json_file, indent=4, ensure_ascii=False) # Vai salvar a lista 'tarefas'.
        print("Tarefa salva com sucesso!\n")
        print("Programa finalizado com sucesso! Até a próxima!")
        continuarExecutando = False # Altera a condição para sair do loop

    # Caso a opção digitada não seja válida (agora pega qualquer int fora do range)
    else:
        print("Opção inválida. Por favor, escolha entre 1, 2, 3, 4 ou 5.\n")
        input("Pressione <enter> para continuar...")

print("Obrigado por usar o Gerenciador de Tarefas!")