# ==========================================
# 1. A Classe PAI (Tem o que é comum a todos)
# ==========================================
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def bater_ponto(self):
        print(f"⏰ {self.nome} bateu o ponto!")

# ==========================================
# 2. A Classe FILHA (Herda de Funcionario)
# ==========================================
# Colocamos o nome da classe pai entre parênteses
class Gerente(Funcionario):
    def __init__(self, nome, salario, senha_cofre):
        # O 'super()' serve para acionar o __init__ da classe Pai. 
        # É como dizer: "Pai, arruma o nome e o salário aí que eu cuido da senha daqui."
        super().__init__(nome, salario)
        
        # Atributo exclusivo do Gerente
        self.senha_cofre = senha_cofre

    # Método exclusivo do Gerente
    def abrir_cofre(self):
        print(f"💰 {self.nome} abriu o cofre com a senha {self.senha_cofre}.")
    

class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao

    def vender(self):
        print("item vendido")
        


#========================================================================

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def buzinar(self):
        print(f'O {self.marca} {self.modelo} buzinou: Biiip Biiip')


class Carro(Veiculo):
    def __init__(self, marca, modelo, quantidade_portas):
        self.quantidade_portas = quantidade_portas
        super().__init__(marca, modelo)
    
    def abrir_porta(self):
        print('abrindo portas')

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        self.cilindradas = cilindradas
        super().__init__(marca, modelo)
    
    def empinar(self):
        print('empinando moto')
