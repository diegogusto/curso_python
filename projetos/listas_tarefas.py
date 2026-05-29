import os

tasks = []

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. editar tarefa")
    print("4. sair")

    choice = input("Escolha uma opção: ")
    if choice == "1":
        print("Digite a nova tarefa:")
        task = input("> ")
        tasks.append(task)
        print("Tarefa adicionada!")
        input("Pressione Enter para continuar...")

    elif choice == "2":
        print('=== Tarefas ===')
        value = 1
        for task in tasks:
            print(f'{value} - {task}')
            value += 1
        remove_task = input("Deseja remover alguma tarefa? (s/n) ")
        if remove_task.lower() == "s":
            task_number = int(input("Digite o número da tarefa a ser removida: "))
            if task_number > 0 and task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f'Tarefa "{removed_task}" removida!')
            else:
                print("Número de tarefa inválido.")

        input("Pressione Enter para continuar...")

    elif choice == "3":

        if len(tasks) == 0:
            print("Nenhuma tarefa para editar.")
            input("Pressione Enter para continuar...")
        
        else:
            print('=== Tarefas ===')
            value = 1
            for task in tasks:
                print(f'{value} - {task}')
                value += 1
            
            edit_task = input("Deseja editar alguma tarefa? (s/n) ")
            if edit_task.lower() == 's':
                task_number = int(input("digite o numero da tarefa a ser editada: "))
                if task_number > 0 and task_number <= len(tasks):
                    new_task = input("digite a nova tarefa: ")
                    tasks[task_number - 1] = new_task
                    print("tarefa editada com sucesso!")
                else:
                    print("Número de tarefa inválido.")
            input("Pressione Enter para continuar...")
    
    elif choice == "4":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")

    
    


    

    
        
    
