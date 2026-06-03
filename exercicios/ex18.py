import json
import os



def add_task(task):
    tasks.append(task)
    tasks_history.append(task)

def view_tasks():
    if len(tasks) == 0:
        print("Nenhuma tarefa na lista.")
    else:
        print("=== Tarefas ===")
        for task in tasks:
            print(f"- {task}")

def remove_task():
    if len(tasks) == 0:
        print("Nenhuma tarefa para remover.")
    else:
        removed_task = tasks.pop()
        print(f'Tarefa "{removed_task}" removida!')

def redo_task():
    if len(tasks_history) == 0:
        print("Nenhuma tarefa para refazer.")
    else:
        last_task = tasks_history[-1]
        if last_task in tasks:
            print(f'Tarefa "{last_task}" já está na lista.')
        else:
            tasks.append(last_task)
            print(f'Tarefa "{last_task}" refeita!')

def to_read_file(tasks, path_archive):
    data = []
    try:
        with open(path_archive, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {path_archive} não encontrado. Criando um novo arquivo.")
        save_tasks(tasks, path_archive)
    return data

def save_tasks(tasks, path_archive):
    data = tasks
    with open(path_archive, 'w', encoding='utf-8') as file:
        data = json.dump(tasks, file, indent=2, ensure_ascii=False)
    return data

PATH_ARCHIVE = 'exercicios/ex18_tasks.json'         
tasks_history = []
tasks = to_read_file([], PATH_ARCHIVE)




while True:
    print ("=== Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("4. refazer tarefa")
    print()

    choice = input("Escolha uma opção: ")

    if choice == "1":
        task = input("Digite a tarefa: ")
        add_task(task)
        print()

    elif choice == "2":
        view_tasks()
        print()

    elif choice == "3":
        remove_task()
        print()

    elif choice == "4":
        redo_task()
        print()

    
    save_tasks(tasks, PATH_ARCHIVE)