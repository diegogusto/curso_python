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
            
        