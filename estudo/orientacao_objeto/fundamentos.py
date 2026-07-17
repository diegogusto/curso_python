class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.estoque = stock

    def diminuir_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print('Estoque insuficiente')
            return False
        

class Cart_item:
    def __init__(self):
        self.itens = []
        self.total = 0.0

    def adicionar(self, product, quantidade):
        if product.diminuir_estoque(quantidade):
            self.itens.append({"nome": product.name, "quantidade": quantidade})
            self.total += (product.price * quantidade)
            print(f"{quantidade}x '{product.name}' adicionado ao carrinho")
            
    def exibir_resumo(self):
        print("\n resumo da compra")
        for item in self.itens:
            print(f"-{item['quantidade']}x {item['nome']}")
            print(f"total a pagar: R$ {self.total:.2f}")
            
notebook = Product("Notebook DEll", 4500.00, 10)
mouse = Product("Mouse Gamer", 150.00, 20)

carrinho_cliente = Cart_item()

carrinho_cliente.adicionar(notebook, 2)
carrinho_cliente.adicionar(mouse, 1)
carrinho_cliente.adicionar(mouse, 25)  # Tentativa de adicionar mais do que o estoque disponível
print(f"Estoque restante do notebook: {notebook.estoque}")