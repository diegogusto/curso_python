cart = []
def add_product():
    product = input("digite o nome do produto: ")
    value_product = float(input("digite o valor do produto: "))
    if value_product < 0:
        print("Valor do produto não pode ser negativo. Por favor, tente novamente.")
        return
    else:
        cart.append({"product": product, "value": value_product})


def view_cart():
    if len(cart) == 0:
        print("O carrinho está vazio.")
    else:
        print("=== Carrinho ===")
        value = 1
        for item in cart:
            print(f'{value}. {item["product"]} - R${item["value"]:.2f}')
            value += 1

    remove_item = input("Deseja remover algum item? (s/n) ")
    if remove_item.lower() == "s":
        item_number = int(input("Digite o número do item a ser removido:"))
        if item_number > 0 and item_number <= len(cart):
            removed_item = cart.pop(item_number - 1)
            print(f'Item "{removed_item["product"]}" removido!')
            input("Pressione qualquer botão para voltar ao menu...")
        else:
            input("Número de item inválido. Pressione qualquer botão para voltar ao menu...")
            


def finalize_purchase():
    if len(cart) == 0:
        print("O carrinho está vazio. Adicione produtos antes de finalizar a compra.")
    else:
        total = sum(item["value"] for item in cart)
        print(f"Total da compra: R${total:.2f}")
        change = input("ira precisar precisar de troco? (s/n)")

        if change.lower() == "s":
            amount_paid = float(input("Digite o valor pago:"))
            if amount_paid >= total:
                troco = amount_paid - total
                print(f"Troco: R${troco:.2f}")
                print("Compra finalizada! Obrigado por comprar conosco.")
                cart.clear()
            else:
                print("Valor pago insuficiente. Por favor, tente novamente.")
        else:
            print("Compra finalizada! Obrigado por comprar conosco.")
            cart.clear()

while True:
    print("Bem-vindo ao mercado!")
    print("1. Adicionar item ao carrinho")
    print("2. Ver carrinho")
    print("3. finalizar compra")
    print("4. sair")

    choice = input("Escolha uma opção: ")

    if choice == "1":
        add_product()
        input("Produto adicionado! Pressione qualquer botão para voltar ao menu...")
    
    elif choice == "2":
        view_cart()
        input("Pressione qualquer botão para voltar ao menu...")

    elif choice == "3":
        finalize_purchase()
        input("Pressione qualquer botão para voltar ao menu...")
    
    elif choice == "4":
        print("Obrigado por visitar o mercado! Até a próxima.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        input("Pressione qualquer botão para voltar ao menu...")
