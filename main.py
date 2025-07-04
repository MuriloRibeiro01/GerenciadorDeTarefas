# Gerenciador de tarefas.



tarefas = []



continuarExecutando = True



while continuarExecutando:



    print("==================\n")

    print("1. Adicionar Tarefa")

    print("2. Listar Tarefas")

    print("3. Sair.")

    print("==================\n")



    escolhaUsuario = input("Escolha uma opção: \n")



    if escolhaUsuario == "1":

        print("Digite sua tarefa: ")

        tarefasUsiario = input()

        tarefas.append(tarefasUsiario)



    if escolhaUsuario == "2":

        print("Lista de Tarefas: \n")

        print(tarefas)



    if escolhaUsuario == "3":

        print("Programa finalizado com sucesso!")
        break