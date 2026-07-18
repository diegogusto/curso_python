import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    @abc.abstractmethod
    def sacar(self, valor): ...


    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f"(DEPOSITO {valor})")

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')
    

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo
        
        print('Nâo foi possivel sacar o valor desejado ')
        self.detalhes(f"(SAQUE NEGADO{valor})")


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_max = -self.limite

        if valor_pos_saque >= limite_max:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo
        
        print('Nâo foi possivel sacar o valor desejado ')
        print(f"Seu limite é {-self.limite:.2f}" )
        self.detalhes(f"(SAQUE NEGADO{valor})")
        return self.saldo
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r}'
        return f'{class_name}{attrs}'