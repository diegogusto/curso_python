enrolled_students = []



def enroll(name, course):
        student = {
            "name": name,
            "course": course,
            "payment_status": False
        }
        enrolled_students.append(student)
        print(f"Aluno {name} matriculado com sucesso no curso {course}.")

def list_students():
    if not enrolled_students:
        print("Nenhum aluno matriculado.")
    else:
        print("\n--- Alunos Matriculados ---")
        for student in enrolled_students:
            print(f"Nome: {student['name']}, Curso: {student['course']}, Status de Pagamento: {'Pago' if student['payment_status'] else 'Pendente'}")




while True:
     print("\n--- SISTEMA DE MATRICULAS ---")
     print("1. matricular novo aluno")
     print("2. listar alunos matriculados")
     print("3. pagamentos")
     print("4. sair")

     option = input("Escolha uma opção: ")

     if option == "1":
          print("\n--- Matricular Novo Aluno ---")
          name = input("Digite o nome do aluno: ")
          course = input("Digite o curso desejado: ")
          enroll(name, course)
    
     if option == "2":
        list_students()
        input("\nPressione Enter para voltar ao menu principal...")

     if option == "3":
        print("\n--- Pagamentos ---")
        print("nome do aluno que deseja fazer o pagamento: ")
        student_payment= input()

        student_found = False

        for student in enrolled_students:
            if student["name"].lower() == student_payment.lower():
                student["payment_status"] = True
                print(f"Pagamento realizado com sucesso para o aluno {student['name']}.")
                student_found = True
                break

        if student_found == False:
            print(f"Aluno {student_payment} não encontrado.")

        input("\nPressione Enter para voltar ao menu principal...") 


        if option == "4":
            print("\nSaindo do sistema. Até logo!")
            break

    

        