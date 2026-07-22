class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def ver_saldo(self):
        return self.__saldo
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print('valor adicionado')
        else:
            print('nao é possivel adicionar esse valor')


minha_conta = ContaBancaria("João", 100.0)

# Tentando depositar 50 reais
minha_conta.depositar(50.0)

# Verificando se o saldo atualizou para 150.0
print(f"Saldo atual: R$ {minha_conta.ver_saldo()}")

#=======================================================

class Usuario:
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha
        self.__falhas = 0
        self.__conta_bloqueada = False

    
    def logar_conta(self, login_digitado, senha_digitado):
        if self.__conta_bloqueada == True:
            print('conta bloquada')
            return False
        
        if login_digitado == self.__login and senha_digitado == self.__senha:
            print('conta logada')
            self.__falhas = 0
            return True
        else: 
            self.__falhas += 1
            if self.__falhas > 3:
                print('conta bloquada')
                self.__conta_bloqueada = True
                return False
            

#==========================================
                
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
