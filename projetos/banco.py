import os
balance = []
extrato = []
while True:
    os.system("cls" if os.name == "nt" else "clear")
    
    print("=== Banco do Diego ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver saldo")
    print("4. Ver extrato")
    print("5. Sair")

    choice = input("Escolha uma opção: ")
    if choice  == "1":
        deposit = float(input("Digite o valor a ser depositado: "))
        if deposit <= 0:
            print("Valor inválido! O depósito deve ser maior que zero.")
            input("Pressione Enter para continuar...")

        else:
            balance.append(deposit)
            extrato.append(f"Depósito: +R${deposit:.2f}")
            print(f"Você depositou R${deposit:.2f}")
            input("Pressione Enter para continuar...")
    

    elif choice == "2":
        withdraw = float(input("digite o valor a ser sacado: "))
        if withdraw <= 0:
            print("Valor inválido! O saque deve ser maior que zero.")
            input("Pressione Enter para continuar...")

        elif withdraw > sum(balance):
            print("Saldo insuficiente!")
            input("Pressione Enter para continuar...")

        else:
            balance.append(-withdraw)
            extrato.append(f"Saque: -R${withdraw:.2f}")
            print(f"Você sacou R${withdraw:.2f}")
            input("Pressione Enter para continuar...")
    

    elif choice == "3":
        print(f"Seu saldo é R${sum(balance):.2f}")
        input("Pressione Enter para continuar...")

    elif choice == "4":
        print("=== Extrato ===")
        
        if not extrato:
            print("Não foram realizadas movimentações.")

        else:
            for transaction in extrato:
                print(transaction)
            print(f"Saldo atual: R${sum(balance):.2f}")
            input("Pressione Enter para continuar...")

    elif choice == "5":
        print("Encerrando o programa...")
        break
    
        

    
